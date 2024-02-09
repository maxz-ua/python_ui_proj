import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkboxes == output_result, 'Test assertion: no checkboxes'

    class TestRadioButton:
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
    class TestWebTable:
        def test_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            time.sleep(1)
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result
