from .app import App
from .utils import Util
from tests import locators
from selenium.common.exceptions import WebDriverException


class Screen(App):

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def fill_input_text(self, text):
        element = self.wait_for_element_present(locators.input_text)
        element.send_keys(text)
        self.hide_keyboard()

    def click_encode_button(self):
        element = self.wait_for_element_present(locators.encode_button)
        element.click()

    def assert_binary_conversion(self, text):
        element = self.wait_for_element_present(locators.binary_text)
        binary_value = Util.remove_whitespace(element.get_attribute('text'))
        expected_value = Util.text_to_binary(text)

        assert binary_value == expected_value
