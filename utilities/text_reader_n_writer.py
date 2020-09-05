import json
import os

from data.config import settings, projectPath

"""
CODE BY         ::  NIKHIL SHIVANKAR
DESCRIPTION     ::  TextReaderWriter CLASS TO READ & WRITE DICTIONARY 
                    INTO / FROM TEXT FILE FOR RUNTIME DATA CREATION AND PARAMETERIZATION
CREATION DATE   ::  27/12/2019
"""

"""
Class updated by: Namita on 27-Dec-2019
To append dictionaries.
Clear contents of dictionaries.
Get count of all the characters available in the file
"""


class TextReaderWriter:
    instance = None
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = TextReaderWriter()
        return cls.instance

    """
        in_dict parameter: is the dictionary to be written to the text file
    """
    def writing_dictionary(self, in_dict):
        print("Dictionary value::", in_dict)
        dictionary = {}
        path = os.path.join(projectPath, 'data\\')
        path = path + settings['file_to_store_counter']
        file = open(path, "a+")
        characters = read_write_txt.get_count_of_characters()
        if len(characters) > 0:
            dictionary = read_write_txt.reading_dictionary()
            dictionary.update(in_dict)
            read_write_txt.clear_contents_of_file()
            file.write(json.dumps(dictionary))
        else:
            file.write(json.dumps(in_dict))

    def get_count_of_characters(self):
        path = os.path.join(projectPath, 'data\\')
        path = path + settings['file_to_store_counter']
        file = open(path, "r")
        str_dict = file.read()
        return str_dict

    def clear_contents_of_file(self):
        path = os.path.join(projectPath, 'data\\')
        path = path + settings['file_to_store_counter']
        file = open(path, "r+")
        file.seek(0)
        file.truncate()
        file.flush()

    def reading_dictionary(self):
        path = os.path.join(projectPath, 'data/')
        path = path + settings['file_to_store_counter']
        file = open(path, "r")
        str_dict = file.read()
        res = read_write_txt.convert_string_to_dictionary(str_dict)
        file.close()
        print("read from file")
        return res

    def reading_environment_variables(self):
        path = os.path.join(projectPath, 'data\\environment_variables.txt')
        file = open(path, "r")
        str_dict = file.read( )
        res = read_write_txt.convert_string_to_dictionary(str_dict)
        file.close( )
        print("read from file")
        return res

    def convert_string_to_dictionary(self, str_dict):
        res_dict = json.loads(str_dict)
        return res_dict


read_write_txt = TextReaderWriter().get_instance()
