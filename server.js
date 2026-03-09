const express = require('express');
const http = require('http');
const { Server } = require("socket.io");
const os = require('os');
const qrcode = require('qrcode');
const { spawn } = require('child_process');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: { origin: "*" }
});

// Enable CORS and disable caching for all routes (to prevent browser cache issues on Render)
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Cache-Control", "no-cache, no-store, must-revalidate");
    res.header("Pragma", "no-cache");
    res.header("Expires", "0");
    next();
});

// Serve the static files from current directory
app.use(express.static(__dirname));

// Redirect root to presentation deck
app.get('/', (req, res) => {
    res.redirect('/presentation.html');
});

// Quiz Data based on the presentation
const quizQuestions = [
    {
        id: 1,
        text: "In Extreme Programming (XP), what is the rule about when you should write your automated tests?",
        options: ["At the very end of the project.", "Before you write the actual code.", "Only when the user complains.", "After you design the logo."],
        correctIndex: 1,
        funFact: "Test-Driven Development (TDD) ensures code always has a safety net."
    },
    {
        id: 2,
        text: "According to Lean Engineering, what happens when you try to work on 5 large tasks at the exact same time?",
        options: ["The code becomes perfect.", "You get done much faster.", "Everything takes much longer.", "You become a master coder."],
        correctIndex: 2,
        funFact: "Context switching creates immense mental waste."
    },
    {
        id: 3,
        text: "How does a Kanban board prevent the team from doing too many things at once?",
        options: ["By skipping team meetings.", "By putting a limit on active tasks.", "By complaining to the boss.", "By avoiding new tasks completely."],
        correctIndex: 1,
        funFact: "WIP (Work In Progress) Limits are the engine of Kanban."
    },
    {
        id: 4,
        text: "What does \"Technical Debt\" refer to in software engineering?",
        options: ["A bank loan to buy servers.", "Messy, hard-to-change code caused by rushing.", "Paying software engineers too much.", "A type of database error."],
        correctIndex: 1,
        funFact: "Rushing now means paying with interest later."
    },
    {
        id: 5,
        text: "In \"Pair Programming\", how do two engineers work together?",
        options: ["Both type on different keyboards to code faster.", "One person writes code, the other reviews it instantly.", "One person codes while the other takes a break.", "One plans the UI, the other codes the database."],
        correctIndex: 1,
        funFact: "Driver and Navigator dynamic cuts bugs dramatically."
    },
    {
        id: 6,
        text: "What is the main goal of Continuous Integration (CI) in XP?",
        options: ["To merge code frequently to avoid huge conflicts.", "To mathematically prove the code has no bugs.", "To work continuously without any breaks.", "To create integrations between different websites."],
        correctIndex: 0,
        funFact: "Merge often to avoid 'Merge Hell'."
    },
    {
        id: 7,
        text: "In Lean Engineering, what perfectly defines \"Waste\"?",
        options: ["Taking too many lunch breaks.", "Deleting old project files.", "Writing too many automated tests.", "Anything the customer does not care about."],
        correctIndex: 3,
        funFact: "If the user doesn't value it, don't build it."
    },
    {
        id: 8,
        text: "Little's Law proves that if you want to finish a project faster, you MUST...",
        options: ["Multitask as much as humanly possible.", "Decrease the number of items currently in progress.", "Work late into the night every day.", "Buy faster computers for the engineers."],
        correctIndex: 1,
        funFact: "Stop starting, start finishing!"
    }
];

// Game State
let gameState = {
    status: 'LOBBY', // 'LOBBY', 'QUESTION_ACTIVE', 'QUESTION_RESULTS', 'LEADERBOARD', 'END'
    currentQuestionIndex: 0,
    players: {}, // socketId -> { name, score, currentAnswer, hasAnswered }
    timeLeft: 0,
    answersCount: [0, 0, 0, 0] // Count of votes for options 0,1,2,3
};

let timerInterval = null;

// Get Local IP
function getLocalIP() {
    const interfaces = os.networkInterfaces();
    for (const devName in interfaces) {
        const iface = interfaces[devName];
        for (let i = 0; i < iface.length; i++) {
            const alias = iface[i];
            if (alias.family === 'IPv4' && alias.address !== '127.0.0.1' && !alias.internal)
                return alias.address;
        }
    }
    return '127.0.0.1';
}

const LOCAL_IP = getLocalIP();
const PORT = 3000;

