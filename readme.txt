LittleLemon Django API Endpoints
==============================

Authentication & User Management
--------------------------------
- Register new user:         POST /auth/users/
- Login (get token):         POST /auth/token/login/
- Logout (invalidate token): POST /auth/token/logout/
- Get user list:             GET /auth/users/

Token Authentication
--------------------
- Obtain token:              POST /restaurant/api-token-auth/
  (Body: username, password)

Menu API
--------
- List menu items:           GET /restaurant/menu/
- Create menu item:          POST /restaurant/menu/
- Retrieve menu item:        GET /restaurant/menu/<id>
- Update menu item:          PUT /restaurant/menu/<id>
- Delete menu item:          DELETE /restaurant/menu/<id>

Table Booking API
-----------------
- List bookings:             GET /restaurant/booking/tables/
- Create booking:            POST /restaurant/booking/tables/
- Retrieve booking:          GET /restaurant/booking/tables/<id>/
- Update booking:            PUT /restaurant/booking/tables/<id>/
- Delete booking:            DELETE /restaurant/booking/tables/<id>/

Notes
-----
- All menu and booking endpoints require authentication via token.
- Include header: Authorization: Token <your_token>
- Use the browsable API or tools like Postman/Insomnia for testing.
