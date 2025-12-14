🧠🌾 KhetMitra – Backend
==================================================

KhetMitra Backend is the server-side application that powers
the KhetMitra platform. It manages authentication, user data,
crop recommendation logic, email services, and integration
with the machine learning model.

--------------------------------------------------
🌐 Backend Live API
--------------------------------------------------
🚀 Base URL:
https://khetmitra-backend.onrender.com/

--------------------------------------------------
🛠️ Tech Stack
--------------------------------------------------
🐍 Python  
⚙️ Flask  
🌐 Flask-CORS  
🗄️ MongoDB Atlas  
📧 Email Service (Resend / Gmail API)  
🤖 Machine Learning Model Integration  
🔐 Google OAuth (Token Verification)  
☁️ Render Deployment  

--------------------------------------------------
🔐 Environment Variables
--------------------------------------------------
Create a `.env` file in the backend root:

FLASK_ENV=production  
MONGO_URI=your_mongodb_atlas_uri  
GOOGLE_CLIENT_ID=your_google_client_id  
RESEND_API_KEY=your_resend_api_key  
FROM_EMAIL=your_verified_domain_email  

--------------------------------------------------
▶️ Run Backend Locally
--------------------------------------------------

1️⃣ Create virtual environment

python -m venv venv

Activate environment:
• macOS / Linux:
  source venv/bin/activate

• Windows:
  venv\Scripts\activate

--------------------------------------------------
2️⃣ Install dependencies
--------------------------------------------------

pip install -r requirements.txt

--------------------------------------------------
3️⃣ Start Flask server
--------------------------------------------------

python app.py

Server runs at:
http://localhost:5000

--------------------------------------------------
🚀 Deployment
--------------------------------------------------
☁️ Hosted on Render  
🔁 Auto-deploy enabled via GitHub  
🔐 Environment variables configured in Render Dashboard  
❌ SMTP blocked → Email API used instead  

--------------------------------------------------
🔗 Related Repositories
--------------------------------------------------
🎨 Frontend:
https://github.com/JeetNathwani26/khetmitr-frontend

🌾 Machine Learning / Model:
https://github.com/JeetNathwani26/khetmitra-model

--------------------------------------------------
⚠️ Common Issues
--------------------------------------------------
❗ MongoDB Atlas IP not whitelisted  
❗ Missing environment variables  
❗ SMTP not supported on Render  
❗ CORS configuration issues  

--------------------------------------------------
👨‍💻 Author
--------------------------------------------------
🧑‍💻 Jeet Nathwani  
🎯 Full Stack Developer  

--------------------------------------------------
🌍 Project
--------------------------------------------------
🚜 KhetMitra – Smart Agriculture Platform
==================================================
