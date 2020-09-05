import os
from data.config import projectPath


class Folder:
    instance = None

    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Folder()
        return cls.instance

    def __init__(self):
        print()

    def create_directory(self, directory_name):
        path = os.path.join(projectPath, directory_name)
        if folder.check_if_directory_exists(path) is False:
            os.mkdir(path)
            print("Directory '% s' created" % directory_name)
        else:
            print(directory_name, " : Already Exists")

    def check_if_directory_exists(self, directory_path):
        return os.path.isdir(directory_path)


folder = Folder().get_instance()
