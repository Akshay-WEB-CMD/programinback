from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}

    name = data.get('name', '')
    age = data.get('age', '')

    if not name or not age:
        return jsonify({
            "success": False,
            "message": "Name and age are required"
        }), 400

    return jsonify({
        "success": True,
        "message": "Registration successful",
        "data": {
            "name": name,
            "age": age
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
