# Agile JCS Quiz - Deployment Guide

This quiz app has been packaged and configured to be deployed on **Render** (a free hosting platform) or any other Node.js host!

Because Cloudflare tunnels are only meant for local testing, the `server.js` file is now fully production-ready. 

## How to Deploy to Render (Free)

1. **Create a GitHub Repository**: 
   - Go to [GitHub](https://github.com/) and create a new, private repository.
   - Upload all the files in this folder (`server.js`, `package.json`, `client.html`, `host.html`, `presentation.html`) into that repository.

2. **Create a Render Account**:
   - Go to [Render.com](https://render.com/) and sign up.
   - Click **New +** and select **Web Service**.
   - Connect your GitHub account and select your new repository.

3. **Configure the Service**:
   - **Name:** agile-jcs
   - **Environment:** Node
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`
   - **Instance Type:** Free

4. **Deploy!**
   - Click **Create Web Service**. 
   - Render will build and launch your app. In about 2 minutes, it will give you a public URL (e.g. `https://agile-jcs.onrender.com`).

That's it! 
Because `server.js` is now listening for Render's environment variables (`process.env.PORT` and `RENDER_EXTERNAL_URL`), the **QR code on the host dashboard will automatically match your new public Render link.**
