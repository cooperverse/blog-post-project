📝 Blog Post Project

A clean and modular Blog API built using Django REST Framework (DRF), designed to handle blog posts, categories, comments, user authentication, and more.
This project follows professional best practices, clean architecture, and reusable components suitable for production-grade REST APIs.

🚀 Features
🧑‍💻 User & Auth

User Registration & Login (JWT Authentication)

Secure password handling

Permission-based access (only authors can edit/delete their posts)

📰 Blog Management

Create, read, update, and delete blog posts

Draft & published states

Slug-based post URLs

Category & Tag support

💬 Comments System

Add comments on posts

Nested/Threaded comments (optional)

Author-only edit/delete access

🔍 Extra Functionalities

Search posts by title/content

Filter posts by category/tag

Pagination enabled

Ordering (latest, oldest, most viewed — optional)

🛠️ Tech Stack

Python 3

Django

Django REST Framework

SimpleJWT

SQLite / PostgreSQL support

DRF Serializers, Viewsets & Routers

📁 Project Structure
blog-post-project/
│── blog/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│── config/
│   ├── settings.py
│   ├── urls.py
│── requirements.txt
│── README.md
