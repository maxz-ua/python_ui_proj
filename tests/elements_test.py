import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, ButtonsPage, UploadAndDownloadPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("Text Box")
    class TestTextBox:
        @allure.title("Check Text Box")
        def test_text_box(self, drivers, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data

    @allure.feature("Check Box")
    class TestCheckBox:
        @allure.title("Check Check Box")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkboxes == output_result, 'Test assertion: no checkboxes'

    @allure.feature("Radio Button")
    class TestRadioButton:
        @allure.title("Check Radio Button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_button('yes')
            rb_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_button('impressive')
            rb_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_button('no')
            rb_no = radio_button_page.get_output_result()
            assert rb_yes == 'Yes'
            assert rb_impressive == 'Impressive'
            assert rb_no == 'No'

    @allure.feature("Different Buttons")
    class TestButtonsPage:
        @allure.title("Check Different Click")
        def test_different_clicks_on_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_diff_button("double")
            right = button_page.click_on_diff_button("right")
            click = button_page.click_on_diff_button("click")
            time.sleep(3)
            assert double == "You have done a double click", "Double was not pressed"
            assert right == "You have done a right click", "Right was not pressed"
            assert click == "You have done a dynamic click", "Dynamic was not pressed"

    @allure.feature("Upload and Download Files")
    class TestUploadAndDownload:
        @allure.title("Upload File")
        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, "Not uploaded"

        @allure.title("Download File")
        def test_download_file(self, driver):
            download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, "Not downloaded"
