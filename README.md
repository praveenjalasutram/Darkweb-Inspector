# Darkweb Inspector

## How to Use the Darkweb Inspector
The Darkweb Inspector is a Python program that allows you to search for specific keywords on a list of URLs () and display the results. It includes a graphical user interface (GUI) using the Tkinter library, which allows you to enter the list of URLs and keywords, start the search, and view the results.

## IMPORTANT
Fore Darkweb-Inspector.py script, the list of URLs to search is obtained from a specified page (https://raw.githubusercontent.com/praveenjalasutram/Darkweb-Inspector/main/Darkweb%20URL%20List in this case). The script extracts the list of URLs from the page and searches them for the specified keywords. But for the Surfaceweb-Inspector.py script, you have to enter the desired URLs manually.

## Prerequisites
Before you can use the keyword search script, you need to have the following installed on your computer:

- Python 3
- The Tkinter library (which is included with Python)
- The requests and BeautifulSoup libraries (which can be installed using pip install requests beautifulsoup4)

## Running the Script
To run the keyword search script, open a terminal or command prompt and navigate to the directory where the script is located. Then enter the following command:

`python keyword_search.py`

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

1. Enter the following list of URLs in the first entry field: http://www.example.com,http://www.example.net
2. Enter the following list of keywords in the second entry field: keyword1,keyword2,keyword3
3. Click the "Search" button.
4. The results of the search will be displayed in the text widget. If any of the keywords are found on the URLs, the URL and location where they were found will be displayed. If no keywords are found, a message indicating that no keywords were found will be displayed.

I hope this user guide helps you to understand how to use the keyword search script. Let me know if you have any questions or need further assistance.
