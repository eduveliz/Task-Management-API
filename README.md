# ️ Task Management API

A RESTful API built with **FastAPI** and **SQLAlchemy** to manage **projects**, **task lists** (like Trello), and **individual tasks**. Designed as an educational project to improve Python, relational database, and nested structure skills.

---

##  Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite (easily switchable to PostgreSQL)
- Pydantic

---

## Project Structure

```
Task-Management-API/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── project.py
│   │   ├── list.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── project.py
│   │   ├── list.py
│   │   └── task.py
│   ├── routers/
│   │   ├── project.py
│   │   ├── list.py
│   │   └── task.py
│   └── create_tables.py
├── requirements.txt
└── README.md
```

---

## ️ Installation

1. Clone the repository:

```bash
git clone https://github.com/eduveliz/Task-Management-API.git
cd Task-Management-API
```

2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create the database tables:

```bash
python create_tables.py
```

This will generate a `tasks.db` file (if you're using SQLite).

---

##  Run the Server

Launch the development server with:

```bash
uvicorn app.main:app --reload
```

Access the auto-generated API docs:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

##  Key Endpoints

| Method | Route                | Description            |
|--------|----------------------|------------------------|
| POST   | `/projects/`         | Create a new project   |
| GET    | `/projects/`         | List all projects      |
| POST   | `/lists/`            | Create a new list      |
| GET    | `/lists/`            | List all lists         |
| POST   | `/tasks/`            | Create a new task      |
| GET    | `/tasks/`            | List all tasks         |

---

##  Next Steps

- [ ] Support for nested endpoints (`/projects/{id}/lists`)
- [ ] User authentication
- [ ] Deploy on Render or Railway
- [ ] Write tests with pytest

---

##  Author

Developed by **Eduardo Veliz** as a personal project to deepen Python and backend knowledge.

---

##  License

This project is licensed under the MIT License. See the `LICENSE` file for details.
