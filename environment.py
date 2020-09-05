import os
from data.config import projectPath
from lib.application import app
from lib.excel_reading import get_test_data, get_data_dict
from utilities.json_file_operations import update_json_data
from utilities.text_reader_n_writer import read_write_txt


def before_all(context):
    print("Starting Framework")
    # context.index_dict = read_write_txt.reading_dictionary()
    # context.test_data = context.index_dict['test_data_file_name']
    # context.sheet_name = context.index_dict['test_data_sheet']
    # context.index_current_row = context.index_dict['current_row_counter']
    context.test_data = "test_data/Generic_Test_Data_Hotel_List.xlsx"
    context.sheet_name = "Trivago_ESP"
    context.index_current_row = 2
    context.search_id = app.load_website()
    # # context.index_dict = read_write_txt.reading_dictionary()
    # # context.run_id = context.index_dict['Run_id']
    # # context.index_current_row = context.index_dict['current_row_counter']
    # # environment = context.index_dict['Environment']
    # # environment = "Spain"
    # # context.screen_shot_name_for_page_loading = obj_trivago.change_browser_region(environment, context.index_current_row)
    # context.step_status_dict = {"Status_1_Night": "FAIL", "Status_2_Night": "FAIL", "Status_5_Night": "FAIL"}


def before_feature(context, feature):
    """
            This function is for executing block of code before executing each feature file
    """
    print("Starting feature", feature)


def before_scenario(context, scenario):
    """
            This function is for executing block of code before executing each scenario in all feature files
    """
    print()


def after_step(context, step):
    """
            This function is for executing block of code after executing each scenario step in all feature files
    """
    status = str(step.status)
    print("Status>>>>>>>>>>", status)
    # ob = Screenshot_Clipping.Screenshot()
    if status == 'Status.failed':
        print("Inside failed")
        hotel_name = get_test_data(context.sheet_name, "Hotel_Name", context.index_current_row)
        screen_shot_name = os.path.join(projectPath, 'screenshots/') + str(hotel_name) + ".png"
        app.driver.save_screenshot(screen_shot_name)

    status = str(step.status)
    print("Status change_browser_region >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", status)
    result_value = str(step.status).split(".")
    step_name = str(step.name)
    print("step_name is :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ", step_name)
    #
    # if step_name == "Check if TUI Add is present for 2 Nights":
    #     context.step_status_dict.update({"Status_2_Night": result_value[1]})
    #     print("Check if TUI Add is present for 2 Nights :::::::::: COMPLETED")
    # elif step_name == "Check if TUI Add is present for 5 Nights":
    #     context.step_status_dict.update({"Status_5_Night": result_value[1]})
    #     print("Check if TUI Add is present for 5 Nights :::::: COMPLETED")
    # elif step_name == "The dates and the Passenger Count are the Same on the IBE Page":
    #     context.step_status_dict.update({"Status_1_Night": result_value[1]})
    #     print("The dates and the Passenger Count are the Same on the IBE Page :::::: COMPLETED")


def after_scenario(context, scenario):
    """
            This function is for executing block of code after executing each scenario in all feature files
    """


def after_feature(context, feature):
    """
            This function is for executing block of code after executing each feature file
    """
    result_value = str(feature.status).split(".")
    print("Context.sheet name >>>>>>>>>>>", context.sheet_name)
    # output_dict = get_data_dict(context.sheet_name, context.index_current_row, result_value[1], context.step_status_dict)
    # print("Output Dict::", output_dict)
    # update_json_data(output_dict)
    # print("Current Row Counter::", context.index_current_row)
    # dict_to_write = {"current_row_counter": context.index_current_row + 1}
    # read_write_txt.writing_dictionary(dict_to_write)


def after_all(context):
    """
            This function is for executing block of code after executing all feature files for cleanup purpose
    """
    app.close_entire_browser()
    print("Ending Connections")

