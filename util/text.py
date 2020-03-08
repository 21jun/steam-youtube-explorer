import re


def clean_text(text):
    text = text.lower()
    # replace special chars and keep spaces
    text = re.sub(r"[ ](?=[ ])|[^A-Za-z0-9 ]+", '', text)
    text = re.sub(' +', ' ', text)  # replace multiple spaces and keep one
    return text
