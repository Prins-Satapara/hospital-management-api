# 🏥 Hospital Management API

A simple REST API built with **FastAPI** to manage patient records using CRUD operations.

## 🚀 Features

- View all patients
- View a patient by ID
- Create a new patient
- Update patient details
- Delete a patient
- Sort patients by Height, Weight, or BMI
- Automatic request validation using Pydantic

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- JSON (as a database)

## 📂 Project Structure

```
hospital-management-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── routers/
│   └── services/
│
├── data/
│   └── patients.json
│
├── .gitignore
├── requirements.txt
└── README.md
```

## API Documentation

Swagger UI

![Swagger](images/swagger.png)

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/<Prins-Satapara>/hospital-management-api.git
```

2. Move to the project directory

```bash
cd hospital-management-api
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the server

```bash
uvicorn app.main:app --reload
```

## 📖 API Documentation

After starting the server, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc