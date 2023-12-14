import re

def detect_lang(text):
    """Detect language of text.

    Count the character of Thai characters using regex [ก-๙]
    If the count is more than half of the total characters, return 'TH'
    Otherwise, return 'EN'
    """
    th_chars = re.findall(r'[ก-๙]', text)
    if len(th_chars) > len(text) / 2:
        return 'TH'
    else:
        return 'EN'