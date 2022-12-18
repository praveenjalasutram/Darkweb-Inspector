# Darkweb Inspector & Surfaceweb Inspector Tools

![image](https://user-images.githubusercontent.com/17245435/208282422-8cada54b-db74-4f88-bd0b-d0b4d9667f70.png)

## How to Use the Darkweb Inspector & SurfaceWeb Inspector tools
The Darkweb Inspector and SurfaceWeb Inspectors are Python programs that allows you to search for specific keywords on a list of URLs and display and save the results. It includes a graphical user interface (GUI) using the Tkinter library, which allows you to enter the list of URLs and keywords, start the search, and view the results.

## Difference between Surfaceweb-Inspector and Darkweb-Inspector scripts
Both are almost similar in functionality with minor difference being the DarkWeb Inspector tool uses defined Darkweb Onion links whereas SurfaceWeb-Inspector expect user to provide the URLs manually through GUI to perform the search. For Darkweb-Inspector.py script, the list of URLs to search is obtained from a specified page (https://raw.githubusercontent.com/praveenjalasutram/Darkweb-Inspector/main/Darkweb%20URL%20List in this case). The script extracts the list of URLs from the page and searches them for the specified keywords. But for the Surfaceweb-Inspector.py script, you have to enter the desired URLs manually through GUI.

## Prerequisites
Before you can use the keyword search script, you need to have the following installed on your computer:

- Python 3
- The Tkinter library (which is included with Python)
- The requests and BeautifulSoup libraries (which can be installed using pip install requests beautifulsoup4)

## How to install Prerequisites

* Download Python 3 from here: https://www.python.org/download/releases/3.0/

After you installed Python3, To install the required libraries in Python 3, you can use the pip package manager. Here are the steps you can follow to install the Tkinter library (which is included with Python), and the requests and BeautifulSoup libraries (which can be installed using pip):

1. Open a terminal or command prompt.

2. Make sure you have pip installed. You can check if pip is installed by running the following command:

`pip --version`

If pip is installed, you should see a message indicating the version of pip that is installed. If pip is not installed, you can install it by running the following command:

`python3 -m ensurepip --upgrade`

Install the requests library by running the following command:

`pip install requests`

Install the BeautifulSoup library by running the following command:

`pip install beautifulsoup4`

Once these libraries are installed, you should be able to use them in your Python scripts.

## Running the Script
To run the keyword search script, open a terminal or command prompt and navigate to the directory where the script is located. Then enter the following command:

`python3 Darkweb-Inspector.py` or `python3 Surfaceweb-Inspector.py` (based on the selected script)
 
This will launch the GUI of the keyword search script.

## Using the GUI
The GUI of the keyword search script consists of two entry fields and a button.

- In the first entry field, you can enter the list of URLs to search, separated by commas.
- In the second entry field, you can enter the list of keywords to search for, separated by commas.
- To start the search, click the "Search" button.

The results of the search will be displayed in a text widget below the button. Each result will consist of the keyword that was found, the URL where it was found, and the location (such as the page's title or meta tags) where it was found.

If no keywords are found on a URL, a message will be displayed indicating that no keywords were found.

## Saving the Results
To save the results of the search to a file, you can use the save as option in the text widget's context menu (right-click on the text widget). This will allow you to specify a file name and location for the results, and save them to a text file.

## Example Usage
Here is an example of how to use the keyword search script:

1. Enter the following list of URLs in the first entry field: http://www.example.com,http://www.example.net (This step is only for Surfaceweb-Inspector.py, for Darkweb-Inspector.py, it will be automatically fetched from predefined onion links)
2. Enter the following list of keywords in the second entry field: keyword1,keyword2,keyword3
3. Click the "Search" button.
4. The results of the search will be displayed in the text widget. If any of the keywords are found on the URLs, the URL and location where they were found will be displayed. If no keywords are found, a message indicating that no keywords were found will be displayed.

I hope this user guide helps you to understand how to use the keyword search script. Let me know if you have any questions or need further assistance.
