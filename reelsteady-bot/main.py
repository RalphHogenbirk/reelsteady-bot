from config import Config
from instance import Instance
import time
import os
import traceback

class ReelSteadyGoRunner:
    delay_after_click = 0.7
    image_folder = 'images'
    config_file = '../config.json'

    # files
    unstabilised = []
    stabilised = []
    started_with = 0
    running = False

    #instances
    instances = []
    config = None

    def __init__(self,debug_level):
        self.debug_level = debug_level
        self.config = Config(self.config_file)
        self.read_videos()


    # main application loop
    def start(self):
        self.running = True

        if self.started_with > 0:
            self.display("=========")
            self.display("Program starting! Don't touch your mouse and keyboard and let me do my thing :)")
            self.display("To stop, simply Ctrl-C inside this window")
            self.display("=========")

        while (not self.is_done() or len(self.instances) > 0) and self.running:
            running_count = self.get_running_count()

            if self.is_done():
                self.display("We're all done after rendering "+str(self.started_with)+" files! Closing down while last files render")
                break

            if self.max_running():
                self.check_renders_for_completion()

            if self.max_running():
                self.display("That's enough for now, waiting for completed renders...")
                time.sleep(30)

            else:
                new_file = self.unstabilised.pop(0)
                self.display("Starting new window for "+new_file)
                instance = Instance(new_file, self.config)
                self.instances.append(instance)
                instance.start()
                try:
                    instance.configure()
                    instance.render()
                except Exception as e:
                    self.display("An error occurred during this file! Trying this file again later")
                    if self.debug_level > 0:
                        self.display(e,1)
                        traceback.print_exc()
                    instance.close()
                    self.instances.pop()
                    self.unstabilised.append(new_file)

        self.running = False

    def stop():
        self.running = False # stops the loop after current iteration
        for instance in self.instances:
            if not instance.is_rendering():
                print("closing "+ instance.file_name)
                instance.close()
                instances.remove(instance)


    # checks all instances for completion
    def check_renders_for_completion(self):
        done = []
        for i,instance in enumerate(self.instances[:]):
            if instance.is_done():
                instance.close()
                self.instances.remove(instance)
                self.stabilised.append(instance.file_name)

    # reads configured folder and analyses videos
    def read_videos(self):
        # analise files to stabilise
        all_files = os.listdir(self.config.project_dir)
        smoothed_files = [x for x in all_files if '_smoothed' in x]
        self.unstabilised = []
        self.stabilised = []
        for file in all_files:
            if '.MP4' in file and '_smoothed' not in file:
                if file.replace('.MP4','_smoothed.mp4') in smoothed_files:
                    self.stabilised.append(file)
                else:
                    self.unstabilised.append(file)

        self.started_with = self.get_unstabilised()
        self.display("Found " + str(self.started_with) + " files to stabilise (" + str(self.get_stabilised()) + " already done)")
        self.display("File list: " + ",".join(self.unstabilised))


    def get_unstabilised(self):
        return len(self.unstabilised)

    def get_stabilised(self):
        return len(self.stabilised)

    def is_done(self):
        return self.get_unstabilised() == 0

    def get_running_count(self):
        return len(self.instances)

    def max_running(self):
        return self.get_running_count() == self.config.max_instances

    def display(self,text,level=0):
        if level <= self.debug_level:
            print(text)
