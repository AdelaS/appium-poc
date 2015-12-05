class Util:
    @staticmethod
    def remove_whitespace(value):
        return value.replace(' ', '')

    @staticmethod
    def text_to_binary(text):
        return bin(int.from_bytes(text.encode(), 'big')).replace('b', '')
