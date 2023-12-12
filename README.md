# varsity-pro-assignment

The objective of this assignment is to evaluate your proficiency in Django and Django Rest Framework (DRF) for building a Timesheet Software. The software should allow users to log their working hours for selected projects on a weekly basis.



## 🎯Features 

- **JWT Authentication:** Jsonwebtokens are used for user authentication, ensuring secure access to protected routes.

-**Authorization:** All types of requests are authorized to ensure only authenticated users can access the services.

-**Projects Mangement** The Projects Management API provides endpoints for creating, updating, and listing projects. Authenticated users can create and modify projects using the `POST` and `PUT` requests, respectively, while the `GET` endpoint allows them to retrieve a list of all projects or detailed information about a specific project using its primary key (`pk`).

**Timesheet Management:** The Timesheet Management API enables users to create, update, and retrieve timesheets. Authenticated users can create timesheets using a `POST` request, update their own timesheets with a `PUT` request, and retrieve a list of all their timesheets or details of a specific timesheet using the respective `GET` endpoints. Permissions are enforced to ensure users can only modify their own timesheets.


**User Management:** The User Authentication API facilitates user registration, login, and logout functionalities. Users can register by sending a `POST` request to the registration endpoint, log in using valid credentials through the login endpoint, and log out with a valid refresh token via the logout endpoint. JSON Web Tokens (JWT) are used for secure authentication and authorization.

- **Note:** Note:
All endpoints are decorated with @api_view(["POST"]) and @permission_classes([IsAuthenticated]) to ensure authentication and the use of proper HTTP methods.
HTTP status codes are appropriately used to indicate the outcome of each operation (e.g., HTTP_201_CREATED for successful creations, HTTP_400_BAD_REQUEST for validation errors).
Proper naming conventions and modularization have been applied to keep the code organized and readable.
The ProjectSerializer is utilized for data validation and serialization, promoting code reusability and maintaining consistency.


## 🚀Technologies Used 

- **Django 5.0**: A high-level Python web framework.
- **Django Rest Framework (DRF)**: A powerful and flexible toolkit for building Web APIs.
- **SQLite database**: A lightweight, file-based database engine.
- **Token-based Authentication using `rest_framework_simplejwt`**: Token-based authentication for securing API endpoints.

## Getting Started 🛠️

1. **Clone the Repository:**
   ```shell
   git clone https://github.com/adityaShar24/varsity-pro-assignment.git

2. **Navigate to the project directory:**
   ```shell
    cd src

2. **Create and activate a virtual environment (optional but recommended)**
   ```shell
    python -m venv venv
    source venv/bin/activate  
    On Windows, use `venv\Scripts\activate`


2. **Install project Dependencies:** 
    ```shell
    pip install -r requirements.txt
 

3. **Apply Database Migrations (Step1):** 
    ```shell
    python manage.py makemigrations

4. **Apply Database Migrations (Step2):** 
    ```shell
    python manage.py migrate

5. **Create Superuser:** 
    ```shell
    python manage.py createsuperuser
    username: admin
    password: admin   

5. **Run Development Server:** 
    ```shell
    python manage.py runserver    





## Contributing 🤝

Feel free to contribute to enhance the functionality of Todo-Application. Follow the [contribution guidelines](CONTRIBUTING.md) for more details.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/adityaShar24/varsity-pro-assignment/blob/main/LICENSE) file for details.

## Acknowledgments 🙏

Special thanks to the Django community and contributors for making this project possible.

Happy task managing! 😊






