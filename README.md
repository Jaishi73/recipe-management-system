# Recipe Management System (Django)

# Description
A Django-based Recipe Management System that allows users to:
- Add, view, edit, and delete recipes
- Upload recipe images or provide image URLs
- Filter recipes by category
- Store data in a database (SQLite/MySQL)
- Use clean UI with HTML and CSS

# Features
- Full CRUD operations
- Image upload & image URL support
- Category filtering
- Client-side & server-side validation
- Clean and responsive UI
- Django MVC architecture

# Tech Stack
- Python 3.12
- Django 6.0
- HTML5
- CSS3
- SQLite / MySQL

# How to Run the Project
```bash
git clone <repo-link>
cd recipe_management_system
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
