"""
    Create a function to allow the user to select the folders name of:
        1. The supporting pages e.g navigation page, footer page error page e.t.c.
        2. The folder containing the Markdown files or any other formats to be converted.
        3. The destination or output folder that will contain the generated site.
"""


# The function with three parameters to define the desired directory constants
def generate_site_constant_folders(supporting_directory="templates", to_be_converted_directory="inputs",
                                   destination_directory="outputs"):
    # Tuple is preferred since it is immutable
    # Ask the user for their preferred folder names
    # support_dir will hold users static supportind pages such as nav, footer..
    support_dir = input('Please input your template supporting directory termed as : {} :'
                        .format(supporting_directory))
    # convert_dir will hold user their preferred input directory containing the files to be converted
    convert_dir = input('Please input your template input directory termed as : {} :'
                        .format(to_be_converted_directory))
    # destiny_dir will hold the user output folder names
    destiny_dir = input('Please input your template output directory termed as: {} :'
                        .format(destination_directory))
    the_folders = (support_dir, convert_dir, destiny_dir)
    print(the_folders)
    return the_folders
