from time import sleep
from selenium.common.exceptions import NoSuchElementException


class App:
    """Represents the application that is being tested."""

    def __init__(self, driver):
        self.driver = driver

        self.default_timeout = 1000
        self.iteration_sleep = 100

    def wait_for_element_present(self, selector, timeout=None):
        """Waits for a element to be present on the screen.

        Args:
            selector (ElementLocator):
                The selector of the element to wait for.

            timeout (int):
                Number of milliseconds to wait.

        Returns (UiSelector):
            The element that has been found.

        Raises:
            NoSuchElementException:
                If the element is not found in the given time.
        """
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
