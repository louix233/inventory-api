Inventory Management API

A simple, fully functional Inventory Management REST API built with Django and Django REST Framework, created as part of the Backend Capstone Project.

This API allows authenticated users to:

Register & login

Create, view, update, and delete inventory items

Track low-stock items

Filter items by category

View stock update history per item



Live API (PythonAnywhere Deployment)

Base URL:

https://louix.pythonanywhere.com/

Example endpoints:

POST /api/users/register/
POST /api/users/login/
GET  /api/items/
POST /api/items/
GET  /api/items/low-stock/
GET  /api/items/category/<category>/
GET  /api/items/<id>/history/
🗄️ Database ERD

The project uses 3 core entities:

User 1 ────∞ Item 1 ────∞ StockHistory
Entities
User

id

username

email

password

date_joined

Item

id

name

category

quantity

description

threshold

created_by (FK → User)

created_at

StockHistory

id

item_id (FK → Item)

old_quantity

new_quantity

updated_by (FK → User)

updated_at



Authentication (JWT)

The API uses JSON Web Tokens (JWT).

Register
POST /api/users/register/
Login
POST /api/users/login/

Response contains:

access: <token>
refresh: <token>

Use the access token in all authenticated requests:

Authorization: Bearer <token>
Endpoints Summary
Users
Method	Endpoint	Description
POST	/api/users/register/	Register new user
POST	/api/users/login/	Login user (JWT)
GET	/api/users/me/	Current logged-in user

Items
Method	Endpoint	Description
GET	/api/items/	List user items
POST	/api/items/	Create new item
GET	/api/items/<id>/	Retrieve item
PUT	/api/items/<id>/	Update item
DELETE	/api/items/<id>/	Delete item
GET	/api/items/low-stock/	Items below threshold
GET	/api/items/category/<category>/	Filter by category


 Stock History
Method	Endpoint	Description
GET	/api/items/<id>/history/	View stock update history
POST	/api/items/<id>/history/	Add new stock record


Tech Stack

Python 3

Django 5+

Django REST Framework

SimpleJWT

SQLite (local)

PythonAnywhere (deployment)

Running the Project Locally

git clone https://github.com/louix233/inventory-api.git
cd inventory-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Louis Dziwornu Alevi
Capstone Project