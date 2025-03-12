# Little Lemon - Back-End Developer Capstone

Welcome to the **Little Lemon** restaurant backend, a capstone project for the Meta Back-End Developer certification. This project provides a set of APIs to manage the restaurant's menu, bookings, and authentication.

## Features

- RESTful APIs for menu and booking management.
- Authentication and user management.
- Static HTML index page for the restaurant.

## API Endpoints

### Menu Endpoints

- `GET /restaurant/menu` - Retrieve the menu.
- `GET /restaurant/menu/<int:pk>` - Retrieve a specific menu item.

### Booking Endpoints

- `GET /restaurant/booking` - Retrieve basic root view for DefaultRouter.
- `GET /restaurant/booking/tables` - Retrieve all bookings.
- `GET /restaurant/booking/tables/<int:pk>` - Retrieve a specific booking.

### Authentication Endpoints (Djoser)

- **User Registration & Management:**
   - `GET, POST /auth/users` - Retrieve users and create a new user.
   - `GET /auth/users/me` - Retrieve the authenticated user's details.
   - `POST /auth/users/resend_activation` - Resend activation email.
   - `POST /auth/users/set_password` - Set a new password.
   - `POST /auth/users/reset_password` - Request a password reset.
   - `POST /auth/users/reset_password_confirm` - Confirm password reset.
   - `POST /auth/users/set_username` - Set a new username.
   - `POST /auth/users/reset_username` - Request a username reset.
   - `POST /auth/users/reset_username_confirm` - Confirm username reset.

- **Token Authentication:**
   - `POST /auth/token/login` - Obtain an authentication token.
   - `POST /auth/token/logout` - Logout and invalidate token.

### Other Authentication Endpoint
- `POST /restaurant/api-token-auth` - Obtain an API token.

### Static HTML Page

- `GET /restaurant` - Serves the static `index.html` page. This page is almost empty and is primarily used to confirm that templates and static files are properly configured.

## Installation

### Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/impoldev/littlelemon-backend-capstone.git
   cd BASE_DIR
   ```
2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv ../venv
   source ../venv/bin/activate  # On Windows use `..\venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Update MySQL credentials**
   **IMPORTANT:** Edit `BASE_DIR/LittleLemon/settings.py` and update your MySQL database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'your_mysql_host',
           'PORT': 'your_mysql_port',
       }
   }
   ```
5. **Apply database migrations**
   ```sh
   python manage.py migrate
   ```
6. **Create a superuser (optional, for admin access)**
   ```sh
   python manage.py createsuperuser
   ```
7. **Run the server**
   ```sh
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the APIs using Postman, cURL, or a web browser.

## License

This project is for educational purposes.

---

Feel free to suggest improvements!

