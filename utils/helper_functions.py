from config.configuraton import Config
from ml_models.model import Model
import torch
import os

def load_saved_model(model : Model, model_name:str = "depression_model") -> None:
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "ml_models" ,
                                "saved_model_files", model_name)
    
    if os.path.exists(model_path): 
        model.load_state_dict(torch.load(model_path))
        print(model.eval())
        return model
    else : 
        raise FileNotFoundError(model_path)

def get_prediction(model : Model, inputs : dict):
    input = [value for value in inputs.values()]
    input = torch.tensor(input)
    print(model.eval())
    with torch.no_grad():
      prediction = model.forward(input)

    return prediction.argmax().item()

def url_builder(base_url, port, endpoint):
    return f"{base_url}:{port}/{endpoint}"