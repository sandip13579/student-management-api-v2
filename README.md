Student Management API V2

A Student Management API built using **FastAPI** and **SQLite**. This project demonstrates CRUD (Create, Read, Update, Delete) operations with a database-backed REST API.

 Features

* Add a new student
* View all students
* Get student details
* Update student information
* Delete student records
* SQLite database integration
* Interactive API documentation using Swagger UI

 Tech Stack

* Python
* FastAPI
* Pydantic
* SQLite
* Uvicorn

 Project Structure

```text
student_management_V2.py
SIT_students.db
README.md
```

 Student Model

```python
class student(BaseModel):
    SIC: str
    name: str
    roll_no: int
```

 API Endpoints

 Add Student

```http
POST /students
```

 Get All Students

```http
GET /students
```

 Update Student

```http
PUT /students/UPDATE/{student_name}
```

 Delete Student

```http
DELETE /students/DELETE/{student_SIC}
```

 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/student-management-api-v2.git
```

Move into the project directory:

```bash
cd student-management-api-v2
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the application:

```bash
python -m uvicorn student_management_V2:app --reload
```

 API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows testing all API endpoints directly from the browser.

 Learning Outcomes

Through this project I learned:

* FastAPI fundamentals
* REST API development
* CRUD operations
* SQLite database integration
* Pydantic models
* API testing using Swagger UI

 Future Improvements

* Add search by roll number
* Add input validation
* Improve error handling
* Use SQLAlchemy ORM
* Add authentication and authorization

 Author

Sandip Panigrahi
First-Year Engineering Student | Python & Backend Development Enthusiast
