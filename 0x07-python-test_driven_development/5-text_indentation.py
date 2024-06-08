#!/usr/bin/python3
"""
This module defines a function `text_indentation` that prints a text with 2 new lines
after each of these characters: ., ? and :.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text: The text to be processed, must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in chars:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    
    print(result.strip())
