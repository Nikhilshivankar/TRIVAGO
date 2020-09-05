import os
import json

settings = None
projectPath = None
environment = None


def load_settings():
    """
            This function is for loading environment settings related to framework

    """
    global settings, projectPath
    projectPath = os.path.dirname(os.path.dirname(os.path.expanduser(__file__)))
    with open(os.path.join(os.path.dirname(os.path.expanduser(__file__)), 'settings.json')) as f:
        settings = json.load(f)


load_settings()

