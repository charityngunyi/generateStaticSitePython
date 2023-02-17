"""
Convert possible file formats into html file.
The converted file will be used as the body section
In this case the program can convert three file formats, which are
    1. Json file
    2. Markdown file
    3. Xml file
"""
import json
# imports
# Makrkdown package to transform markdown files to html.
# xmltodict to convert xml to dictionary and json2html to convert json to html
import os
import xmltodict
import markdown
from json2html import *


def convert_files(the_folders):
    # in this case the_folders is a tuple
    static_folder = the_folders[0]
    input_folder = the_folders[1]
    export_folder = the_folders[2]
    # Check for errors
    file_type_error = ""
    file_type = False
    try:
        for filename in os.listdir(input_folder):

            slag = [] # will help to hold the file types formats that we may need
            # file = ""

            #         check file types
            if filename.endswith(".md"):
                file_type = True
                slag.append('md')
            elif filename.endswith(".json"):
                file_type = True
                slag.append('json')
            elif filename.endswith(".xml"):
                file_type = True
                slag.append('xml')
            else:
                file_type_error = "File type not supported"

            while file_type:  # if file type exists
                html = ""
                # Read the possible file
                with open(os.path.join(input_folder, filename), "r") as file:
                    data = file.read()
                    for s in slag:
                        if s == "md":
                            # Convert the markdown to HTML
                            html = markdown.markdown(data)
                        elif s == "json":
                            # convert the json file to html
                            html = json2html.convert(json=data)
                        elif s == "xml":
                            # convert the xml file to html
                            # use xmltodict package to convert it first to dict and then to json
                            data_dict = xmltodict.parse(data)
                            json_data = json.dumps(data_dict) # to json
                            html = json2html.convert(json=json_data)
                # Read support static files
                nav_page = open(os.path.join(static_folder, "header.html"), "r").read()
                footer_page = open(os.path.join(static_folder, "footer.html"), "r").read()
                index_page = open(os.path.join(static_folder, "index.html"), "r").read()
                # Write the html content to the export folder
                # output filename is assumed to have a default name as my_static_site
                file_name_export = "my_static_site"
                with open(os.path.join(export_folder, file_name_export, "w")) as file:
                    file.write(nav_page)
                    file.write(index_page.replace("{{ body }}", html))
                    file.write(footer_page)
                    file.close()
    except: #possible errors
        print(file_type_error)
