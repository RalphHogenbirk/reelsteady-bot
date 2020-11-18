import pyautogui
import time

class Screen:

    def __init__(self,config):
        self.config = config

    def click(self,image):
        pyautogui.click(self.config.image_folder+"/"+image+'.png',1)
        time.sleep(self.config.delay_after_click)

    def image_exists(self,image):
        try:
            rendered_location = self.get_location(image)
            if rendered_location[0]:
                return True
            else:
                return False
        except Exception as e:
            return False

    def wait_for(self,image,timeout=None):
        if timeout == None:
            timeout = 180
        count = 0
        while not self.image_exists(image):
            time.sleep(1)
            count += 1
            if count > timeout:
                print("timeout.. continuing")
                break

    def wait_for_disappear(self,image,timeout=None):
        if timeout == None:
            timeout = 180
        count = 0
        while self.image_exists(image):
            time.sleep(1)
            count += 1
            if count > timeout:
                print("timeout.. continuing")
                break

    def click_slider(self,image,value):
        location = self.get_location(image)
        center = pyautogui.center(location)
        x,y = center # x defaults to the second line, or 10
        start = round(x - 10 * 5.28) # move 10% to the left, to start at 0
        x = start + round(value * 5.28) # calculate new x
        pyautogui.click(x,y)
        time.sleep(self.config.delay_after_click)

    def get_location(self,image):
        img_src = self.config.image_folder+"/"+image+'.png'
        return pyautogui.locateOnScreen(img_src,1)
