from pywinauto.application import Application
from screen import Screen
import pyautogui
import time

class Instance:

    def __init__(self,file_name,config):
        self.file_name = file_name
        self.config = config
        self.app = Application()
        self.rendering = False

    def start(self):
        self.app.start(self.config.application_location)
        self.controls = self.app.ReelSteadyGO
        self.screen = Screen(self.config)

    def click(self,image):
        self.screen.click(image)

    def wait_for(self,image,timeout=None):
        self.screen.wait_for(image,timeout)

    def wait_for_click(self,image,timeout=None):
        self.wait_for(image,timeout)
        self.click(image)

    def wait_for_disappear(self,image,timeout=None):
        self.screen.wait_for_disappear(image,timeout)

    def click_slider(self,image,value):
        self.screen.click_slider(image,value)

    def keypress(self,key,repeat=1):
        for _ in range(repeat):
            pyautogui.press('enter')
            time.sleep(self.config.delay_after_keypress)

    def write(self,text):
        pyautogui.write(text)
        time.sleep(self.config.delay_after_write)

    def configure(self):

        self.controls.wait('visible')

        print(" -- Loading file...")
        self.wait_for_click('loadvideo')

        self.wait_for_click('locate',10)

        self.write(self.config.project_dir)
        self.keypress('enter')
        self.keypress('tab',5)
        self.write(self.file_name)
        self.keypress('enter')
        self.wait_for_disappear('locate') # wait for the select box to disappear

        print(" -- Running the numbers")
        self.wait_for_disappear('running_the_numbers')

        print(" -- Configuring")
        self.click('config')

        double_save = False
        if self.config.flip_gyro:
            self.click('flip')
            double_save = True

        if self.config.horizon_lock:
            self.click('lock')
            double_save = True

        if double_save:
            print(" -- Running the numbers again")
            self.click('okay')
            time.sleep(1)
            self.wait_for_disappear('running_the_numbers')
            if self.config.horizon_lock:
                print("-- Gyro sync...")
                self.wait_for('config')

            print(" -- Settings moothness and cropping speed")
            self.click('config')


        if self.config.smoothness != self.config.cropping_speed:
            self.click('linksmoothness')

        if self.config.smoothness != 50:
            self.click_slider('low',self.config.smoothness)

        if self.config.cropping_speed != 50:
            self.click_slider('fast',self.config.cropping_speed)

        self.click('okay')
        print(" -- Recomputing...")
        self.wait_for_disappear('recomputing')

    def render(self):
        print(" -- Starting render!")
        self.click('save')
        self.rendering = True

    def is_done(self):
        self.controls.set_focus()
        time.sleep(1) # wait for focus, just to be sure
        return self.screen.image_exists('rendered2')

    def is_rendering(self):
        return self.rendering

    def close(self):
        self.controls.close()
        time.sleep(0.5) # wait for instance to close, just to be sure
