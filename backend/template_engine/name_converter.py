import re


def converter(s):
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    s = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub("([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.lower()
