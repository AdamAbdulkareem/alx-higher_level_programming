#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as text_file:
        write_text = text_file.write(text)
        return write_text
