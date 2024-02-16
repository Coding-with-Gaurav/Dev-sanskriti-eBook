from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db = client['book_catalog']
books_collection = db['books']

@app.route('/')
def index():
    books = list(books_collection.find())
    return render_template('index.html', books=books)

@app.route('/api/books')
def get_books():
    books = list(books_collection.find())
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
