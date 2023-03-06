import re

def select_language():
    language = input('Select a language (default: en): ')
    if re.search(r'[Rr]u\w*', language):
        return 'ru-RU'
    else:
        return 'en-US'