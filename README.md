# Generate Static Site using python
A simple generate static site program using python. The program allows you to convert non-html files into html files,

with an addition of supportive html files such as navigation pages, footer page or sidebar pages.
## Getting started
To run the project, you will need to have Python 3 and pip installed in your system.

Having a virtual environment is highly encouraged for easier installion of the packages used.
### Installation
1. Clone or download the repository to your local machine or your preferred coding environment.


    `gh repo clone charityngunyi/generateStaticSitePython`

2. Enter the working folder/directory

    `cd generateStaticSitePython`

3. Use pip to install the required libraries.

    `pip install -r requirements.txt`

### Usage
1. Copy your three directories that contain the templates for into your root project directory (generateStaticSitePython):
    1. Supporting template directory that will hold your supporting files such as navigation page, footer page..
    2. Input directory that contain the nohtml files to be converted into html.
    3. The output directory that will hold the generated html files.

2. Run the program using the following command:

    `python main.py`

3. The program will ask for user input in the console. Enter your three folders name that you added from the above statement.
