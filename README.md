# 🔧 Gas Utility Customer Support Portal

A Django-based web application for managing customer service requests, tracking their status, and providing tools for support representatives. Built for internal use at a gas utility company.

---

## 📚 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
  
---

## ✨ Features

### 👥 For Customers
- Register, login, and manage account
- Submit service requests
- Track the status of submitted requests

### 🛠️ For Support Reps (CSR/Admin)
- View all service requests
- Update request status and assign reps
- View customer info and request history

---

## 🏗️ Project Structure
```bash
gas-support-portal/
│
├── accounts/             
├── gas_utility_service/  
├── service_requests/    
├── support_dashboard/
├── templates/
└── manage.py

## ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/gas-support-portal.git
   cd gas-support-portal
   ```
2. **Create virtual environment**
   ```bash
  python -m venv venv
  source venv/bin/activate      # Linux/macOS
  venv\Scripts\activate         # Windows
   ```
3. **Apply migrations**
  ```bash
  python manage.py makemigrations
  python manage.py migrate
   ```
4. **Create superuser**
  ```bash
  python manage.py createsuperuser
  ```

5. **Run development server**

  ```bash
  python manage.py runserver
  ```

## 🚀 Running the Project

Once the server is running, visit:
http://127.0.0.1:8000/ — Home
http://127.0.0.1:8000/admin/ — Admin panel
