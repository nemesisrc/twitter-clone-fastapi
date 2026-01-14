---
# 🚀 Social Media Clone (FastAPI)

A **modern, high-performance social media backend** inspired by Twitter, built using **⚡ FastAPI**.  
This project focuses on **speed, scalability, clean API design, and real-world backend architecture**.

> 🧠 Designed for learning, experimentation, and real-world backend development best practices.

---

## ✨ Features

✅ User authentication & authorization  
✅ Create, read, update & delete posts  
✅ Like & comment system  
✅ Follow / Unfollow users  
✅ Feed generation  
✅ RESTful API design  
✅ JWT-based authentication  
✅ Clean project structure  
✅ Interactive API docs (Swagger & ReDoc)  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| 🚀 Backend | **FastAPI (Python)** |
| 🧩 API | REST |
| 🔐 Auth | JWT |
| 🗄️ Database | PostgreSQL / SQLite |
| 🔄 ORM | SQLAlchemy |
| ⚡ Server | Uvicorn |
| 📦 Dependency Mgmt | pip / venv |

---

## 📂 Project Structure

```

social-media-clone/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── database.py      # Database configuration
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── routes/          # API routes
│   ├── services/        # Business logic
│   ├── utils/           # Helper utilities
│
├── requirements.txt
├── .env.example
├── README.md
└── alembic/             # DB migrations

````

---

## 🚀 Getting Started (Run Locally)

Follow these steps to run the project on your local machine 👇

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/social-media-clone.git
cd social-media-clone
````

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Environment Variables Setup

Create a `.env` file using `.env.example`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/social_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 5️⃣ Run Database Migrations (If Using Alembic)

```bash
alembic upgrade head
```

---

### 6️⃣ Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Access the Application

| Service       | URL                                                        |
| ------------- | ---------------------------------------------------------- |
| 🚀 API        | [http://127.0.0.1:8000](http://127.0.0.1:8000)             |
| 📘 Swagger UI | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)   |
| 📕 ReDoc      | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |

---

## 🔐 Authentication Flow

1. Register a new user
2. Login to receive a **JWT token**
3. Use the token in headers:

```http
Authorization: Bearer <your_token_here>
```

---

## 🧪 Example API Endpoints

| Method | Endpoint             | Description   |
| ------ | -------------------- | ------------- |
| POST   | `/auth/register`     | Register user |
| POST   | `/auth/login`        | Login         |
| POST   | `/posts/`            | Create post   |
| GET    | `/posts/`            | Get feed      |
| POST   | `/posts/{id}/like`   | Like a post   |
| POST   | `/users/{id}/follow` | Follow user   |

---

## 📌 Why FastAPI?

⚡ Extremely fast (Starlette + Pydantic)
📄 Automatic API documentation
🧩 Easy to scale & maintain
🔒 Built-in validation & security
🚀 Production-ready

---

## 🧠 Learning Outcomes

✔ Designing scalable REST APIs
✔ Authentication using JWT
✔ Database modeling & relations
✔ Clean backend architecture
✔ Real-world FastAPI patterns

---

## 🛣️ Future Enhancements

🔹 Real-time notifications (WebSockets)
🔹 Media upload support
🔹 Search & trending posts
🔹 Caching with Redis
🔹 Rate limiting
🔹 Deployment with Docker

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo, open issues, or submit PRs 🙌

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you like this project, don’t forget to **star ⭐ the repository**
It helps a lot and keeps me motivated 😊

---