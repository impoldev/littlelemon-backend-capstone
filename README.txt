IMPORTANT: Update your MYSQL credentials in BASE_DIR/LittleLemon/settings.py

Static index.html:
/restaurant

APIs:
/restaurant/menu
/restaurant/menu/<int:pk>
/restaurant/booking
/restaurant/booking/tables
/restaurant/booking/tables/<int:pk>

Authentication:
restaurant/api-token-auth
/auth/users
/auth/users/me
/auth/users/resend_activation
/auth/users/set_password
/auth/users/reset_password
/auth/users/reset_password_confirm
/auth/users/set_username
/auth/users/reset_username
/auth/users/reset_username_confirm
/auth/token/login (Token Based Authentication)
/auth/token/logout (Token Based Authentication)