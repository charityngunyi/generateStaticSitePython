"""
The aim of this project is to generate static site.
My name is Charity Ngunyi, ngunyicharity@gmail.com, for job links purposes.
The main file imports two functions from two files, one deal with user defining the folders location
and the other file deals with file conversions
"""

from locate_folders_function import *
from convert_to_html import *

if __name__ == '__main__':
    # generate_site_constant_folders() for testing purposes
    convert_files(generate_site_constant_folders())

