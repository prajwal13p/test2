from flask import Flask, render_template, request, redirect, url_for, jsonify
from urllib.parse import quote_plus
from pymongo import MongoClient
import requests

username = "deltatraderskp"
password = "787898@pP"

# Encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Upd
MONGO_URI = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.osvuu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['mydb']  # Replace <dbname> with your database name
collection = db['mycollection']  # Replace <collection_name> with your collection name


app = Flask(__name__)

correct_answers = ["1", "2"]



def Mathrix_send_image(image_path, caption=""):
    bot_token = "7361947274:AAEVVDIudONO--PLc6c09K9O3ygkq2UW6go" 
    chat_id = "-4751986525"  

    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    with open(image_path, "rb") as image_file:
        data = {
            "chat_id": chat_id,
            "caption": caption
        }
        files = {
            "photo": image_file
        }
        response = requests.post(url, data=data, files=files)

    # Check the response
    if response.status_code == 200:
        print(f"Image {caption} sent successfully!")
    else:
        print(f"Failed to send image. Error: {response.status_code}")
        print(response.text)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Save to MongoDB
        user = {"name": name, "email": email, "password": password}
        collection.insert_one(user)

        return redirect(url_for('home'))  # Redirect to home after successful registration
    return render_template('register.html')


@app.route('/home')
def Home():
    return render_template("index.html")

@app.route('/ed')
def ed():
    return "reched edit"

@app.route('/act')
def act():
    return "reched action"

@app.route('/con')
def con():
    return "reched contact"

@app.route('/mathhunt')
def mathhunt():
    return render_template('mathhunt.html')

@app.route('/SetOps')
def door():
    return render_template('setops.html')

@app.route('/graph')
def grapg():
    return render_template('graph.html')
@app.route('/escape_room')
def ecroom():
    return render_template('escape_room.html')

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.get_json()
    user_answer = data.get("answer", "").replace(" ", "").lower()

    if user_answer in [ans.replace(" ", "").lower() for ans in correct_answers]:
        Mathrix_send_image("/home/ubuntu/Event-Mathix/Event-Mathix/Project MATHRIX/static/images/IMG20250111145756.jpg",caption=" ")
        Mathrix_send_image("/home/ubuntu/Event-Mathix/Event-Mathix/Project MATHRIX/static/images/IMG20250111151051.jpg",caption=" ")
        Mathrix_send_image("/home/ubuntu/Event-Mathix/Event-Mathix/Project MATHRIX/static/images/IMG20250111151545.jpg",caption=" ")
        return jsonify({"correct": True})

    else:
        return jsonify({"correct": False})
import ssl
print(ssl.OPENSSL_VERSION)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
