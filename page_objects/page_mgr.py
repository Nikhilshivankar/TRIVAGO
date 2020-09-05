import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from object_repository import ele_repo
from utilities.convert_month import get_month
from utilities.text_reader_n_writer import read_write_txt

from data.config import projectPath
from lib.application import app
from object_repository import ele_repo
# from page_objects.page_mgr import Page

"""
        This class is for handling different page objects classes in framework

"""


class Page(object):
    def __init__(self, driver):

        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):

        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def apply_style(self, element):
        """This method is to apply style(highlight a particular element)"""
        style = "background: amber; border: 2px solid red;"
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)

    def scroll_to_particular_element(self, element):
        """
         Function to bring a specific element into view
         Parameter passed is the element, which needs to be in the view.
         Created by: Namita
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_progressbar(self):
        progress_bar = self.driver.find_element_by_xpath(ele_repo.elements['xp_loading_indicator_gp'])
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((progress_bar.get_attribute('aria-hidden'), 'true')))

    def wait_for_more_option_to_display(self, element):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, element)))

    def not_busy(self):
        try:
            element = self.driver.find_element_by_xpath(ele_repo.elements['xp_loading_indicator_gp'])
        except NoSuchElementException:
            return False
        return element.get_attribute("aria-hidden") == "false"
        self.wait.until(not_busy)

    def wait_unit_is_displayed(self, element):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,' loading-button__button button ')]"))
        )

    def wait_for_loading_indicator(self):
        indicator = self.driver.find_element_by_xpath(ele_repo.elements['xp_loading_indicator_gp'])
        attribute_value = indicator.get_attribute('style')
        while attribute_value == "opacity: 0;":
            time.sleep(1)
            attribute_value = indicator.get_attribute('style')

    def progress_bar_wait(self):
        progress_bar = self.driver.find_element_by_xpath(ele_repo.elements['xp_ads_gp_progress_bar'])
        attribute_value = progress_bar.get_attribute('aria-hidden')
        while attribute_value == "false":
            time.sleep(1)
            attribute_value = progress_bar.get_attribute('aria-hidden')

    def check_side_bar(self):
        test = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='wp-tabs-container']")))

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def check_overlay_displayed_and_click(self, element):
        overlay_element = self.driver.find_element_by_xpath("//div[@class='df_overlay js-overlay']")
        status = overlay_element.is_displayed( )
        if status is True:
            print("")
        else:
            element.click( )

    def verify_dates(self, start_date, end_date):
        expected_start_date = self.get_expected_dates_to_compare(start_date)
        expected_end_date = self.get_expected_dates_to_compare(end_date)
        dates = self.driver.find_element_by_xpath(ele_repo.elements['xp_date_selection_ibe'])
        self.scroll_to_particular_element(dates)
        self.apply_style(dates)
        time.sleep(1)
        actual_dates = str(dates.text).split(" – ")
        print("Exepected Start Date::", expected_start_date)
        print("Actual Start Date::", actual_dates[0])
        print("Expected End Date::", expected_end_date)
        print("Actual End Date::", actual_dates[1])
        if expected_start_date == str(actual_dates[0]) and expected_end_date == str(actual_dates[1]):
            return True

    def verify_passenger_count(self, expected_passenger_count):
        passenger_count_ibe = self.driver.find_element_by_xpath(ele_repo.elements['xp_passenger_count_ibe'])
        self.apply_style(passenger_count_ibe)
        actual_passenger_count = str(passenger_count_ibe.text).split(" ")
        if expected_passenger_count == actual_passenger_count[0]:
            return True
        else:
            return False

    def get_expected_dates_to_compare(self, dates):
        expected_from_date = dates.split("-")
        dictionary = read_write_txt.reading_dictionary()
        region = self.get_region(dictionary['Environment'])
        month = get_month(expected_from_date[1], region)
        print("Month Now::", month)
        if str(month).__contains__("sept"):
            expected_from_date_to_compare = str(expected_from_date[0]) + " " + str(month)[:4].lower() + "."
        else:
            expected_from_date_to_compare = str(expected_from_date[0]) + " " + str(month)[:3].lower( ) + "."
        return expected_from_date_to_compare

    def hotel_verification_after_search(self, hotel_name_searched, element):
        screen_shot_name = os.path.join(projectPath, 'screenshots//') + str("hotel_name") + ".png"
        app.driver.save_screenshot(screen_shot_name)
        hotel_name_element = self.driver.find_element_by_xpath(ele_repo.elements['xp_hotel_name'])
        self.apply_style(hotel_name_element)
        hotel_name_displayed = hotel_name_element.text
        status = self.check_exists_by_xpath(element)
        print("Status >>>>>", status)
        if str(hotel_name_displayed).find(hotel_name_searched) != "-1" and status is True:
            return True
        else:
            return False

    def check_tui_google_ads(self, from_date, to_date, passenger_count, ready_button_xpath, element, passenger_element, passenger_options):

        print("inside the check_tui_google_ads function :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        # self.wait_for_loading_indicator( )
        # self.apply_style(more_options)
        # self.scroll_to_particular_element(more_options)
        # self.driver.execute_script("arguments[0]. click()", more_options)
        # ActionChains(self.driver).move_to_element(element).pause(2).perform()
        # screen_shot_name = os.path.join(projectPath, 'screenshots//') + str("before_driver_close_") + str(
        #     end_date) + ".png"
        # app.driver.save_screenshot(screen_shot_name)
        index = self.select_start_date(from_date, element)
        self.select_end_date(to_date, index)
        time.sleep(1)
        ready_button = self.driver.find_elements_by_xpath(ready_button_xpath)
        self.driver.execute_script("arguments[0]. click()", ready_button[1])
        self.progress_bar_wait( )
        self.passenger_selection(passenger_count, passenger_element, passenger_options)
        screen_shot_name = os.path.join(projectPath, 'screenshots//') + str("after_pax_selection_") + str(to_date) + ".png"
        app.driver.save_screenshot(screen_shot_name)
        time.sleep(1)
        self.progress_bar_wait( )

    def select_start_date(self, date, element):
        start_date_box = self.driver.find_elements_by_xpath(element)
        self.apply_style(start_date_box[1])
        start_date_box[1].click( )
        start_date = str(date).split("-")
        day = start_date[0]
        month = start_date[1]
        current_month_header = self.driver.find_elements_by_xpath(ele_repo.elements['xp_month_header'])
        # next_month_arrow_one = self.driver.find_element_by_xpath(ele_repo.elements['xp_next_month_arrow'])
        next_month_arrow = self.driver.find_elements_by_xpath(ele_repo.elements['xp_next_month_arrow'])
        index_month = 0
        for i in current_month_header:
            ind = current_month_header.index(i)
            time.sleep(1)
            if str(current_month_header[ind].text).upper().__contains__(str(month).upper()):
                    # or str(current_month_header[int(ind + 1)].text).upper() == str(month).upper():
                # if str(i.text) == str(month) and i.is_displayed():
                index_month = ind
                time.sleep(5)
                self.select_day_of_start_month(index_month + 1, day)
                return index_month + 1
                break
            else:
                next_month_arrow[len(next_month_arrow) - 1].click()

    def select_day_of_start_month(self, index_month, day):
        xp_month = "//div[@role='dialog']//div[@role='listitem'][" + str(index_month) + "]"
        mo = self.driver.find_element_by_xpath(xp_month)
        ActionChains(self.driver).move_to_element(mo).pause(2).perform()
        self.apply_style(mo)
        date_cells = self.driver.find_elements_by_xpath(xp_month + "/div[3]//div[contains(@jsaction,'clickonly')]")
        for date in date_cells:
            if str(date.text).startswith(str(day)):
                ActionChains(self.driver).move_to_element(date).pause(2).perform()
                self.apply_style(date)
                date.click()
                break

    def select_day_of_end_month(self, index_month, day):
        xp_month = "//div[@role='dialog']//div[@role='listitem'][" + str(index_month) + "]"
        mo = self.driver.find_element_by_xpath(xp_month)
        ActionChains(self.driver).move_to_element(mo).pause(2).perform( )
        date_cells = self.driver.find_elements_by_xpath(xp_month + "/div[3]//div[contains(@jsaction,'clickonly')]")
        for date in date_cells:
            if str(date.text).startswith(str(day)):
                self.apply_style(date)
                ActionChains(self.driver).move_to_element(date).pause(2).perform( )
                date.click()
                break

    def select_end_date(self, date, index):
        end_date = str(date).split("-")
        day = end_date[0]
        month = end_date[1]
        self.select_day_of_end_month(index, day)

    def passenger_selection(self, passenger_count, passenger_element_xpath, passenger_options_xpath):
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
        passenger_element = self.driver.find_elements_by_xpath(passenger_element_xpath)
        passenger_options = self.driver.find_elements_by_xpath(passenger_options_xpath)
        self.apply_style(passenger_element[1])
        default_value = str(passenger_element[1].text)[:1]
        if str(passenger_count).startswith(default_value):
            print("Passenger Set")
        else:
            passenger_element[1].click()
            passenger_count = str(passenger_count).split(" ")
            for opt in passenger_options:
                if opt.get_attribute('data-value') == str(passenger_count[0]):
                    self.driver.execute_script("arguments[0]. click()", opt)
                    break

    def check_tui_ads_on_google_page(self):
        index = None
        ads_list = self.driver.find_elements_by_xpath(ele_repo.elements['xp_ads_list'])
        for i in ads_list:
            if str(i.text).startswith("TUI"):
                self.scroll_to_particular_element(i)
                index = ads_list.index(i)
                return index
                break

    def set_dates(self, from_date, start_date_element, index):
        start_date_element = self.driver.find_elements_by_xpath(start_date_element)
        start_date_element[index].click()
        month_header = self.driver.find_element_by_xpath(ele_repo.elements['xp_month_header_search_page'])
        actual_month_value = month_header.text
        from_date = str(from_date).split("-")
        expected_month = from_date[1]
        date_to_set = from_date[0]
        current_month = str(actual_month_value).split(" ")[0]
        arrows = self.driver.find_elements_by_xpath(ele_repo.elements['xp_month_arrow'])
        month_header = self.driver.find_elements_by_xpath("//calendar-month//month-header//jsl")
        for month in month_header:
            if str(month.text) == str(expected_month):
                previous_button = arrows[0]
                self.driver.execute_script("arguments[0].click()", previous_button)
                dates = self.driver.find_elements_by_xpath(ele_repo.elements['xp_dates_search_page'])
                for day in dates:
                    if str(day.text) == str(date_to_set):
                        self.apply_style(day)
                        day.click()
                break
            else:
                next_button = arrows[1]
                self.apply_style(next_button)
                time.sleep(2)
                self.driver.execute_script("arguments[0].click()", next_button)

    def get_region(self, region):
        if str(region) == str("Spain_Gha"):
            return "Spain"
        elif str(region) == str("Portugal_Gha"):
            return "Portugal"







