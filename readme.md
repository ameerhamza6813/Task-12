# FastAPI To-Do List App with PostgreSQL and S3 CSV Export

This is a full-stack to-do list web application built using **FastAPI**, **PostgreSQL**, and **Amazon S3**. The app supports **CRUD operations** on tasks, stores data in a PostgreSQL database, and allows exporting task data as a CSV file to an S3 bucket.

---

## Features

- Create, Read, Update, and Delete (CRUD) To-Do tasks
- PostgreSQL database integration
- Export tasks as CSV to an AWS S3 bucket
- Dummy data seeding for testing
- Modular FastAPI architecture

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Storage:** Amazon S3 (CSV export)
- **ORM:** SQLAlchemy
- **CSV Export:** Python CSV module + `boto3`

---

##  Project Structure
├── app/
│ ├── main.py # FastAPI app and endpoints
│ ├── models.py # SQLAlchemy models
│ ├── database.py # DB engine and session
│ ├── crud.py # CRUD logic
│ ├── schemas.py # Pydantic schemas
│ ├── utils.py # Utility functions (e.g. S3 upload)
├── seed_db.py # Dummy data seeder script
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ameerhamza6813/task12.git
cd todo-fastapi-postgres-s3

2. Install Dependencies
bash

pip install -r requirements.txt

3. Configure Database
Update your PostgreSQL credentials in database.py:

DATABASE_URL = "postgresql+psycopg2://username:password@hostname:port/dbname"

4. Create the Database Tables
bash

>>> from models import Base
>>> from database import engine
>>> Base.metadata.create_all(bind=engine)

6. Start the FastAPI Server
bash

uvicorn app.main:app --reload

Requirements
Python 3.8+

PostgreSQL 12+

AWS account with an S3 bucket

boto3, sqlalchemy, fastapi, uvicorn

