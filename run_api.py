from flask import Flask , render_template, request, jsonify
from ml_models.model import Model
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classifier', methods = ['POST', 'GET'])
def classifier():
    if request.method == "POST": 
        age = request.form.get("age")
        cgpa = request.form.get("cgpa")
        data = {
            'age' : age,
            'cgpa' : cgpa
        }
        
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url = "http://127.0.0.1:3000/api"
        try: 
            response = requests.post(url=url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                return response_data
            else:
                response.raise_for_status()
        except Exception as e:
            return f"<h1>{e}</h1>"
    else:
        return render_template("classifier.html")


@app.route('/api', methods = ['POST'])
def api():
    data = request.get_json()
    data["hello"] = int(data["age"]) + 1 
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(port=3000, debug=True)
    
