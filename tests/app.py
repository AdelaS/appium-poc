from time import sleep
from selenium.common.exceptions import NoSuchElementException


class App:

    def __init__(self, driver):
        self.driver = driver

        self.default_timeout = 1000
        self.iteration_sleep = 100

    def wait_for_element_present(self, selector, timeout=None):
        locator = selector.to_locator()

        iteration_count = int(
            (timeout or self.default_timeout) / self.iteration_sleep
        )

        element = None
        exception = None

        for x in range(0, iteration_count):
            try:
                element = self.driver.find_element_by_android_uiautomator(
                    locator
                )
            except NoSuchElementException as e:
                # Conversion from milliseconds to seconds
                sleep(self.iteration_sleep / 1000)

                # Store the exception so we can raise it if we
                # really didn't find the element
                exception = e
            else:
                return element

        raise exception
