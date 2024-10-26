```markdown
# Book Management API

This is a RESTful API built with Flask for managing a collection of books.
It allows users to register, log in, and perform CRUD operations (Create, Read, Update, Delete) on book entries.
User authentication is implemented for secure access to certain operations.

## Features

- **User Registration**: Allows new users to register with a unique username and password.
- **User Login**: Authenticates users and establishes a session.
- **CRUD Operations for Books**:
  - **Create**: Add new books to the database.
  - **Read**: Retrieve details of all books or a specific book.
  - **Update**: Update details of an existing book.
  - **Delete**: Soft-delete a book from the collection (using a `deleted_at` field).

## Technologies

- **Flask** - Python web framework
- **SQLAlchemy** - ORM for database interaction
- **Flask-Migrate** - Database migrations
- **Flask-Login** - User session management
- **MySQL** - Database

## Requirements

- **Python 3.6+**
- **MySQL Database**
- **pip** - Python package installer

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/Alltoft/book_api.git
   cd book_api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**

   - Create a MySQL database:
     ```sql
     CREATE DATABASE books;
     GRANT ALL PRIVILEGES ON `books`.* TO 'root'@'localhost';
     FLUSH PRIVILEGES;
     ```
   - Update your MySQL credentials in `app/__init__.py`:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:your_password@localhost/books'
     ```

4. **Apply Migrations:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the Application:**
   ```bash
   python run.py
   ```

   The API should now be accessible at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint             | Description              | Authentication Required |
|--------|-----------------------|--------------------------|-------------------------|
| POST   | `/register`           | Register a new user      | No                      |
| POST   | `/login`              | Log in an existing user  | No                      |
| POST   | `/logout`             | Log out the current user | Yes                     |
| GET    | `/books`              | Get all books            | No                      |
| POST   | `/books/add`          | Add a new book           | Yes                     |
| PUT    | `/books/update/<id>`  | Update an existing book  | Yes                     |
| DELETE | `/books/delete/<id>`  | Soft-delete a book       | Yes                     |

## Example Requests

- **Register User**
  ```http
  POST /register
  Content-Type: application/json
  {
    "username": "exampleuser",
    "password": "examplepass"
  }
  ```

- **Add Book**
  ```http
  POST /books/add
  Content-Type: application/json
  Authorization: Bearer <token>
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  }
  ```

- **Get All Books**
  ```http
  GET /books
  ```

## Testing the API

You can test the API using [Postman](https://www.postman.com/) or similar tools. Importantly, remember to:
- Register a new user and log in to get an authorization token.
- Include the token in headers for all protected routes (`POST`, `PUT`, `DELETE`).

## License

This project is licensed under the MIT License.
```

This `README.md` covers project setup, usage, endpoints, and example requests to give clients a full overview. Adjust as needed if you make further changes to the API!