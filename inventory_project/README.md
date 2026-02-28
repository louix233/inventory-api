Inventory Management API

A simple Django REST API for managing inventory items and tracking stock history. Built as part of my Backend Engineering Capstone Project.

 Features
	•       User registration and login (JWT authentication)
	•	Create, view, update, and delete inventory items
	•	Filter items by category
	•	View low-stock items (quantity < threshold)
	•	Track stock history when quantity changes
	•	Each user manages only their own items

Main Endpoints

Authentication
Method 			Endpoint

POST			/api/users/register/
POST			/api/users/login/
GET			/api/users/me/

Items
Method			Endpoint

POST			/api/items/
GET			/api/items/
GET			/api/items/<id>/
PUT			/api/items/<id>/
DELETE			/api/items/<id>/
GET			/api/items/low-stock/
GET			/api/items/category/<category>/

Stock History
Method			Endpoint

GET			/api/items/<item_id>/history/
POST			/api/items/<item_id>/history/add/
