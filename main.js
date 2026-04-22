// --- Three.js Background Setup ---
const canvas = document.getElementById('bg-canvas');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);

// Create an abstract "Library Network" using Points and Lines
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 200; // Number of nodes

const posArray = new Float32Array(particlesCount * 3);
for(let i = 0; i < particlesCount * 3; i++) {
    // Spread particles in a wide area
    posArray[i] = (Math.random() - 0.5) * 20;
}

particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

// Material for nodes
const particlesMaterial = new THREE.PointsMaterial({
    size: 0.05,
    color: 0x023e8a,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
});

const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);

// Add lines connecting close nodes to simulate a network
const lineMaterial = new THREE.LineBasicMaterial({
    color: 0x023e8a,
    transparent: true,
    opacity: 0.25
});

// Create a line geometry connecting nearby points
const linePositions = [];
for(let i=0; i<particlesCount; i++) {
    const x1 = posArray[i*3];
    const y1 = posArray[i*3+1];
    const z1 = posArray[i*3+2];
    
    // Connect to a few random other points if they are close enough
    for(let j=i+1; j<particlesCount; j++) {
        const x2 = posArray[j*3];
        const y2 = posArray[j*3+1];
        const z2 = posArray[j*3+2];
        
        const dist = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2) + Math.pow(z2-z1, 2));
        if(dist < 3.0) { // connection threshold
            linePositions.push(x1, y1, z1);
            linePositions.push(x2, y2, z2);
        }
    }
}

const lineGeometry = new THREE.BufferGeometry();
lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
const lineMesh = new THREE.LineSegments(lineGeometry, lineMaterial);
scene.add(lineMesh);

camera.position.z = 8;

// Animation Loop for Three.js
let mouseX = 0;
let mouseY = 0;
let targetX = 0;
let targetY = 0;

const windowHalfX = window.innerWidth / 2;
const windowHalfY = window.innerHeight / 2;

document.addEventListener('mousemove', (event) => {
    mouseX = (event.clientX - windowHalfX);
    mouseY = (event.clientY - windowHalfY);
});

const clock = new THREE.Clock();

function animate3D() {
    requestAnimationFrame(animate3D);
    const elapsedTime = clock.getElapsedTime();

    // Rotate network slowly
    particlesMesh.rotation.y = elapsedTime * 0.05;
    particlesMesh.rotation.x = elapsedTime * 0.02;
    
    lineMesh.rotation.y = elapsedTime * 0.05;
    lineMesh.rotation.x = elapsedTime * 0.02;

    // Slight parallax effect on mouse move
    targetX = mouseX * 0.001;
    targetY = mouseY * 0.001;
    
    camera.position.x += (targetX - camera.position.x) * 0.05;
    camera.position.y += (-targetY - camera.position.y) * 0.05;
    camera.lookAt(scene.position);

    renderer.render(scene, camera);
}
animate3D();

// Handle Resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});


// --- Presentation Logic & GSAP Animations ---

const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
let currentSlide = 0;

const counter = document.getElementById('slide-counter');
const headerNav = document.querySelector('header');

// Initialize GSAP
gsap.registerPlugin();

function updateCounter() {
    counter.textContent = `${String(currentSlide + 1).padStart(2, '0')} / ${totalSlides}`;
    
    // Show navbar only on slide 1
    if (currentSlide === 0) {
        gsap.to(headerNav, {opacity: 1, duration: 0.3, onStart: () => headerNav.style.display = 'flex'});
    } else {
        gsap.to(headerNav, {opacity: 0, duration: 0.3, onComplete: () => headerNav.style.display = 'none'});
    }
}

