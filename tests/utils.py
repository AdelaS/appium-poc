class Util:
    """Static utilities used throughout the tests to make the code more readable."""

    @staticmethod
    def remove_whitespace(value):
        """Removes whitespace from a given string.

        Args:
            value (str):
                The value to remove whitespace from.

        Returns (str):
            Input string without whitespace.
        """
        return value.replace(' ', '')

    @staticmethod
    def text_to_binary(text):
        """Converts the specified string to it's binary value.

        Args:
            text (str):
                The value to convert.

        Returns (str):
            Binary representation of the input string.
        """
        return bin(int.from_bytes(text.encode(), 'big')).replace('b', '')
