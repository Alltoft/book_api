from app import db
from flask_login import UserMixin
import bcrypt
from datetime import datetime
from uuid import uuid4
# import sqlalchemy as sa

class User(UserMixin, db.Model):
    id = db.Column(db.String(64), default=lambda: str(uuid4()), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    deleted_at = db.Column(db.DateTime, index=True)
    last_login = db.Column(db.DateTime, index=True)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at,
            'last_login': self.last_login
        }

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Book(db.Model):
    book_id = db.Column(db.String(64), default=lambda: str(uuid4()), primary_key=True)
    title = db.Column(db.String(64), index=True)
    author = db.Column(db.String(64), index=True)
    published_year = db.Column(db.Integer, default=lambda: datetime.now().year, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    deleted_at = db.Column(db.DateTime, index=True)

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at
        }

    def __repr__(self):
        return '<Book {}>'.format(self.title)
    
# class Borrow(db.Model):
#     borrow_id = db.Column(db.String(64), default=lambda: str(uuid4()), primary_key=True)
#     user_id = db.Column(db.String(64), db.ForeignKey('user.user_id'), index=True)
#     book_id = db.Column(db.String(64), db.ForeignKey('book.book_id'), index=True)
#     borrowed_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     returned_at = db.Column(db.DateTime, index=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     deleted_at = db.Column(db.DateTime, index=True)

#     def to_dict(self):
#         return {
#             'borrow_id': self.borrow_id,
#             'user_id': self.user_id,
#             'book_id': self.book_id,
#             'borrowed_at': self.borrowed_at,
#             'returned_at': self.returned_at,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at,
#             'deleted_at': self.deleted_at
#         }

#     def __repr__(self):
#         return '<Borrow {}>'.format(self.borrow_id)
    
# class Review(db.Model):
#     review_id = db.Column(db.String(64), default=lambda: str(uuid4()), primary_key=True)
#     user_id = db.Column(db.String(64), db.ForeignKey('user.user_id'), index=True)
#     book_id = db.Column(db.String(64), db.ForeignKey('book.book_id'), index=True)
#     rating = db.Column(db.Integer, index=True)
#     review = db.Column(db.String(256), index=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
#     deleted_at = db.Column(db.DateTime, index=True)

#     def to_dict(self):
#         return {
#             'review_id': self.review_id,
#             'user_id': self.user_id,
#             'book_id': self.book_id,
#             'rating': self.rating,
#             'review': self.review,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at,
#             'deleted_at': self.deleted_at
#         }

#     def __repr__(self):
#         return '<Review {}>'.format(self.review_id)