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
    
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
    
    print(result.strip())
