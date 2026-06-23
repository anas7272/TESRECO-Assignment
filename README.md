# TESRECO Internship Management Portal

## Overview

TESRECO Internship Management Portal is a Flask-based web application developed to manage interns, mentors, attendance, and internship activities.

The project demonstrates the practical implementation of:

* Python Programming
* Object-Oriented Programming (OOP)
* Exception Handling
* File Handling (CSV)
* Logging
* SQLite Database Integration
* Flask Web Development
* REST APIs
* Jinja2 Templates
* CRUD Operations

The portal allows administrators to register interns, manage intern records, assign mentors, record attendance, and interact with data through both APIs and web pages.

---

# Features

## Home Page

Route:

```text
/
```

Displays:

* TESRECO Internship Program Welcome Page
* Organization Branding
* Styled User Interface

---

## About Page

Route:

```text
/about
```

Displays:

* Organization Overview
* Internship Domains
* Mission
* Vision

Implemented using:

* Flask
* Jinja2 Templates

---

## Intern Management APIs

### Register Intern

```http
POST /register
```

Sample Request:

```json
{
    "name":"Vaibhav",
    "email":"vaibhav@gmail.com",
    "domain":"Data Science"
}
```

Stores intern details in SQLite.

---

### View Interns

```http
GET /interns
```

Returns all registered interns in JSON format.

---

### Update Intern

```http
PUT /intern/<id>
```

Updates intern details.

---

### Delete Intern

```http
DELETE /intern/<id>
```

Deletes intern record.

---

## Attendance Module

### Record Attendance

```http
POST /attendance
```

Sample Request:

```json
{
    "intern_id":1,
    "date":"2026-06-23",
    "status":"Present"
}
```

Stores attendance records in SQLite.

---

## Mentor Assignment Module

### Assign Mentor

```http
POST /assign-mentor
```

Sample Request:

```json
{
    "intern_id":1,
    "mentor_id":2
}
```

Assigns mentors to interns.

---

## Web CRUD Application

### Add Intern

```text
/add-intern
```

Create new intern records using a web form.

---

### View Interns

```text
/view-interns
```

Displays all intern records.

---

### Edit Intern

```text
/edit/<id>
```

Update intern information.

---

### Delete Intern

```text
/delete/<id>
```

Delete intern records.

---

# Project Structure

```text
TESRECO_PORTAL/
│
├── app.py
│
├── database/
│   └── interns.db
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── add_intern.html
│   ├── view_interns.html
│   ├── edit_intern.html
│   └── delete_intern.html
│
├── static/
│   ├── logo.png
│   └── style.css
│
├── logs/
│   └── tesreco.log
│
├── README.md
│
└── requirements.txt
```

---

# Database Design

## Interns Table

| Column | Type    |
| ------ | ------- |
| id     | INTEGER |
| name   | TEXT    |
| email  | TEXT    |
| domain | TEXT    |

---

## Mentors Table

| Column         | Type    |
| -------------- | ------- |
| mentor_id      | INTEGER |
| name           | TEXT    |
| specialization | TEXT    |

---

## Attendance Table

| Column    | Type    |
| --------- | ------- |
| id        | INTEGER |
| intern_id | INTEGER |
| date      | TEXT    |
| status    | TEXT    |

---

## Assignments Table

| Column    | Type    |
| --------- | ------- |
| id        | INTEGER |
| intern_id | INTEGER |
| mentor_id | INTEGER |

---

# Technologies Used

## Backend

* Python 3.x
* Flask

## Database

* SQLite3

## Frontend

* HTML5
* CSS3
* Jinja2 Templates

## Tools

* Postman
* VS Code
* Git
* GitHub

---

# Installation

## Clone Repository

```bash
git clone <repository-link>
```

---

## Move into Project Directory

```bash
cd TESRECO_PORTAL
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

Create a requirements.txt file containing:

```text
Flask
```

Install using:

```bash
pip install Flask
```

---

# Running the Application

Start Flask Server:

```bash
python app.py
```

Expected Output:

```text
* Running on http://127.0.0.1:5000
```

Open Browser:

```text
http://127.0.0.1:5000
```

---

# API Testing

Use Postman to test:

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /register      |
| GET    | /interns       |
| PUT    | /intern/<id>   |
| DELETE | /intern/<id>   |
| POST   | /attendance    |
| POST   | /assign-mentor |

---

# Logging

Application logs are stored in:

```text
tesreco.log
```

Logged Activities:

* User Login Events
* Error Logs
* Report Generation Activities

---

# Completed Assignment Tasks

## Core Python Tasks

* Intern Class Design
* Constructor
* Getter & Setter Concepts
* **str** Method
* Decorators
* Performance Calculator
* Custom Iterator
* Generator Function
* Custom Exceptions
* Shallow Copy vs Deep Copy
* Multiple Inheritance
* Method Resolution Order (MRO)
* Abstract Classes
* Lambda Functions
* Functional Programming
* CSV File Handling
* Search & Delete Operations
* Multithreading
* Multiprocessing
* Logging
* SQLite Integration
* CRUD Operations

---

## Flask Tasks

* Home Page
* About Page
* Register Intern API
* View Interns API
* Update Intern API
* Delete Intern API
* Attendance Module
* Mentor Assignment Module
* CRUD Web Application
* SQLite Integration
* Jinja2 Templates

---

# Future Improvements

* Authentication & Authorization
* Dashboard Analytics
* Attendance Reports
* Email Notifications
* Export Data to CSV/PDF
* Admin Panel
* Search & Filter Functionality

---

# Author

Anas Khan

B.Tech Artificial Intelligence

SAGE University, Indore

---

# License

This project is developed for educational and internship learning purposes under the TESRECO Internship Program.
