from app import app, db
from flask import request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Book
from datetime import datetime

# The routes are the endpoints that the client can access to interact with the application.

# The first route is the register route. This route is used to create a new user in the database.
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify({'message': 'Username already exists'}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

# The login route is used to authenticate a user. If the user is successfully authenticated, the user is logged in.
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401
    login_user(user)
    user.last_login = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Login successful'})

# The logout route is used to log out a user.
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

# The get_books route is used to get all the books in the database.
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.filter_by(deleted_at = None).all()
    return jsonify([book.to_dict() for book in books])

# The get_book route is used to get a specific book in the database.
@app.route('/books/add', methods=['POST'])
@login_required
def create_book():
    data = request.get_json()
    if not data.get('title') or not data.get('author'):
        return jsonify({'message': 'Missing required data'}), 400
    title = data.get('title')
    author = data.get('author')
    book = Book(title=title, author=author)
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'})

# The update_book route is used to update a specific book in the database.
@app.route('/books/update/<book_id>', methods=['PUT'])
@login_required
def update_book(book_id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    book = Book.query.get(book_id)
    book.title = title
    book.author = author
    book.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

# The delete_book route is used to delete a specific book in the database.
@app.route('/books/delete/<book_id>', methods=['DELETE'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    book.deleted_at = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})
