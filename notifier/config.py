
import yaml


class Config:
    def __init__(self):
        self.config_file_name = 'config.yaml'
        self.config = self.__read_config(self.config_file_name)

    def get(self, key):
        return self.config.get(key)

    def get_config(self):
        return self.config
    
    def set(self, key, value):
        self.config[key] = value
    
    def __read_config(self, config_file):
        with open(config_file, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return config
    
    def __write_config(self, config_file):
        with open(self.config_file_name, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False)

    def restore_config(self):
        self.config = self.__read_config(self.config_file_name)

config_file = Config()
