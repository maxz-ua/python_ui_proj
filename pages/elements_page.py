import base64
import os
import random
import time

import allure
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import (TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
, ButtonsPageLocators, UploadAndDownloadPageLocators)
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill in all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace("\n", " ")
        permanent_address = person_info.permanent_address.replace("\n", " ")
        with allure.step("Filling fields"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("Click submit button"):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Check form")
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("Open full list")
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("Click random checkbox")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        for _ in range(count):  # use a for loop to iterate elements
            item = random.choice(item_list)  # use random.choice to select a random element
            self.go_to_element(item)
            item.click()

    @allure.step("Get Checked checkbox")
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    @allure.step("Get output result")
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Click on button")
    def click_on_button(self, button):
        buttons = {'yes': self.locators.YES_RB,
                   'impressive': self.locators.IMPRESSIVE_RB,
                   'no': self.locators.NO_RB}
        if button not in buttons:
            raise ValueError(f"Invalid button: {button}. Expected one of: {', '.join(buttons.keys())}")
        button_locator = buttons[button]
        try:
            button_element = self.element_is_visible(button_locator)
            button_element.click()
        except Exception as e:
            raise RuntimeError(f"Error clicking on button '{button}': {str(e)}")

    @allure.step("Get result")
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("Click on different buttons")
    def click_on_diff_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE))
            return self.check_clicked_on(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT))
            return self.check_clicked_on(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK).click()
            return self.check_clicked_on(self.locators.SUCCESS_CLICK)

    @allure.step("Check is clicked on")
    def check_clicked_on(self, element):
        return self.element_is_present(element).text


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    @allure.step("Upload file")
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step("Download file")
    def download_file(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        link = self.element_is_present(self.locators.DOWNLOAD).get_attribute('href')
        # Decode the base64-encoded link
        link_bytes = base64.b64decode(link)
        # Find the start of the JPEG content
        offset = link_bytes.find(b'\xff\xd8')
        # Generate a random filename with a unique identifier
        file_name = f'filetest_{random.randint(0, 9999)}_{random.randint(0, 9999)}.jpg'
        file_path = os.path.join(current_directory, file_name)
        # Write the decoded content to the file
        with open(file_path, 'wb') as f:
            f.write(link_bytes[offset:])
        # Check if the file exists
        file_exists = os.path.exists(file_path)
        os.remove(file_path)
        return file_exists
