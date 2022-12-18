import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Set the list of URLs to search
urls = ['http://www.example.com', 'http://www.example.net']
#urls = url_entry.get().split(',')

# Set the keywords to search for
keywords = ['keyword1', 'keyword2', 'keyword3']
#keywords = keyword_entry.get().split(',')

# Create the main window
window = tk.Tk()
window.title('SurfaceWeb-Inspector, Created by @CyberSec_Sai')
# window.attributes('-fullscreen', True) # For Full screen
window.geometry('1920x1080')  # Fit the window to the size of the screen

# Create a label for the URL list
url_label = tk.Label(text='URLs:')
url_label.grid(row=0, column=0)

# Create an entry field for the URL list
url_entry = tk.Entry(width=150)
url_entry.insert(0, 'Enter URLs separated by comma ","')
url_entry.grid(row=0, column=1, columnspan=5)

# Create a label for the keyword list
keyword_label = tk.Label(text='Keywords:')
keyword_label.grid(row=1, column=0)

# Create an entry field for the keyword list
keyword_entry = tk.Entry(width=150)
keyword_entry.insert(0, 'Enter keywords separated by comma ","')
keyword_entry.grid(row=1, column=1, columnspan=5)

# Create a button to start the search
search_button = tk.Button(text='Search')
search_button.grid(row=0, column=5, columnspan=5, rowspan=2)

# Create a label for the Results list
Result_label = tk.Label(text='Results:')
Result_label.grid(row=3, column=0)

# Create a text widget to display the results
results_text = tk.Text(width=175, height= 40)
results_text.grid(row=4, column=1, columnspan=5)

# Creator
creator_label = tk.Label(text='Created by CyberSec_Sai:\nWebsite: https://praveenjalasutram.wixsite.com/praveenjalasutram\nLinkedIn: https://www.linkedin.com/in/praveenjalasutram/\nTwitter: https://twitter.com/cybersec_sai\nGitHub: https://github.com/praveenjalasutram')
creator_label.grid(row=5, column=3)

# Define a function to start the search
def start_search():
  # Get the list of URLs and keywords from the entry fields
  urls = url_entry.get().split(',')
  keywords = keyword_entry.get().split(',')

  # Clear the results text widget
  results_text.delete('1.0', tk.END)
  
  # Search the URLs for the keywords
  for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
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
            results_text.insert(tk.END, f'Keyword "{keyword}" found in meta name at URL: {url}\n')
          elif 'content' in meta.attrs and keyword in meta['content'].lower():
            found = True
            results_text.insert(tk.END, f'Keyword "{keyword}" found in meta content at URL: {url}\n')

    # If no keywords were found, display a message
    if not found:
      results_text.insert(tk.END, f'No keywords found at URL: {url}\n')

# Bind the start_search function to the search button's "clicked" event
search_button.config(command=start_search)

# Run the main loop of the GUI
window.mainloop()
