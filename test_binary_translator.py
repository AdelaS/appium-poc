from tests.screen import Screen


class TestBinaryTranslator:

    def test_convert_text_to_binary(self, app_driver):
        screen = Screen(app_driver)

        screen.fill_input_text('test')
        screen.click_encode_button()
        screen.assert_binary_conversion('test')
