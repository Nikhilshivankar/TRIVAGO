import json
import os

from data.config import projectPath


def update_settings(dictionary_value):
    print("Path>>>>>>>>>>>", projectPath)
    path = os.path.join(projectPath, "data\\environment_variables.txt")
    print("Path>>>>>>>>>>>", path)
    file = open(path, "a+")
    dictionary = reading_dictionary_from_json()
    dictionary.update(dictionary_value)
    clear_contents_of_file()
    file.write(json.dumps(dictionary, indent=4, sort_keys=True))
    file.flush()
    file.close()
    print("written to file")


def reading_dictionary_from_json():
    path = os.path.join(projectPath, "data\\environment_variables.txt")
    file = open(path, "r")
    str_dict = file.read( )
    res = convert_string_to_dictionary(str_dict)
    file.close( )
    return res


def convert_string_to_dictionary(str_dict):
    res_dict = json.loads(str_dict)
    return res_dict


def clear_contents_of_file():
    path = os.path.join(projectPath, "data\\environment_variables.txt")
    file = open(path, "r+")
    file.seek(0)
    file.truncate()
    file.flush()
