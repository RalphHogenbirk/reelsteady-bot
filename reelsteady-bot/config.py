import json, os

class Config:

    image_folder = 'images'
    delay_after_keypress = 0.3
    delay_after_write = 0.3
    delay_after_click = 0.5

    def __init__(self,file_name):
        # read config file
        with open(file_name) as config_file:
            data = json.load(config_file)

        # global config
        self.base = data['base_folder']
        self.max_instances =  data['max_instances']
        self.application_location =  data['application_location']

        # project based config
        self.project =  data['project']['folder']
        self.smoothness =  data['project']['smoothness']
        self.cropping_speed =  data['project']['cropping_speed']
        self.flip_gyro =  data['project']['flip_gyro']
        self.horizon_lock =  data['project']['horizon_lock']
        self.project_dir = self.base + self.project
