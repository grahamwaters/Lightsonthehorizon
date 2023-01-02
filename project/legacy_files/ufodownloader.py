
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from tqdm import tqdm
from tqdm import tqdm_gui
import string
# connect to website and get list of all pdfs
#?url="https://www.theblackvault.com/documentarchive/ufos-the-central-intelligence-agency-cia-collection/"
nsaurl = "https://www.nsa.gov/news-features/declassified-documents/ufo/"
'''
these are the links
starting with the first part of 16 files on ufos in the database these links are sequential
https://vault.fbi.gov/UFO/UFO%20Part%201%20of%2016/view
and they end at this link below
https://vault.fbi.gov/UFO/UFO%20Part%2016%20of%2016/view



this is the mufon gallery url
https://ufostalker.com/gallery
https://www.worldufophotos.org/page/send-your-photos/#/gallery/top-200-ufo-photos/top-200-3-18-20-shropshire-england-mufon/

'''
#?input
choice = input("for nsaurl enter 2: ")
choice = int(choice)
#?end input section

#? FBI list
links = []
iterator = 1
initial = "https://vault.fbi.gov/UFO/UFO%20Part%20"
preending = "%"
postending = "20of%2016/view"
ending = preending + postending #this combines to create the end of the url
top = 16
while iterator < top:
    url = initial + str(iterator) + ending
    links.append(str(url))
    iterator += 1 #iterate up one
#? end FBI list

if choice == 2:
    links = []
    links.append(nsaurl)

#? MUFON list
""" Here is the explanation for the code above:
1. We request the web page using requests.get() and save the response object in a variable called response.
2. We then create a soup object using BeautifulSoup() and pass the response.content and the parser type as arguments.
3. We use the soup object to find all the links with href ending with .pdf. We do this by using soup.select("a[href$='.pdf']") and save it in a variable called links.
4. We then iterate over each link in the links variable and download the pdf file to our local machine using the requests.get() method.
5. We save the pdf files in the folder we created using the os.path.join() method. """

#go through and extract the pdfs
for link in links:
    print("link:",link)
    #If there is no such folder, the script will create one automatically
    folder_location = r'E:\webscraping'
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    response = requests.get(link)
    soup= BeautifulSoup(response.text, "html.parser")
    for link in tqdm(soup.select("a[href$='.pdf']")):
        #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
