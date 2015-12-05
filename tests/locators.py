from .element_locator import ElementLocator

prefix = 'de.android.BinarCodeTranslator:id/'

input_text = ElementLocator(prefix, 'EditTextText')
encode_button = ElementLocator(prefix, 'Encode')
binary_text = ElementLocator(prefix, 'EditTextBinary')
