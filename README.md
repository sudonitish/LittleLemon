# LittleLemon Django Capstone Project

## Overview
LittleLemon is a Django-based restaurant management API project. It provides endpoints for menu management, table booking, and user authentication using Django REST Framework and Djoser.

## Features
- User registration, login, and logout (token-based authentication)
- Menu management (CRUD)
- Table booking management (CRUD)
- MySQL database integration
- Unit tests for models and views

## Project Structure
- `littlelemon/` - Django project folder
- `restaurant/` - Django app for menu and booking
- `tests/` - Unit tests for models and views


## Setup Instructions

### 1. Install Python
- Download and install Python 3.10 or newer from the [official website](https://www.python.org/downloads/).
- Make sure to check "Add Python to PATH" during installation.

### 2. Clone the repository
```sh
git clone <your-repo-url>
cd LittleLemon
```

### 3. Create and activate a virtual environment
On Windows:
```sh
python -m venv env
env\Scripts\activate
```
On macOS/Linux:
```sh
python3 -m venv env
source env/bin/activate
```

### 4. Install dependencies
```sh
pip install -r requirements.txt
```

### 5. Configure your MySQL database
- Edit `littlelemon/settings.py` and update the `DATABASES` section with your MySQL credentials.
- Make sure your MySQL server is running and the database exists.

### 6. Run migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser
```sh
python manage.py createsuperuser
```

### 8. Start the server
```sh
python manage.py runserver
```

## API Endpoints

### Authentication & User Management
- Register: `POST /auth/users/`
- Login: `POST /auth/token/login/`
- Logout: `POST /auth/token/logout/`
- User list: `GET /auth/users/`

### Token Authentication
- Obtain token: `POST /restaurant/api-token-auth/` (body: username, password)

### Menu API
- List menu items: `GET /restaurant/menu/`
- Create menu item: `POST /restaurant/menu/`
- Retrieve menu item: `GET /restaurant/menu/<id>`
- Update menu item: `PUT /restaurant/menu/<id>`
- Delete menu item: `DELETE /restaurant/menu/<id>`

### Table Booking API
- List bookings: `GET /restaurant/booking/tables/`
- Create booking: `POST /restaurant/booking/tables/`
- Retrieve booking: `GET /restaurant/booking/tables/<id>/`
- Update booking: `PUT /restaurant/booking/tables/<id>/`
- Delete booking: `DELETE /restaurant/booking/tables/<id>/`

## Notes
- All menu and booking endpoints require authentication via token.
- Include header: `Authorization: Token <your_token>`
- Use the browsable API or tools like Postman/Insomnia for testing.

## Testing
- Run all tests:
  ```sh
  python manage.py test
  ```

## License
This project is for educational purposes.
