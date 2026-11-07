from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Cloud Computing", "author": "Rajkumar Buyya"}
]

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    data["id"] = len(books) + 1
    books.append(data)
    return jsonify(data), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    for b in books:
        if b["id"] == book_id:
            b.update(request.get_json())
            return jsonify(b)
    return jsonify({"error": "Not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(debug=True)