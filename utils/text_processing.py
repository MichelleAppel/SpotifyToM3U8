import string

def normalize_text(text):
    """Normalize text by converting to lowercase, removing punctuation, and ignoring certain phrases."""
    ignore_phrases = ["original mix"]

    text = text.lower().translate(str.maketrans('', '', string.punctuation))

    for phrase in ignore_phrases:
        text = text.replace(phrase, '')

    return text.replace(' ', '')
