import os


def clear_up(filename):
    """Delete the processed file>"""
    os.remove(filename)
    return True
