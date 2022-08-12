from pickletools import read_stringnl_noescape_pair
from pydoc import render_doc
from urllib import request
from flask import render_template, request
from app import app
from models.books import Book
from models.books_list import *


@app.route('/')
def index():
    return render_template('index.html', title='Home', books = books)

@app.route('/books')
def books_list():
    return render_template('index,html', title = "books", books = books)

@app.route('/books/<index>')
def show(index):
    book_to_show = books[int(index)]
    return render_template('book.html', book = book_to_show)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/', methods=['POST'])
def create():
    book_title = request.form['book_title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(book_title, author, genre)
    add_new_book(new_book)
    return render_template('index.html', title="home", books=books)

@app.route('/', method=["POST"])
def remove(index):
    book_to_remove = books[int(index)]
    remove_book(book_to_remove)
    return redirect('index.html', title="home", books=books)