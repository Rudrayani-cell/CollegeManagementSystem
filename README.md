# 🎓 College Management System – Smart Dashboard

A web-based dashboard to manage students' academic performance, attendance, and notices — built using Flask, Firestore, and Bootstrap. Fully containerized and ready for deployment on Google Cloud Run.

---

## 🚀 Features

- 📊 **Student Dashboard**: View student name, marks, attendance, and notices.
- ✅ **Firestore Integration**: Real-time database using Google Firebase Firestore.
- 🧾 **Attendance Tracking**: View attendance % alongside marks.
- 📢 **Notices Panel**: Display notices for students on the dashboard.
- 💻 **Flask Backend**: Lightweight and easy to maintain.
- 🎨 **Bootstrap UI**: Clean, responsive layout.
- 🐳 **Docker Support**: Easily containerized and deployable.
- ☁️ **GCP-Ready**: Configured for Cloud Run deployment.

---

## 🛠️ Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| Frontend     | HTML5, CSS3, Bootstrap |
| Backend      | Python, Flask         |
| Database     | Google Firestore (Firebase) |
| Deployment   | Docker + Google Cloud Run |
| Version Ctrl | Git + GitHub          |

---


## 🌐 Live Demo

🚀 [Click here to view the live app](https://college-dashboard-xxxxx.a.run.app)  
_(Replace the above link with your actual deployed URL on GCP Cloud Run or any hosting platform)_
---

---

## 📷 Project Screenshot

![College Management System Dashboard](dashboard.jpg)

> Smart dashboard showing student marks, analytical comparison ,attendance, and notices.
---

## 📷 Project Screenshots

### 📊 Dashboard Overview
![Dashboard View](cloudproject2.jpg)

### 🧾 Student Record Table
![Student Table](cloudpro3.jpg)

### 🧑‍🏫 Admin Panel View
![Admin Panel](cloudpro4.jpg)

### 🔐 Login Page
![Login Page](cloudpro5.jpg)

## 🐳 Docker Support

### 📦 Build Docker Image

```bash
docker build -t college-dashboard .

## ⚙️ Step-by-Step Setup (Local)

### 🔄 1. Clone the Project
```bash
git clone https://github.com/Rudrayani-cell/CollegeManagementSystem.git
cd CollegeManagementSystem

---

### ✅ 2. Save the file  
Make sure `README.md` is saved properly with markdown formatting (no code block cut-off).

---

### ✅ 3. Add, Commit & Push

In your terminal:

```bash
git add README.md
git commit -m "Added Docker build instructions and setup guide"
git push origin main

## ▶️ Run Docker Container
docker run -p 8080:8080 college-dashboard

## 🗂️ Folder Structure
college-management-system/
├── app.py
├── templates/
│ ├── layout.html
│ └── dashboard.html
├── static/
├── firebase-key.json (ignored)
├── .env
├── Dockerfile
├── README.md
└── requirements.txt


---

## 👩‍💻 Author

Built with 💡 by [Rudrayani-cell](https://github.com/Rudrayani-cell)


