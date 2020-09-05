import json
import os
from collections import OrderedDict
from datetime import date
import pandas

from data.config import projectPath

"""
    Created by Namita Maurkar
"""


def create_output_json_file():
    """Method to create the output json file"""
    data = [{'test': 'test_value'}]
    path_to_create_file = os.path.join(projectPath, "output_files//output_json_file.json")
    with open(path_to_create_file, "w") as write_file:
        json.dump(data, write_file)


def reading_the_json_file(json_path):
    """Method to read the json file"""
    with open(json_path) as f:
        json_file_content = json.load(f)
    return json_file_content


def read_index_of_availability_button():
    path_json = os.path.join(projectPath, "data//board_counters.json")
    with open(path_json) as f:
        json_file_content = json.load(f)
    return json_file_content


def clear_contents_of_file(folder_structure):
    """Method to clear the contents of json file"""
    path = os.path.join(projectPath, folder_structure)
    file = open(path, "r+")
    file.seek(0)
    file.truncate()
    file.flush()


def create_output_json_file():
    """Method to create the output json file"""
    data = [{'test': 'test_value'}]
    path_to_create_file = os.path.join(projectPath, "data//room_board_details.json")
    with open(path_to_create_file, "w") as write_file:
        json.dump(data, write_file)


def delete_json_file():
    path_for_output_json = os.path.join(projectPath, "data//")
    for filename in os.listdir(path=path_for_output_json):
        if str(filename) == "room_board_details.json":
            file_to_delete = filename
            os.remove(path_for_output_json + file_to_delete)


def write_board_value(values):
    folder_structure = "data//board_counters.json"
    json_content_list = []
    path = os.path.join(projectPath, folder_structure)
    file = open(path, "a+")
    board_count = values[0]
    json_content_list = reading_the_json_file(path)
    json_content_list['total_board_count'] = board_count
    json_content_list['current_counter_available_button'] = values[1]
    clear_contents_of_file(folder_structure)
    print("JSON CONTENTS::", json_content_list)
    file.write(json.dumps(json_content_list, indent=4, sort_keys=False))
    file.flush()
    file.close()


def write_room_details_to_json(value_to_append):
    """Method to write the list of details to the json file"""
    json_content_list = []
    path = os.path.join(projectPath, "data//room_board_details.json")
    file = open(path, "a+")
    json_content_list = reading_the_json_file(path)
    json_content_list.append(value_to_append)
    clear_contents_of_file("data//room_board_details.json")
    sort_order = ['test', 'Hotel_Name', 'Date', 'Passenger_count', 'Availability Index', 'Room_Name', 'Board_Name',
                  'Price_on_landing_page', 'Availability_Status']
    ordered_data = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                    for item in json_content_list]
    file.write(json.dumps(ordered_data, indent=4, sort_keys=False))
    file.flush()
    file.close()


def write_to_output_json(value_to_append):
    """Method to write the list of details to the json file"""
    print("Inside Json writting")
    json_content_list = []
    path = os.path.join(projectPath, "output_files//output_json_file.json")
    file = open(path, "a+")
    json_content_list = reading_the_json_file(path)
    json_content_list.append(value_to_append)
    clear_contents_of_file()
    sort_order = ['test', 'Search_id', 'Hotel_Name', 'Travel_Dates', 'Board_Name', 'Room_Name', 'Room_Availability_on_Landing_page',
                  'Price_on_landing_Page', 'Price_on_Checkout_Page', 'Price_Difference', 'Redirection_to_Checkout',
                  'Status']
    ordered_data = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                    for item in json_content_list]
    file.write(json.dumps(ordered_data, indent=4, sort_keys=False))
    file.flush()
    file.close()


def write_data_to_excel():
    """Method to write create and write the data from json file to excel"""
    today_date = date.today()
    output_excel_file_name = "Output_" + str(today_date)
    path_to_store_excel_file = os.path.join(projectPath, "output_files//")
    output_file_name = path_to_store_excel_file + output_excel_file_name + ".xlsx"
    path = os.path.join(projectPath, "output_files//output_json_file.json")
    json_content = reading_the_json_file(path)
    del json_content[0]
    pandas.DataFrame(json_content).to_excel(output_file_name)
    return output_file_name


def get_landing_page_data(index):
    """Method to read the json file for Landing page details"""
    json_path = os.path.join(projectPath, "data//room_board_details.json")
    with open(json_path) as f:
        json_file_content = json.load(f)
    json_file_content.remove(json_file_content[0])
    return json_file_content[index]


def update_json_data(dict_to_update):
    """Method to read the json file for Landing page details"""
    json_path = os.path.join(projectPath, "output_files//output_json_file.json")
    with open(json_path) as f:
        json_file_content = json.load(f)
    json_file_content.append(dict_to_update)
    clear_contents_of_file(json_path)
    file = open(json_path, "a+")
    sort_order = ['test', 'Hotel_Name', 'Start_Date', 'End_Date', 'Status_1_Night', 'End_Date_2', 'Status_2_Night', 'End_Date_5', 'Status_5_Night', 'Number_of_Travellers', 'Status']
    ordered_data = [OrderedDict(sorted(item.items(), key=lambda item: sort_order.index(item[0])))
                    for item in json_file_content]
    file.write(json.dumps(ordered_data, indent=4, sort_keys=False))


