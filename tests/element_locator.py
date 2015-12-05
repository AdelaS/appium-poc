class ElementLocator:

    def __init__(self, prefix, selector):
        self.prefix = prefix
        self.selector = selector

    def to_locator(self):
        return 'new UiSelector().resourceId("{}{}")'.format(
            self.prefix,
            self.selector
        )