function animateSlideIn(index) {
    const slide = slides[index];
    slide.classList.add('active');
    
    // Animate texts
    const texts = slide.querySelectorAll('.gsap-text');
    if(texts.length > 0) {
        gsap.fromTo(texts, 
            { y: 50, opacity: 0 }, 
            { y: 0, opacity: 1, duration: 0.8, stagger: 0.1, ease: "power3.out" }
        );
    }
    
    // Animate elements (cards, images)
    const elements = slide.querySelectorAll('.gsap-element');
    if(elements.length > 0) {
        gsap.fromTo(elements, 
            { y: 30, opacity: 0, scale: 0.95 }, 
            { y: 0, opacity: 1, scale: 1, duration: 0.6, stagger: 0.05, ease: "power2.out", delay: 0.3 }
        );
    }

    // Animate Workflow Video Wipe Effect
    const workflowImg = slide.querySelector('.workflow-anim');
    if (workflowImg) {
        gsap.fromTo(workflowImg, 
            { clipPath: 'inset(0 100% 0 0)' }, 
            { clipPath: 'inset(0 0% 0 0)', duration: 3.5, ease: 'power1.inOut', delay: 0.8 }
        );
    }

    // Move 3D camera slightly to give sense of progression
    gsap.to(camera.position, {
        z: 8 - (index * 0.2), // Zoom in slightly per slide
        duration: 1.5,
        ease: "power2.inOut"
    });
    // Rotate scene slightly to give sense of progression
    gsap.to(particlesMesh.rotation, {
        z: index * 0.5,
        duration: 1.5,
        ease: "power2.inOut"
    });
    gsap.to(lineMesh.rotation, {
        z: index * 0.5,
        duration: 1.5,
        ease: "power2.inOut"
    });
}

function animateSlideOut(index, direction) {
    const slide = slides[index];
    const elements = slide.querySelectorAll('.gsap-text, .gsap-element');
    
    gsap.to(elements, {
        y: direction === 'next' ? -50 : 50,
        opacity: 0,
        duration: 0.4,
        ease: "power2.in",
        onComplete: () => {
            slide.classList.remove('active');
            // reset styles for next time
            gsap.set(elements, { clearProps: "all" });
            
            const workflowImg = slide.querySelector('.workflow-anim');
            if (workflowImg) {
                gsap.set(workflowImg, { clearProps: "all" });
            }
        }
    });
}

function goToSlide(newIndex) {
    if(newIndex < 0 || newIndex >= totalSlides || newIndex === currentSlide) return;
    
    const direction = newIndex > currentSlide ? 'next' : 'prev';
    animateSlideOut(currentSlide, direction);
    
    // Small delay to let old slide fade out
    setTimeout(() => {
        currentSlide = newIndex;
        updateCounter();
        animateSlideIn(currentSlide);
    }, 400);
}

// Event Listeners
document.addEventListener('keydown', (e) => {
    if(e.key === 'ArrowRight' || e.key === 'Space') {
        goToSlide(currentSlide + 1);
    } else if(e.key === 'ArrowLeft') {
        goToSlide(currentSlide - 1);
    }
});

// Init first slide
updateCounter();
setTimeout(() => animateSlideIn(currentSlide), 100);

// --- Modal Logic for Images ---
const modal = document.getElementById('image-modal');
const modalImg = document.getElementById('img01');
const closeBtn = document.getElementsByClassName('close-modal')[0];
const zoomImages = document.querySelectorAll('.zoom-img');

zoomImages.forEach(img => {
    img.addEventListener('click', function() {
        modal.style.display = "block";
        modalImg.src = this.src;
        // animate modal in
        gsap.fromTo(modalImg, {scale: 0.8, opacity: 0}, {scale: 1, opacity: 1, duration: 0.3, ease: "back.out(1.7)"});
    });
});

closeBtn.addEventListener('click', () => {
    gsap.to(modalImg, {scale: 0.8, opacity: 0, duration: 0.2, onComplete: () => {
        modal.style.display = "none";
    }});
});

// Close modal on click outside image
modal.addEventListener('click', (e) => {
    if(e.target === modal) {
        closeBtn.click();
    }
});
