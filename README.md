# Student Management System

A web-based Student Management System developed using Python, Django, MySQL, HTML, and CSS. This project helps manage student information through a simple and user-friendly interface.

## Features

- **Add Student:** Add new student records.
- **View Students:** Display all registered students.
- **Edit Student:** Update existing student details.
- **Delete Student:** Delete student records with a confirmation page.
- **Search Students:** Search by name, email, or course.
- **MySQL Database:** Store student information persistently.
- **User-Friendly Interface:** Styled pages for student lists and forms.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** MySQL
- **Version Control:** Git and GitHub

## Project Structure

```text
Studentmanagement/
├── manage.py
├── Studentmanagement/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
└── README.md
```

## Prerequisites

- Python 3.x
- Django
- MySQL Server
- Git

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/deekshithanaidu31/django-student-management-system.git
cd django-student-management-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django mysqlclient
```

Install any other database driver your project actually uses.

### 4. Configure the database

Create a MySQL database named `student_db` in MySQL Workbench or MySQL Server.

Configure the database credentials in Django's `settings.py` or through environment variables.


### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

## Future Enhancements

- User authentication and authorization
- Dashboard with student statistics
- Pagination for student records
- Additional form validation

