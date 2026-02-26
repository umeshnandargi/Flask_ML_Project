from flask import Flask , render_template, request, jsonify , flash
from ml_models.model import Model
from config.configuraton import Config
from utils.helper_functions import (
    load_saved_model, 
    get_prediction, 
    url_builder )
import requests
import json
import sys

app = Flask(__name__)
cfg = Config()
mappings = cfg.get_config(config_name='mappings.yaml')
config = cfg.get_config(config_name='config.yaml')
DISCLAIMER_MESSAGE = config['disclaimer_message']
depts   : dict  = mappings['departments']
genders : dict = mappings['genders']

model = Model(9,12,12,24,16,2)
model = load_saved_model(model=model, model_name=config['model_name'])

app.secret_key = config['secret_key']
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classifier', methods = ['POST', 'GET'])
def classifier():
    flash_message = False
    if request.method == "POST": 
        age                = float(request.form.get("age"))
        gender             = float(genders[request.form.get("gender")])
        department         = float(depts[request.form.get("department")])
        cgpa               = float(request.form.get("cgpa"))
        sleep_duration     = float(request.form.get("sleep_duration"))
        study_hours        = float(request.form.get("study_hours"))
        social_media_hours = float(request.form.get("social_media_hours"))
        physical_activity  = float(request.form.get("physical_activity"))
        stress_level       = float(request.form.get("stress_level"))

        data = {
            'age' : age,
            'gender' : gender,
            'department' : department,
            'department' : department,
            'cgpa' : cgpa,
            'sleep_duration' : sleep_duration,
            'study_hours' : study_hours,
            'social_media_hours' : social_media_hours,
            'physical_activity' : physical_activity,
            'stress_level' : stress_level,
        }
        
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        BASE_URL  = config['base_url']
        PORT      = config['port']
        END_POINT = config['api_endpoint']
        url = url_builder(BASE_URL, PORT, END_POINT)
        try: 
            response = requests.post(url=url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                if response_data["is_depressed"] is True: 
                    flash(f"You may be Depressed...idk {DISCLAIMER_MESSAGE}")
                    flash_message = True
                else :
                    flash(f"Looks like you are NOT Depressed {DISCLAIMER_MESSAGE}")
                    flash_message = True
                return render_template("classifier.html" , flash_message = flash_message)
            else:
                response.raise_for_status()
        except Exception as e:
            return f"<h1>{e}</h1>"
    else:
        return render_template("classifier.html")

@app.route('/api', methods = ['POST'])
def api():
    # TODO : Add authentication
    data = request.get_json()
    prediction = get_prediction(model=model, inputs=data) 
    response = {}
    response["is_depressed"] = bool(prediction)
    return jsonify(response), 200

if __name__ == "__main__":
    if config['debug'] :
        print("debug mode is on!!! Turn it off or comment this section")
        sys.exit()
    app.run(host="0.0.0.0", port=config['port'],  debug=config['debug'])
    
