import string

def normalize_text(text):
    """Normalize text by converting to lowercase, removing punctuation and spaces."""
    return text.lower().translate(str.maketrans('', '', string.punctuation + ' '))