io.on('connection', (socket) => {
    // When a player joins
    socket.on('join_game', (playerName) => {
        gameState.players[socket.id] = {
            name: playerName,
            score: 0,
            currentAnswer: null,
            hasAnswered: false
        };
        socket.emit('join_success');
        io.emit('state_update', getPublicState());
    });

    // When the host starts the game
    socket.on('host_start_game', () => {
        gameState.currentQuestionIndex = 0;
        resetAnswers();
        startQuestion();
    });

    // When the host moves to next question
    socket.on('host_next_question', () => {
        gameState.currentQuestionIndex++;
        if (gameState.currentQuestionIndex >= quizQuestions.length) {
            gameState.status = 'END';
            io.emit('state_update', getPublicState());
        } else {
            resetAnswers();
            startQuestion();
        }
    });

    // When the host shows leaderboard
    socket.on('host_show_leaderboard', () => {
        gameState.status = 'LEADERBOARD';
        io.emit('state_update', getPublicState());
    });

    // When the host restarts the entire game
    socket.on('host_restart_game', () => {
        gameState.status = 'LOBBY';
        gameState.currentQuestionIndex = 0;
        resetAnswers();

        // Wipe all player scores and answer states, but keep them in the lobby
        Object.values(gameState.players).forEach(p => {
            p.score = 0;
            p.hasAnswered = false;
            p.currentAnswer = null;
        });

        if (timerInterval) clearInterval(timerInterval);

        io.emit('state_update', getPublicState());
    });

    // When the host manually skips the timer
    socket.on('host_skip_timer', () => {
        if (gameState.status === 'QUESTION_ACTIVE' && timerInterval) {
            clearInterval(timerInterval);
            gameState.timeLeft = 0;
            gameState.status = 'QUESTION_RESULTS';
            io.emit('state_update', getPublicState());
        }
    });

    // When player answers
    socket.on('submit_answer', (answerIndex) => {
        const player = gameState.players[socket.id];
        if (player && gameState.status === 'QUESTION_ACTIVE' && !player.hasAnswered) {
            player.hasAnswered = true;
            player.currentAnswer = Number(answerIndex);
            gameState.answersCount[player.currentAnswer]++;

            // Give point based on speed (integer match!)
            const correctIndex = Number(quizQuestions[gameState.currentQuestionIndex].correctIndex);
            if (player.currentAnswer === correctIndex) {
                // Bonus for answering faster
                const scoreGained = 100 + (gameState.timeLeft * 5);
                player.score += scoreGained;
            }

            // Acknowledge answer
            socket.emit('answer_received');

            // Just update host with answer counts
            io.emit('state_update', getPublicState());
        }
    });

    // Disconnect
    socket.on('disconnect', () => {
        if (gameState.players[socket.id]) {
            delete gameState.players[socket.id];
            io.emit('state_update', getPublicState());
        }
    });
});

function resetAnswers() {
    gameState.answersCount = [0, 0, 0, 0];
    Object.values(gameState.players).forEach(p => {
        p.hasAnswered = false;
        p.currentAnswer = null;
    });
}

function startQuestion() {
    gameState.status = 'QUESTION_ACTIVE';
    gameState.timeLeft = 20; // 20 seconds per question

    io.emit('state_update', getPublicState());

    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        gameState.timeLeft--;
        if (gameState.timeLeft <= 0) {
            clearInterval(timerInterval);
            gameState.status = 'QUESTION_RESULTS';
        }
        io.emit('state_update', getPublicState());
    }, 1000);
}

// Prepare state to send to clients without exposing answers when active
function getPublicState() {
    let q = quizQuestions[gameState.currentQuestionIndex];
    let publicQ = null;

    if (gameState.status === 'QUESTION_ACTIVE' || gameState.status === 'QUESTION_RESULTS') {
        const q = quizQuestions[gameState.currentQuestionIndex];
        publicQ = {
            text: q.text,
            options: q.options,
            // Only send the correct answer when it's results time
            correctIndex: gameState.status === 'QUESTION_RESULTS' ? Number(q.correctIndex) : null,
            funFact: gameState.status === 'QUESTION_RESULTS' ? q.funFact : null
        };
    }

    // Sort leaderboard
    let leaderboard = Object.values(gameState.players)
        .sort((a, b) => b.score - a.score)
        .map(p => ({ name: p.name, score: p.score }));

    return {
        status: gameState.status,
        questionIndex: gameState.currentQuestionIndex,
        totalQuestions: quizQuestions.length,
        question: publicQ,
        timeLeft: gameState.timeLeft,
        leaderboard: leaderboard,
        // Host only info really, but ok to broadcast so it animates bars
        answersCount: gameState.answersCount,
        totalPlayers: Object.keys(gameState.players).length,
        answersReceived: Object.values(gameState.players).filter(p => p.hasAnswered).length,
        joinUrl: `${publicUrl}/client.html`
    };
}

// Cloudflare tunneling completely removed in favor of Render deployment

// Generate QR Code dynamically
app.get('/qrcode', async (req, res) => {
    try {
        const url = `${publicUrl}/client.html`;
        const qrImage = await qrcode.toDataURL(url, {
            color: {
                dark: '#0f172a',  // Slate-900
                light: '#ffffff' // White
            },
            width: 400
        });
        res.send(`<img src="${qrImage}" />`);
    } catch (err) {
        res.status(500).send('Failed to generate QR');
    }
});

// When deployed on Render, this environment variable contains the actual public URL (e.g. https://agile-jcs.onrender.com)
publicUrl = process.env.RENDER_EXTERNAL_URL || `http://${LOCAL_IP}:${PORT}`;

server.listen(PORT, '0.0.0.0', () => {
    console.log(`\n=================================================`);
    console.log(`🚀 QUIZ SERVER RUNNING ON PORT ${PORT}`);
    console.log(`=================================================`);
    console.log(`🖥️  Host view:   ${publicUrl}/host.html`);
    console.log(`📱 Player Join: ${publicUrl}/client.html`);
    console.log(`=================================================\n`);
});
