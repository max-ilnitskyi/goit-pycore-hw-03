import re


def normalize_phone(phone_number):
    wrong_chars_pattern = r"[^\d]"
    clean_number = re.sub(wrong_chars_pattern, "", phone_number)

    if clean_number.startswith("+"):
        return clean_number
    elif clean_number.startswith("380"):
        return "+" + clean_number
    else:
        return "+38" + clean_number
