from behave import given, when, then
from lib.excel_reading import get_test_data
from page_objects.trivago_metas import obj_trivago


"""
##############################################################################################################
Trivago ES
##############################################################################################################
"""


@given(u'The home page for Trivago is launched')
def step_impl(context):
    display_status = obj_trivago.check_if_trivago_home_page_is_launched()
    assert display_status is True
    print('STEP: Given The home page for Trivago is launched')


@when(u'User enters the search criteria')
def step_impl(context):
    hotel_name = get_test_data(context.sheet_name, "Hotel_Name", context.index_current_row)
    print("Hotel Name")
    check_in_date = get_test_data(context.sheet_name, "Start_Date", context.index_current_row)
    check_out_date = get_test_data(context.sheet_name, "End_Date", context.index_current_row)
    passenger_count = get_test_data(context.sheet_name, "Number_of_Passenger", context.index_current_row)
    age = get_test_data(context.sheet_name, "Age", context.index_current_row)
    obj_trivago.set_search_criteria(hotel_name, check_in_date, check_out_date, passenger_count, age)


@then(u'Checks if the Hotel is displayed on Search Result Page')
def step_impl(context):
    hotel_name = get_test_data(context.sheet_name, "Hotel_Name", context.index_current_row)
    context.index_of_hotel = obj_trivago.verify_the_search_result(hotel_name)
    print("Hotel index>>>>>>>>>>>>", context.index_of_hotel)
    assert context.index_of_hotel is not None