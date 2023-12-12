# varsity-pro-assignment

The objective of this assignment is to evaluate your proficiency in Django and Django Rest Framework (DRF) for building a Timesheet Software. The software should allow users to log their working hours for selected projects on a weekly basis.



## 🎯Features 

### Authentication and User Management

#### 1. User Registration (`register_user`)

- **Objective:** Allows new users to register by providing necessary information.
- **Implementation:** Utilizes the `UserSerializer` for data validation and creates a new user upon successful validation. The user's password is securely set and saved.
- **Response:** Returns a success message and the registered user's data upon successful registration.

#### 2. User Login (`login_user`)

- **Objective:** Authenticates users based on provided credentials (username and password).
- **Implementation:** Uses the `LoginSerializer` for data validation and authenticates the user using Django's `authenticate` function. Generates JWT tokens (access and refresh) upon successful authentication.
- **Response:** Returns a success message with the user's username, along with the generated access and refresh tokens.

#### 3. User Logout (`logout_user`)

- **Objective:** Logs out users by blacklisting the provided refresh token.
- **Implementation:** Extracts the refresh token from the request headers and blacklists it using the RefreshToken class. Performs a logout operation.
- **Response:** Returns a success message upon successful logout, or an error message if the refresh token is missing or invalid.

-**Note:** All API endpoints are decorated with @api_view(['POST']) to ensure they accept only POST requests, which is a common practice for authentication-related operations. Proper HTTP status codes are used for different scenarios (success, bad request, unauthorized), providing clarity in the response.

  
### Authentication and User Management

#### 1.Create Project (`create_project`)

- **Objective:** Allows authenticated users to create a new project by providing project details.
- **Implementation:** Utilizes the `ProjectSerializer` for data validation and creates a new project upon successful validation.
- **Response:** Returns a success message and the created project's data upon successful creation. If validation fails, returns a bad request with validation errors.

#### 2. Update Project Details(`update_project_detail`)

- **Objective:** Allows authenticated users to update the details of an existing project identified by its primary key (`pk`).
- **Implementation:** Retrieves the existing project based on the provided primary key, validates the updated data using the `ProjectSerializer`, and saves the changes.
- **Response:**  Returns a success message and the updated project's data upon successful update. If validation fails or the project does not exist, returns a bad request with relevant errors.

#### 3. Get All Projects(`get_projects`)

- **Objective:** Allows authenticated users to retrieve a list of all projects.
- **Implementation:** Retrieves all projects from the database, serializes the data using `ProjectSerializer`, and returns the list of projects.
- **Response:**   Returns a success message and the data containing all projects upon successful retrieval.

#### 4. Get Project Detail(`get_project_detail`)

- **Objective:**  Allows authenticated users to retrieve details of a specific project identified by its primary key (`pk`).
- **Implementation:** Retrieves the project based on the provided primary key, serializes the data using `ProjectSerializer`, and returns the project details.
- **Response:**   Returns a success message and the data containing detailed information about the specified project upon successful retrieval. If the project does not exist, returns a bad request with relevant errors.

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

## Usage 📌



## Contributing 🤝

Feel free to contribute to enhance the functionality of Todo-Application. Follow the [contribution guidelines](CONTRIBUTING.md) for more details.

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/adityaShar24/varsity-pro-assignment/blob/main/LICENSE) file for details.

## Acknowledgments 🙏

Special thanks to the Django community and contributors for making this project possible.

Happy task managing! 😊






