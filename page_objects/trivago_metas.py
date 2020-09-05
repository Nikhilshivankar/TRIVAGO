import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import projectPath
from lib.application import app
from object_repository import ele_repo
from page_objects.page_mgr import Page


class TrivagoMetas(Page):
    instance = None

    # get the instance of the class
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = TrivagoMetas( )
        return cls.instance

    # initialize the class
    def __init__(self):
        self.driver = app.get_driver( )

    def check_if_trivago_home_page_is_launched(self):
        """Method to check if the home page for Trivago is launched"""
        title = self.driver.title
        if str(title).startswith("trivago"):
            return True

    def set_search_criteria(self, hotel_name, check_in_date, check_out_date, passenger_count, age):
        """Method to set the search criteria in the search box on the Trivago home page"""
        hotel_search_box = self.driver.find_element_by_xpath(ele_repo.elements['xp_hotel_name_search_bar_trivago'])
        obj_trivago.apply_style(hotel_search_box)
        hotel_search_box.send_keys(hotel_name)
        suggestion_list = self.driver.find_elements_by_class_name(ele_repo.elements['cls_hotel_name_suggestion'])
        suggestion_subtitle = self.driver.find_elements_by_class_name("ssg-subtitle")
        for i in suggestion_list:
            ind = suggestion_list.index(i)
            if str(i.text).upper().__contains__(str(hotel_name).upper()) or str(i.text).upper().startswith(
                    str(hotel_name).upper()) or str(hotel_name).upper().__contains__(str(i.text)):
                obj_trivago.apply_style(i)
                if ind > (len(suggestion_subtitle)-1):
                    if str(i.text).startswith("Buscar"):
                        i.click( )
                        break
                else:
                    if str(suggestion_subtitle[ind].text).startswith("Hotel"):
                        obj_trivago.apply_style(i)
                        i.click()
                        break
        start_date = self.driver.find_element_by_xpath(ele_repo.elements['xp_checkin_date_tivago'])
        obj_trivago.apply_style(start_date)
        obj_trivago.check_overlay_displayed_and_click(start_date)
        obj_trivago.select_dates(check_in_date)
        obj_trivago.check_overlay_displayed_and_click(
            self.driver.find_element_by_xpath(ele_repo.elements['xp_checkout_date']))
        obj_trivago.select_dates(check_out_date)
        obj_trivago.select_passenger_count(passenger_count, age)
        search_button = self.driver.find_element_by_xpath(ele_repo.elements['xp_search_button_tivago'])
        search_button.click( )
        time.sleep(3)

    def select_passenger_count(self, passenger_count, age):
        print("Passenger Count 3:::>>>>>>", passenger_count)
        passenger_box = self.driver.find_element_by_xpath(ele_repo.elements['xp_passenger_trivago'])
        obj_trivago.apply_style(passenger_box)
        obj_trivago.check_overlay_displayed_and_click(passenger_box)
        # self.driver.find_element_by_xpath("//span[contains(text(),'Familiar')]").click( )
        # select = Select(self.driver.find_element_by_xpath(ele_repo.elements['xp_adult_drp_down_tri']))
        # select_child = Select(self.driver.find_element_by_xpath(ele_repo.elements['xp_child_drp_down_tri']))
        # passenger_count = str(passenger_count).split(",")
        # if len(passenger_count) == 1:
        #     adult_count = str(passenger_count[0])[:1]
        #     select.select_by_visible_text(adult_count)
        # else:
        #     adult_count = str(passenger_count[0])[:1]
        #     select.select_by_visible_text(adult_count)
        #     child_count = str(passenger_count[1].strip( ))[:1]
        #     select_child.select_by_visible_text(child_count)
        #     age = str(age).split(",")
        #     child_age = self.driver.find_elements_by_xpath("//select[contains(@class,'df-select js-select-child-age')]")
        #     if str(len(child_age)) == str(child_count):
        #         for i in child_age:
        #             ind = child_age.index(i)
        #             child_age_drp_dwn = Select(i)
        #             child_age_drp_dwn.select_by_visible_text(age[ind])
        adult_input = "//input[@id='adults-input']"
        children_input = "//input[@id='children-input']"
        room_input = "//input[@id='rooms-input']"
        children_ages = "//ul[@class='ages-input__list']/li/select"

        adult = self.driver.find_element_by_xpath(adult_input)
        children = self.driver.find_element_by_xpath(children_input)
        room = self.driver.find_element_by_xpath(room_input)
        print(passenger_count)

        passenger_count = str(passenger_count).split(",")
        if len(passenger_count) == 1:
            adult_count = str(passenger_count[0])[:1]
            obj_trivago.apply_style(adult)
            ActionChains(self.driver).move_to_element(adult).send_keys(Keys.BACKSPACE).pause(1).send_keys(adult_count).perform()
        else:
            adult_count = str(passenger_count[0])[:1]
            obj_trivago.apply_style(adult)
            adult.send_keys(Keys.BACKSPACE)
            ActionChains(self.driver).move_to_element(adult).pause(1).send_keys(adult_count).perform()
            child_count = str(passenger_count[1].strip())[:1]
            if str(child_count) != "0":
                obj_trivago.apply_style(children)
                children.send_keys(Keys.BACKSPACE)
                ActionChains(self.driver).move_to_element(children).send_keys(Keys.BACKSPACE).pause(1)\
                    .send_keys(child_count).pause(1).move_to_element(room).pause(1).perform()
                age = str(age).split(",")
                children_age_drp = self.driver.find_elements_by_xpath(children_ages)

                if str(len(children_age_drp)) == str(child_count):
                    for i in children_age_drp:
                        ind = children_age_drp.index(i)
                        obj_trivago.apply_style(i)
                        child_age_drp_dwn = Select(i)
                        child_age_drp_dwn.select_by_visible_text(age[ind])
        # confirm_button = self.driver.find_element_by_xpath(ele_repo.elements['xp_age_confirmation_btn_tri'])
        confirm_button = self.driver.find_element_by_xpath("//button[contains(@class, 'btn--apply-config')]")
        confirm_button.click()

    def select_dates(self, check_in_date):
        print("Inside date selection")
        check_in_date = str(check_in_date).split("-")
        c_in_day = check_in_date[0]
        c_in_month = check_in_date[1]
        month_header = self.driver.find_element_by_xpath(ele_repo.elements['xp_month_header_trivago'])
        curr_month = str(month_header.text).split(" ")
        next_arrow = self.driver.find_element_by_class_name(ele_repo.elements['cls_next_button_tri'])
        while str(curr_month[0]).upper( ) != str(c_in_month).upper( ):
            next_arrow.click( )
            curr_month = str(month_header.text).split(" ")
        days = self.driver.find_elements_by_class_name(ele_repo.elements['cls_trivago_dates'])
        for day in days:
            if str(day.text) == str(c_in_day):
                day.click( )
                break

    def verify_the_search_result(self, hotel_name):
        search_results = self.driver.find_elements_by_xpath(ele_repo.elements['xp_hotel_list_for_search_tivago'])
        hotel_names_in_search_result = self.driver.find_elements_by_xpath(ele_repo.elements['xp_hotel_name_trivago'])
        for hotels in search_results:
            ind = search_results.index(hotels)
            print("******>>>>>>>>>", hotel_names_in_search_result[ind].text)
            if str(hotel_names_in_search_result[ind].text).upper( ).startswith(str(hotel_name).upper( )):
                return ind
                break
            else:
                expected_hotel = str(hotel_name).split(" ")
                actual_hotel_name = str(hotel_names_in_search_result[ind].text).split(" ")
                if any(item in expected_hotel for item in actual_hotel_name) is True:
                    return ind
                    break

    def check_for_tui_offer(self, index):
        flag = False
        cheap_deals_button = self.driver.find_elements_by_xpath(ele_repo.elements['xp_cheap_deal_btn_tivago'])
        cheap_deals_button[index].click( )
        if obj_trivago.check_exists_by_xpath(ele_repo.elements['xp_more_options_trivago']):
            more_options = self.driver.find_element_by_xpath(ele_repo.elements['xp_more_options_trivago'])
            obj_trivago.scroll_to_particular_element(more_options)
            time.sleep(1)
            while str(more_options.text) == "Más":
                self.driver.execute_script("arguments[0]. click()", more_options)
                time.sleep(2)
        offer_logo = self.driver.find_elements_by_xpath(ele_repo.elements['xp_logo_for_offers_tivago'])
        for offer in offer_logo:
            ind = offer_logo.index(offer)
            offer_name = offer_logo[ind].get_attribute('title')
            if str(offer_name).upper( ).startswith("TUI"):
                return ind
                break

    def select_the_tui_offer(self, index):
        flag = False
        offer_logo = self.driver.find_elements_by_xpath(ele_repo.elements['xp_logo_for_offers_tivago'])
        self.driver.execute_script("arguments[0]. click()", offer_logo[index])
        # offer_logo[index].click()
        handles = self.driver.window_handles
        handle_count = len(handles)
        self.driver.switch_to_window(handles[handle_count - 1])
        offer_title = self.driver.title
        if str(offer_title).startswith("TUI"):
            return flag

    def verify_the_search_criteria_on_ibe_and_trivago(self, start_date, end_date, exp_passenger_count):
        handles = self.driver.window_handles
        obj_trivago.wait_for_more_option_to_display(ele_repo.elements['xp_tab_selection_ibe'])
        tab = self.driver.find_element_by_xpath(ele_repo.elements['xp_tab_selection_ibe'])
        obj_trivago.wait_unit_is_displayed("//span[contains(text(),'Reservar ahora')]")
        active_attribute = tab.get_attribute('class')
        if str(active_attribute).__contains__('--active'):
            print("tab Selected:")
        else:
            tab.click( )
        date_check_status = obj_trivago.verify_dates(start_date, end_date)
        total_expected_passenger_count = obj_trivago.get_expected_passenger_count(exp_passenger_count)
        passenger_count_check = obj_trivago.verify_passenger_count(total_expected_passenger_count)
        self.driver.close( )
        self.driver.switch_to_window(handles[0])
        if passenger_count_check is True and date_check_status is True:
            return True

    def get_expected_passenger_count(self, pass_count):
        total_passenger_count = 0
        pass_count = str(pass_count).split(",")
        if len(pass_count) > 1:
            adult_count = str(pass_count[0])[:1]
            child_count = str(pass_count[1])[:1]
            total_passenger_count = int(adult_count) + int(child_count)
            return total_passenger_count
        else:
            total_passenger_count = str(pass_count[0])[:1]
            return total_passenger_count

    def change_browser_region(self, region_set, index):
        # region = "Spain"
        # reg_set.load_website()
        # search_bar = driver.find_element_by_xpath(ele_repo.elements['xp_search_bar'])
        # search_bar.send_keys("abc")
        # search_bar.send_keys(Keys.ENTER)
        english_title = self.driver.find_element_by_xpath("//div[contains(text(), 'Google angeboten auf:')]//a")
        language_text = english_title.text
        print("Language available::", language_text)
        screen_shot_name_for_page_loading = os.path.join(projectPath, 'screenshots//') + str("page_load_") + str(index) + ".png"
        app.driver.save_screenshot(screen_shot_name_for_page_loading)
        if str(language_text) == "English":
            english_title.click()
        driver = app.get_driver()
        region = self.get_region(region_set)
        settings_button = self.driver.find_element_by_xpath("//a[@id='abar_button_opt' or text()='Settings']")
        settings_button.click()
        search_setting_option = self.driver.find_element_by_xpath("//a[ text()='Search settings']")
        self.driver.execute_script("arguments[0].click()", search_setting_option)
        region_setting_header = self.driver.find_element_by_xpath("//*[ text()='Region Settings'] ")
        self.scroll_to_particular_element(region_setting_header)
        more_options = self.driver.find_element_by_xpath("//a[@id='regionanchormore']")
        more_options.click()
        countries = self.driver.find_elements_by_xpath("//div[@id='regionother']//span[2]")
        radio_buttons = self.driver.find_elements_by_xpath("//div[@id='regionother']//span[1]")
        for county in countries:
            index = countries.index(county)
            if str(county.text) == str(region):
                print("Matched")
                # // div[ @ id = 'regionother'] // span[2] // preceding::span[contains( @class ,'radiobutton-radio' )]
                ActionChains(driver).move_to_element(radio_buttons[index]).click().perform()
                self.apply_style(county)
                self.apply_style(radio_buttons[index])
                # radio_button.click()
        save_button = driver.find_element_by_xpath("//div[text()='Save']")
        save_button.click()
        time.sleep(2)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        return screen_shot_name_for_page_loading
        # driver.close()


obj_trivago = TrivagoMetas.get_instance( )
