import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Set the URL of the page with the list of URLs to search
# Actual URL - Use it for Darkweb searches
url_list_url = 'https://raw.githubusercontent.com/praveenjalasutram/Darkweb-Inspector/main/Darkweb%20URL%20List'
# Test URL - Use it to test the code
# url_list_url = 'https://raw.githubusercontent.com/praveenjalasutram/Darkweb-Inspector/main/Test%20URLs%20for%20Darkweb-Inspector'

# Set the keywords to search for
keywords = ['keyword1', 'keyword2', 'keyword3']

# Create the main window
window = tk.Tk()
window.title('Keyword Search')
# window.attributes('-fullscreen', True) # For Full screen
window.geometry('1920x1080')  # Fit the window to the size of the screen

# Create a label for the keyword list
keyword_label = tk.Label(text='Keywords:')
keyword_label.grid(row=0, column=0)

# Create an entry field for the keyword list
keyword_entry = tk.Entry(width=50)
keyword_entry.insert(0, 'keyword1,keyword2,keyword3')
keyword_entry.grid(row=0, column=1)

# Create a button to start the search
search_button = tk.Button(text='Search')
search_button.grid(row=0, column=2)

# Create a label for the Results list
Result_label = tk.Label(text='Results:')
Result_label.grid(row=1, column=0)

# Create a text widget to display the results
results_text = tk.Text(width=175, height= 40)
results_text.grid(row=3, column=1, columnspan=2)

# Define a function to start the search
def start_search():
  # Get the list of keywords from the entry field
  keywords = keyword_entry.get().split(',')

  # Clear the results text widget
  results_text.delete('1.0', tk.END)

  # Fetch the page with the list of URLs
  page = requests.get(url_list_url)
  soup = BeautifulSoup(page.content, 'html.parser')

  # Extract the list of URLs from the page
  urls = []
  for link in soup.find_all('a'):
    if 'http' in link.get('href'):
      urls.append(link.get('href'))

  # Search the URLs for the keywords
  for url in urls:
    try:
      # Attempt to fetch the URL
      page = requests.get(url)
      soup = BeautifulSoup(page.content, 'html.parser')
      found = False

      # Search the page's title for the keywords
      title = soup.find('title')
      if title:
        for keyword in keywords:
          if keyword in title.text:
            found = True
            results_text.insert(tk.END, f'Keyword "{keyword}" found in title at URL: {url}\n')

            # Search the page's meta tags for the keywords
      metas = soup.find_all('meta')
      if metas:
        for meta in metas:
          for keyword in keywords:
            if 'name' in meta.attrs and keyword in meta['name'].lower():
              found = True
              results_text.insert(tk.END, f'Keyword "{keyword}" found in meta tags at URL: {url}\n')
      # If no keywords were found, display a message
      if not found:
        results_text.insert(tk.END, f'No keywords found at URL: {url}\n')
    except:
      # If an error occurred while fetching the URL, display a message
      results_text.insert(tk.END, f'Error fetching URL: {url}\n')

# Bind the start_search function to the search button's "clicked" event
search_button.config(command=start_search)

# Run the main loop of the GUI
window.mainloop()
