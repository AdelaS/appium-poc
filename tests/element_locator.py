class ElementLocator:
    """Identifier for an element in the UI."""

    def __init__(self, prefix, selector):
        self.prefix = prefix
        self.selector = selector

    def to_locator(self):
        """Gets the locator in the format expected by Appium.

        Returns (str):
            The locator expected by Appium.
        """
        return 'new UiSelector().resourceId("{}{}")'.format(
            self.prefix,
            self.selector
        )
