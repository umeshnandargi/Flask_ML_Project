import yaml
import os

class Config():
    def get_config(self, config_name):
        file_path = os.path.join(os.path.dirname(__file__), config_name)
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                config = yaml.safe_load(file)
        else:
            raise FileNotFoundError(file_path)
        
        return config