# from pickletools import read_stringnl_noescape_pair
from pydoc import render_doc
from flask import render_template, request, redirect
from app import app
from models.books import Book
from models.books_list import books as bookslist
from models.books_list import add_new_book, remove_book


@app.route('/')
def index():
    return render_template('index.html', title='Home', books = bookslist)

@app.route('/books')
def books_list():
    return render_template('index,html', title = "books", books = bookslist)

@app.route('/books/<index>')
def show(index):
    book_to_show = bookslist[int(index)]
    return render_template('book.html', book = book_to_show, books=bookslist)

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
    return render_template('index.html', title="home", books=bookslist)

@app.route('/books/delete/<int:index>')
def remove(index):
    remove_book(bookslist[index])
    return redirect('/')