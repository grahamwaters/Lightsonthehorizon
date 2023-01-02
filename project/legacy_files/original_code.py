#MUFONVARIABLES.py
#include all of these libraries
from tqdm import tqdm
from tqdm import tqdm_gui
import time
import datetime
#from WebDriver import WebDriverWait
#from WebDriver import wait
from datetime import datetime
import string
import os
import fileinput
import os
from selenium.webdriver.support.ui import WebDriverWait
import icecream
import random
from urllib3.exceptions import HTTPError as BaseHTTPError
from icecream import ic
import re #regex
from selenium.webdriver.common.action_chains import ActionChains
import requests
from selenium import webdriver
from requests.exceptions import InvalidSchema
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebElement
from bs4 import BeautifulSoup as bs
from newspaper import Article
from selenium.webdriver import ActionChains
import urllib
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from newspaper import Article
from newspaper import Source
from newspaper import news_pool
from htmldom import htmldom
from selenium.webdriver.support.ui import Select
import urllib.request
from bs4 import BeautifulSoup
import csv
import urllib.request, urllib.error, urllib.parse, ssl
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import Levenshtein
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import csv

#selenium stellarium Variables for space object tracking
'''# todo
    1 - Main controls
    2 - Time Jump
    3 - Selection
    4 - Stars
    5 - Planets
    6 - Atmosphere
    Grids
    8 - DSO
    Landscape
    10 - Starlore
    Actions
    11 - Scripts
    10 - Location
    12 - Projection
'''
#* time tab
maincontrols_tab_dateyear_id = "date_year"
maincontrols_tab_datemonth_id = "date_month"
maincontrols_tab_dateday_id = "date_day"
maincontrols_tab_time_hour_id = "time_hour"
maincontrols_tab_time_minute_id  = "time_minute"
maincontrols_tab_time_second_id = "time_second"

#* field of view
maincontrols_tab_fieldofview_id = "view_fov"

#* location tab
location_tab_id = "ui-id-21"
location_tab_latitude_id = "loc_latitude"
location_tab_longitude_id = "loc_longitude"
location_tab_altitude_id = "loc_altitude"
location_tab_name_id = "loc_name"

#* time jump tab
timejump_tab_id = "ui-id-10"
location_tab_latitude_id = "loc_latitude"
location_tab_longitude_id = "loc_longitude"
location_tab_altitude_id = "loc_altitude"
location_tab_name_id = "loc_name"
#selenium variable front/ends section

atmosphere_tab_id = "ui-id-6"
lightpollution_class = "stelaction" #click this to enable real light polution sim from location

#* actions tab
actions_tab_class = "checkableaction"
actions_tab_datetime_value = "actionShow_DateTime_Window_Global"
actions_button_id = "bt_doaction" #click this to enable the above datetime value window.
actions_optionvalue_update = "actionRun_AstroCalc_UpdatePositions"
actions_optionvalue_screenshot = "actionSave_Screenshot_Global"
actions_optionvalue_show_starlink = "actionShow_Satellite_Group_starlink"
actions_optionvalue_show_militarysats = "actionShow_Satellite_Group_military"

addict = {0:"Date submitted",
                1:"Date/Time of Event",
                2:"Short Description",
                3:"Location of Event",
                4:"Long Description",
                5:"Attachments"}

nearest_city_field_x = "/html/body/center/div[2]/form/table/tbody/tr[8]/td[2]/input"
event_stateusa_x = '//*[@id="id_selbox_state_id"]'

description_x_front = "/html/body/center/form/table/tbody/tr[" #starts at 3
date_sub_x_front = "/html/body/center/form/table/tbody/tr["#starts at 3
date_time_front = "/html/body/center/form/table/tbody/tr[" #starts at 3
sdescr_front = "/html/body/center/form/table/tbody/tr[" # starts at 3
location_of_event_front = "/html/body/center/form/table/tbody/tr[" #starts at 3
#todo could be attachments... idk if you want them but here is the xpath
attachments_front = "/html/body/center/form/table/tbody/tr["# starts at 3
description_css_front = "body > center:nth-child(1) > form:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("
description_css_end = ") > td:nth-child(6) > input:nth-child(1)"
#body > center:nth-child(1) > form:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(6) > input:nth-child(1)
description_x_end = "]/td[6]/input"
date_sub_x_end = "]/td[2]"
date_time_end = "]/td[3]"
sdescr_end = "]/td[4]"
location_of_event_end = "]/td[5]"
attachments_end = "]/td[7]"
keywordfield_x = "/html/body/center/div[2]/form/table/tbody/tr[9]/td[2]/input[1]"
date_of_event_x = "/html/body/center/div[2]/form/table/tbody/tr[2]/td[2]/input[5]"
submit_button_x = "/html/body/center/div[2]/form/input[2]"
pagerows = 50 # number of rows allowed or visible on the MUFON screen

timestamp_string = str(datetime.now())

popup_text = "/html/body/center/table/tbody/tr[2]/td" # this holds the popup window's description text (long)
#popup_x_text = "/html/body/center/table/tbody"
popup_x_text = "/html/body/center/table/tbody/tr[2]/td"
popup_text_x_button = "/html/body/center/form/table/tbody/tr[3]/td[6]/input"

casesfound_css = "body > center:nth-child(1) > form:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > font:nth-child(1)"

#xfiles section
xfiles_original_airdate_x_front = "/html/body/font[3]/table[1]/tbody/tr[" #starts at 2
xfiles_original_airdate_x_end = "]/td[3]"
#ancient aliens section
ancient_aliens_original_airdate_x_front = ""
ancient_aliens_original_airdate_x_front = ""

#for use with selenium automated data extraction
topics = ['low in the sky','line formation','bright','green','blue','fbi was there','swat','I saw police','Angels','lights in a line','strange light','cave'] # todo iterate the entire code through this topics array.
buzzwords = ['God','Jesus','Heaven'] # these will be eliminated from results as they are automatically biased and unlikely to be credible.
odd_words = ['spouse']
Main_Cities = ['','Austin','Miami','Reno','Tinley Park','New York','Houston','El Paso']
Main_HotSpots = {'Tinley Park':['10/2004','10/2005']}
Primary_States = ['Utah','Idaho','Montana','West Virginia','New Hampshire','Maine']
Cities_to_avoid = ['Chicago']
#todo add tags for data runs that can indicate tests for things like starlink satelites.

another_search_x = "/html/body/center/form/input[1]"

#functions section
def scrollment():
    ic()
    '''
    readme
    scrolls down one page length to see invisible content.
    '''
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight-1)")

def shifty(bottom,top):
    ic()
    #ic(bottom)
    #ic(top)
    temp = 0 # init
    if bottom > top:
        temp = top
        top = bottom
        bottom = temp
    #makes lifelike shifts
    x = random.uniform(top,top+4) #init higher so that the while loop kicks in.
    while x < top and x > bottom:
        x = random.random()*float(random.uniform(0,top))
    x = round(x)
    time.sleep(x)
    #ic(x)#debug

def xpathcreator(frontend,iterator,backend):
    ic()
    xpaths_array = []
    fullxpath = ""
    '''for i in range(int(iter_start),int(iter_end)):
        fullxpath = frontend + str(i) + backend
        xpaths_array.append(fullxpath)
        fullxpath = frontend + str(i) + backend'''
    if fullxpath == "":
        fullxpath = frontend + str(iterator) + backend
    return(fullxpath)

def xfiles_spyder():

    ic()

    # this is the path to your firefox driver file
    firefox_driver = "/Users/GrahamAtWork/Documents/firefoxdriver"
    driver = webdriver.Firefox()
    url = "http://www.insidethex.co.uk/"
    print("Beginning the program sequence: ",end="")
    driver.get(url)
    print(url)
    #search page variables
    from MUFONVARIABLES import original_airdate_x_front
    from MUFONVARIABLES import original_airdate_x_end
    elems = driver.find_elements_by_tag_name('a')
    tagnumber = 2
    for elem in tqdm(range(0,len(elems))):
        href = elems[elem].get_attribute('href')
        if href is not None:
            if href.find("transcrp") > -1:
                airdate_x = original_airdate_x_front + str(tagnumber) + original_airdate_x_end
                try:
                    airdate = driver.find_element_by_xpath(airdate_x).text
                except NoSuchElementException:
                    #ic(tagnumber)
                    print("no such element")

                xfiles_script = open("MUFON_XFiles_Episodes_Scraped.txt",'a+') #opening text file in append mode
                title = elems[elem].text
                xfiles_script.write(title)
                xfiles_script.write('\n')

                this_element = elems[elem] #select this element
                this_element.click()
                time.sleep(.15)
                xfiles_script.write(airdate)
                xfiles_script.write('\n')

                #find all p tagged elements
                paragraphs = driver.find_elements_by_tag_name('p')
                p_counter = 0 #init
                for paragraph in paragraphs:
                    first_paragraph = 3 # first dial. paragraph
                    p_counter+=1 #which paragraph is it on

                    if p_counter >= first_paragraph:
                        p_text = paragraph.text
                        xfiles_script.write(p_text)

                driver.back()
                time.sleep(random.uniform(1,4))
                elems = driver.find_elements_by_tag_name('a') #refresh
                xfiles_script.write('\n')
                tagnumber+=1

                #ic(title)
    print("completed")
    xfiles_script.close()
    driver.quit()

def ancient_aliens_spyder():
    ic()
    #extract any transcripts you can from this website for ancient aliens
    # this is the path to your firefox driver file
    firefox_driver = "/Users/GrahamAtWork/Documents/firefoxdriver"
    driver = webdriver.Firefox()
    url = "https://subslikescript.com/series/Ancient_Aliens-1643266"
    print("Beginning the program sequence: ",end="")
    driver.get(url)
    #search page variables
    #from MUFONVARIABLES import ancient_aliens_original_airdate_x_front
    #from MUFONVARIABLES import ancient_aliens_original_airdate_x_end
    elems = driver.find_elements_by_tag_name('a')
    tagnumber = 2
    for elem in tqdm(range(0,len(elems))):
        href = elems[elem].get_attribute('href')
        if href is not None:
            if href.find("/episode") > -1: # if the link is a link to an episode's transcript
                #airdate_x = original_airdate_x_front + str(tagnumber) + original_airdate_x_end
                '''try:
                    airdate = driver.find_element_by_xpath(airdate_x).text
                except NoSuchElementException:
                    #ic(tagnumber)'''

                tv_show_script = open("MUFON_Ancient_Aliens_Episodes_Scraped.txt",'a+') #opening text file in append mode

                this_element = elems[elem] #select this element
                this_element.click()
                time.sleep(random.uniform(1,4))

                # now we are in the page that contains the transcript.
                title = driver.find_element_by_tag_name('h1')
                '''
                    # the title line above finds the upper heading as shown below
                    # Ancient Aliens (2009–…): Season 1, Episode 1 - The Evidence - full transcript
                '''
                real_title = title.text # extract heading
                tv_show_script.write(real_title)
                tv_show_script.write('\n')
                real_title = "" # clear up space
                title = "" # clear up space
                #tv_show_script.write(airdate)
                #tv_show_script.write('\n')

                #find all p tagged elements
                transcript = driver.find_element_by_class_name("full-script") # the transc. object
                transcript_text = transcript.text
                tv_show_script.write(transcript_text)
                driver.back()
                time.sleep(random.uniform(1,4))
                elems = driver.find_elements_by_tag_name('a') #refresh
                tv_show_script.write('\n')
                tagnumber+=1
                #ic(real_title)
    print("completed")
    tv_show_script.close()
    driver.quit()
'''
This section of the code has been adapted from the source below:
Radečić, D. (2019, October 30). Calculating String Similarity in Python. Medium. https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a
'''

def cosine_sim_vectors(vec1,vec2):
    '''
    This function has been reproduced from the source below:
    Radečić, D. (2019, October 30). Calculating String Similarity in Python. Medium. https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a
    '''
    ic()
    vec1 = vec1.reshape(1,-1)
    vec2 = vec2.reshape(1,-1)
    return cosine_similarity(vec1,vec2)[0][0]

def clean_string(text):
    '''
    This code has been adapted from the source below:
    Radečić, D. (2019, October 30). Calculating String Similarity in Python. Medium. https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a
    '''
    ic()
    try:
        text = ''.join([word for word in text if word not in string.digits])
    except TypeError:
        text = "N/A"
    if text != "N/A":
        text = ''.join([word for word in text if word not in string.punctuation])
        text = text.lower()
        text = ' '.join([word for word in text.split() if word not in stopwords])
    else:
        text = "N/A"
    return text

def Levenshtein_Similarity(phrases):
    '''
    This code has been adapted from the source below:
    Radečić, D. (2019, October 30). Calculating String Similarity in Python. Medium. https://towardsdatascience.com/calculating-string-similarity-in-python-276e18a7d33a

    ADAPTATIONS
    phrases is passed to the function and x number of phrases are analyzed to determine their similarity scores.
    this can be iterated to find the most similar reports.

    '''
    ic()
    from nltk.corpus import stopwords
    stopwords = stopwords.words('english') # the stop words are english only
    #?sentences = ['this is my mother','that is your mother','Jim has no father']
    sentences = phrases # save the phrases to compare in this variable.
    cleaned = list(map(clean_string, sentences))
    #ic(cleaned)

    vectorizer = CountVectorizer().fit_transform(cleaned)
    vectors = vectorizer.toarray()
    #ic(vectors)

    csim = cosine_similarity(vectors)
    #ic(csim)

    csimilarity = cosine_sim_vectors(vectors[0],vectors[1])
    #ic(csimilarity)
    return csimilarity
'''
end of adapted section from Radečić (2019)
'''

def my_next_step(driver):
    ic()
    driver.refresh()
    time.sleep(10)
    element=driver.switch_to_frame('iframe')

def wordstemmer(description_string):
    ic()
    # will be used to find the stems of the words in all comments
    words = description_string.split(" ")# extract all words from the string
    print(words)
    ps = PorterStemmer()
    for word in words:
        print(ps.stem(word))

def transcript_parser(transcript_file,heading_text):
    '''
    README
    transcript_file contains "file_name.txt" for example as a string.
    newfilename = "Scrubbed_" added to the filename and will be saved as a txt file
    heading_text should contain text that recurrs in the text file as a heading that you want
    to split into sep. records.

    '''
    ic()
    heading_text = str(heading_text) # data validation step
    newfilename = "" #init
    myfile = open(transcript_file,'r') # open transcript read only
    newfilename = "MUFON_scrubbed_" + transcript_file
    outfile = open(newfilename,'w')
    new_item_line = "" #init
    for item in tqdm(myfile):
        endofline = 0 # init
        new_item = "" # init and reset for every iteration
        if item.find(heading_text)>-1: # in the heading of the transcript
            outfile.write(new_item_line) # save the current episode
            outfile.write('\n') # new episode
            outfile.write(item)
            new_item_line = "" #reset the newline variable
        else: #in the body of the transcript not the heading
            if item.find("\n") > -1:
                endofline = item.find("\n")
                for i in range(0,endofline): #scan the line
                    if item[i] != '\n': #
                        new_item = new_item + item[i]
                    else:
                        #ic(new_item)
                        continue
            else: #there was a newline found
                new_item = item
                #ic()
        #ic(item)
        #ic(new_item)
        new_item_line = new_item_line + new_item

    outfile.close()
    myfile.close()
    print("cleaned up the ",transcript_file," file and saved in new location --> ",newfilename)

def initializer(download_choice,scrape_more):
    '''
        README
            scrape_more can either be Y, y, N, or True
            download_choice is to download the xfiles again as well as ancient aliens
    '''
    ic()
    #ic(download_choice)
    #ic(scrape_more)
    if download_choice == True:
        xfiles_spyder() # extract xfiles transcripts
        ancient_aliens_spyder() # extract the transcripts of ancient aliens show. This will be saved to MUFON_Ancient_Aliens_Episodes_Scraped.txt
        transcript_parser("MUFON_Ancient_Aliens_Episodes_Scraped.txt","ANCIENT ALIENS")
    else:
        print("transcripts have been downloaded\nChecking updated MUFON Reports Database for Quality")
        transcript_parser("MUFON_Database_Scraped_Reports.txt",'Long Description of Sighting Report')
        #ic()
    if scrape_more == "NO" or scrape_more == False or scrape_more == "n" or scrape_more == "N":
        return 0 #does go here so that's working...
    elif scrape_more == 'y' or scrape_more == 'Y' or scrape_more == True:
        print("crawling for more data")
        selenium_crawler(topics,Main_Cities,Primary_States,Main_HotSpots,Cities_to_avoid)
    else:
        #ic()
        print("major issues...")

def selenium_crawler(topic,city,states,mainhotspots,citiestoavoid):
    PRESET_VARIABLE_MAX = 30
    '''mufon_file = open("MUFON_Database_Scraped_Reports.txt",'a+') #opening text file in append mode
    mufon_file.write(timestamp_string)
    mufon_file.close() # save progress in the file and reopen it later'''
    topic

    #search page variables
    from MUFONVARIABLES import nearest_city_field_x
    from MUFONVARIABLES import event_stateusa_x
    from MUFONVARIABLES import keywordfield_x
    from MUFONVARIABLES import date_of_event_x
    from MUFONVARIABLES import submit_button_x


    topics = [topic] # for continuity
    maincities = [city]  # for continuity
    low = 3
    high = 15 # maximum loaded (items on the page) at one time
    highest = PRESET_VARIABLE_MAX
    k = 0 # init
    wallace = 0
    richard = 0 #init
    #?city in primarycities
    # this is the path to your firefox driver file
    firefox_driver = "/Users/GrahamAtWork/Documents/firefoxdriver"
    driver = webdriver.Firefox()
    url = "https://mufoncms.com/cgi-bin/report_handler.pl?req=search_page"
    print("Beginning the program sequence: ",end="")
    driver.get(url)
    #ic(topic)
    #ic()
    #critical section to fool the website. Need speed of use to mimic human and not trigger attention.
    if topic != topics[0]: #skip first iteration
        wallace = random.uniform(1,20)
        richard = random.uniform(25,60)
        print("waiting between ",wallace, " and ",richard, 'seconds...')
        shifty(wallace,richard)

    keywordfield = driver.find_element_by_xpath(keywordfield_x)
    date_of_event_field = driver.find_element_by_xpath(date_of_event_x)
    nearest_city_field = driver.find_element_by_xpath(nearest_city_field_x)
    event_state_field = driver.find_element_by_xpath(event_stateusa_x)
    submit_button = driver.find_element_by_xpath(submit_button_x)
    keywordfield.send_keys(topics[k])

    shifty(1,random.uniform(2,4)) # act humanish
    nearest_city_field.send_keys(city)
    shifty(1,2)
    nearest_city_field.send_keys(Keys.RETURN)
    #event_state_field.send_keys(state)
    #shifty(2,3)
    #?submit_button.click()
    shifty(1,3)


    front_elements = [date_sub_x_front,date_time_front,sdescr_front,location_of_event_front,attachments_front,description_css_front]
    end_elements = [date_sub_x_end,date_time_end,sdescr_end,location_of_event_end,attachments_end,description_css_end]

    descriptions = [] #init
    print("waiting till button is visible")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, casesfound_css)))
    descriptions = driver.find_elements_by_class_name("button") #save 52 buttons to this array to be clicked and extracted in order.
    pagerows = len(descriptions) # this should equal 52 but this step prevents breakage at this point.
    window_before = driver.window_handles[0] # identifies the id of the window with the search results for navigating back later on.
    print("searching for phrase:",topic," and nearest the city:",city) # topic is the referenced "topic" from the uppermost array: "topics"
    #ic()
    topicstring = topic + ',' #will go in first column of csv

    for k in tqdm(range(3,pagerows)):# following the xpath pattern on the page going down each the number of rows on the page.
        #ic(k)
        mufon_file = open("MUFON_Database_Scraped_Reports.txt",'a+')
        mufon_file.write(topicstring)

        front = "" # init and reset every iteration
        back = "" # init and reset every iteration
        inner_string = "" # init and reset every iteration

        for index in range(1,len(front_elements)+1): # go through [description_x_front,date_sub_x_front,date_time_front,sdescr_front,location_of_event_front,attachments_front]
            #ic(index)
            full_path_x = "" # init and reset every iteration
            # generate the xpath
            # in the third line down the 3 is unchanging while the 2 changes every iteration of this inner loop
            front = front_elements[index-1]
            back = end_elements[index-1]
            full_path_x = front + str(k) + back # /html/body/center/form/table/tbody/tr[3]/td[2] for example.
            #ic(full_path_x)
            # extract the contents of the field
            if index != 6: # is other column besides descr.
                field_contents = driver.find_element_by_xpath(full_path_x).text
                #ic()

            # special case: long description field has a button to click first.
            if index == 6: # index = 6 is a clickable button.
                field_text = "" # init and reset
                field_contents = descriptions[k] # should allow the browser to access the popup window
                try:
                    field_contents.click()
                    time.sleep(.25)
                except Exception:
                    driver.quit()
                    #ic()
                    field_contents = "n/a" # save nothing in the field
                shifty(1,2) # pause for a moment then check field contents too see if click was successful above
                if field_contents != "n/a": #means the button was clicked
                    #get current window handle
                    p = driver.current_window_handle
                    #get first child window
                    window_handles = driver.window_handles
                    for w in window_handles:
                        #switch to child window
                        if(w!=p):
                            driver.switch_to.window(w)
                            break
                    shifty(.5,1)
                    el = driver.find_element_by_tag_name('body')
                    #print(el.text[0:30])
                    field_text = el.text
                    inner_string = inner_string + "ø" +str(field_text) # the delimeter is the ø (option o) symbol for this csv file.
                    #ic()
                    # if any error or any exception is flagged then this trips
                p = driver.current_window_handle
                driver.close()

                driver.switch_to_window(window_before)
                shifty(.5,1) # patience...
                descriptions = driver.find_elements_by_class_name("button") #refresh the descriptions array
            else:
                # all other indices
                new_field = "" #init
                field_contents2 = str(field_contents)
                fields = ""
                for i in field_contents:
                    if i != ',' and i != '\n': # remove all commas
                        fields += i
                    else:
                        fields += " "
                field_contents = fields
                if field_contents.find("\n") < len(str(field_contents2)) and field_contents.find("\n")>-1:
                    new_field = field_contents2[0:field_contents2.find("\n")] + " " + field_contents2[field_contents2.find("\n")+1:len(field_contents2)]
                    inner_string = inner_string + "ø" +str(new_field) # the end of record delimiter is the end of line character
                else:
                    # if the index is one less than length then the program is looking at the last field (attachments field)
                    if index < len(front_elements)-1:
                        inner_string = inner_string + "ø" +str(field_contents2) # the delimeter is the ø symbol for this csv file.
                    else:
                        inner_string = inner_string + "ø" +str(field_contents2) # the end of record delimiter is the end of line character
        #ic()
        #print(inner_string) #debugging in the terminal window


        # now inner_string contains the data from the row in string format
        # it can now be saved to the file as a new line
        #inner_string += "ø" + timestamp_string
        #ic(inner_string)
        fields = ""


        for i in inner_string:
            if i != ',' and i != '\n': # remove all commas
                fields += i
            else:
                fields += " "
        #now with no commas sub commas in place of delimiters
        #ic(fields)

        if fields.find(",")>-1 and len(fields)<=len(inner_string):
            #ic()
            print("success")
        fields_ofgrain = ""

        for i in fields:
            if i != 'ø': # remove all commas
                fields_ofgrain += i # add to fields if not a ø
            else:#ic(i)
                fields_ofgrain += ","
        mufon_file.writelines(fields_ofgrain[1:]) # save the row
        mufon_file.write('\n')
	  time.sleep(10)
        #shifty(1,3) #add randomness like a human
        mufon_file.close()
    driver.close()

def corpora_sherlock(text_file,delimeter_used):
    '''
        README
            takes in a text file and creates a csv file
            (textfile,delimeter_used) for this case will be 'ø' this is option + o
    '''
    ic()
    newfilename = "" #init
    myfile = open(text_file,'r') # open transcript read only
    newfilename = "MUFON_Sherlocked_" + text_file
    outfile = open(newfilename,'w')
    myfile = myfile.read()
    print(myfile[0:200])
    fieldtext = "" #init
    fields = "" #init
    linetext = "" #init

    counter = 0 # init
    columns = 12
    rows = myfile.count("øøø") # how many rows of data will there be?
    #ic(rows)
    #initialize matrix
    reports = [ '' for i in range(rows)]

    matrix_index = 0 # will be the record id in the matrix
    column_id = 0 # init
    reportsline =  [ '' for i in range(columns)]# holds each row of the matrix

    for i in tqdm(range(0,len(fields))):
        if fields[i] == 'ø': # this is a new field "2021-03-15"
            #reportsline[column_id] = [linetext] # add these into the matrix later
            column_id += 1 # this column id will increment by 1
            counter+=1 # if goes above 3 there is a new record.
            if counter == 3:
                column_id = 0 # go back to the first column
                reports[matrix_index] = reportsline
                reportsline = [] #reset
                matrix_index += 1 # go to next row of the matrix
                #ic(linetext)
                outfile.write(linetext)
                linetext = ""
                counter = 0 #reset
            else:
                linetext = linetext + ',' + fieldtext
                fieldtext = "" #reset the field text
        else:
            counter = 0 # reset counter that counts the number of ø it sees in a row.
            fieldtext += fields[i]

        #ic(reports)
        #print(reports[10][1])
        #print(reports[23][4])
        #ic(myfile[i])
    outfile.close()

#*topics = 'lights'
city = 'Orlando'
#*selenium_crawler(topics,city,Primary_States,Main_HotSpots,Cities_to_avoid)
#selenium_crawler(topics,Main_Cities,Primary_States,Main_HotSpots,Cities_to_avoid)
#corpora_sherlock("Scrubbed_MUFON_Database_Scraped_Reports.txt",'ø')
'''
Cape Canaveral Space Force Station
WASHINGTON — SpaceX successfully launched another set of Starlink satellites Feb. 4 in the first of back-to-back Falcon 9 launches scheduled from Cape Canaveral. The Falcon 9 rocket lifted off at 1:19 a.m. Eastern from Space Launch Complex 40 at Cape Canaveral Space Force Station.
'''
#!unused function
def convert_csv_to_dict(filename):
    ic()
    #adapted from reading and writing CSV Files in Python Website
    import csv
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        #print(f'\t{row["city"]} , {row["state_name"]} is located at {row["lat"]} {row["lng"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')
    #ic(csv_reader)
    return csv_reader

def convert_csv_to_pandas(filename,indexcolumn):
    ic()
    #df = pandas.read_csv(filename)
    df = pd.read_csv(filename, index_col=indexcolumn)

    return df

def write_to_csv_from_pandas(df_name,new_file_name):
    ic()
    import pandas
    #ic("NOT COMPLETED YET... CHECK THIS FUNCTION BEFORE IMPLEMENTATION")
    df = pandas.read_csv('hrdata.csv',
                index_col='Employee',
                parse_dates=['Hired'],
                header=0,
                names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    newfilename += ".csv"
    df.to_csv(newfilename)

#convert csv file to pandas df
#todofilename = "MUFON_uscities.csv"
#todocities_df = convert_csv_to_pandas(filename)
# saved with cityname as index column

#todo this function is working properly and gives coordinates of cities if available.
def finding_nemopolis_old(city_name,state_name,cities_df,cities2_df):
    ic()
    #test dictionary
    #print("testing Austin,TX in df: ",end="")
    # Check whether city is in the dictionary and print feedback
    #first check main one
    from operator import indexOf
    Mode2 = False #state id mode
    if len(state_name) == 2:
        Mode2 = True
        #ic()

    null_array = ['','','','']

    if city_name not in cities_df['city_ascii']:
        if city_name not in cities2_df['city_ascii']:
            try:
                null_array = ['','','','']
                #ic(cities2_df[city_name])
            except KeyError:
                null_array = [city_name,state_name,'n/a','n/a']
                return null_array
            return null_array
        else:
            cities_df = cities2_df # go with the second option
            null_array = [city_name,state_name,'n/a','n/a']

    #then check mufon 2014 us cities with no state id and find result
    #ic()
    if Mode2 == False: #state names
        line_count = 0 #init
        location_data = [] #init
        null_array = [city_name,state_name,'n/a','n/a']
        for row in tqdm(range(0,len(cities_df['city_ascii']))):
            if cities_df['city_ascii'][line_count] == city_name and cities_df['state_name'][line_count] == state_name:
                #print(cities_df['city_ascii'][line_count],", ",cities_df['state_name'][line_count]," located: ",cities_df['lat'][line_count]," ",cities_df['lng'][line_count])
                location_data = [cities_df['city_ascii'][line_count],cities_df['state_name'][line_count],cities_df['lat'][line_count],cities_df['lng'][line_count]]
                #ic("returning")
                #ic(location_data)
                return location_data
            else:
                #ic("else")
                location_data = [] # remains null
                if row > len(cities_df['city_ascii']):
                    location_data = geopy_city_to_coordinates[city_name,state_name]
                    return location_data
            line_count += 1
    else:
        line_count = 0 #init
        location_data = [] #init
        null_array = [city_name,state_name,'n/a','n/a']
        loc = np.nonzero(np.in1d(cities_df['city_ascii'], city_name))[0]
        loc = np.nonzero(np.in1d(cities_df['city_ascii'], city_name))[0]
        iterator = 0 #init
        for row in tqdm(range(0,len(loc))):
            intersection_x = []
            intersection_y = []
            var0 = []
            var1 = []
            x = np.array(cities_df['city_ascii'])
            y = np.array(cities_df['state_id'])
            intersection_x = np.where(x == city_name)
            intersection_y = np.where(y == state_name)
            intersection = np.intersect1d(intersection_x,intersection_y)
            intersection_bool = np.in1d(intersection, intersection_y)
            resultant = np.nonzero(np.in1d(intersection, intersection_y))
            var0 = intersection_y
            if len(intersection)>0:
                var1 = np.where(var0 == intersection[0])
                #print(var1[1][0])
                truevar = var1[1][0]
                var = intersection[0]
                #print(intersection[0], " and ",intersection_y[0][truevar])
                city_loc = intersection[0]
                state_loc = intersection_y[0][truevar]
                location_data = [cities_df['city_ascii'][city_loc],cities_df['state_id'][city_loc],cities_df['lat'][city_loc],cities_df['lng'][city_loc]]
                return location_data
            else:
                #ic()
                location_data = geopy_city_to_coordinates[city_name,state_name]
                return location_data
    return null_array # no coordinates found.

#todo this function works and finds distance between two points given in the df format returned by finding_nemopolis
#todo: ['Austin', 'Texas', 30.3004, -97.7522]
def chasm_between(point1,point2):
    ic()
    import geopy.distance
    from geopy import distance
    coords_1 = (point1[2], point1[3])
    coords_2 = (point2[2], point2[3])

    dist = geopy.distance.distance(coords_1, coords_2).mi
    return dist

#todo julian date converter (complete)
def tojulian(day,month,year):
    '''
    README
        dd/mm/yyyy
    '''
    ic()
    #* https://stackoverflow.com/questions/13943062/extract-day-of-year-and-julian-day-from-a-string-date
    import datetime
    import jdcal
    fmt = '%m.%d.%Y'
    s = str(month) + "." + str(day) + "." + str(year)
    dt = datetime.datetime.strptime(s, fmt)

    julian_day = sum(jdcal.gcal2jd(dt.year, dt.month, dt.day))

    return julian_day

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
def city_finder(city_name,state_name):
    #coordinates data provided by https://simplemaps.com/data/us-cities.
    #see their website for more details.
    #finds coordinates of city


    '''geolocator = Nominatim(user_agent="mufon_scanner")
    location = geolocator.geocode("175 5th Avenue NYC")
    print(location.address)

    print((location.latitude, location.longitude))
    print(location.raw)
    #{'place_id': '9167009604', 'type': 'attraction', ...}
    #from geopy.distance import geodesic
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    print(geodes#ic(newport_ri, cleveland_oh).miles)
    #538.390445368

    df = pd.DataFrame({'name': ['paris', 'berlin', 'london']})

    #from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    #from geopy.extra.rate_limiter import RateLimiter
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1) #keeps my ping within respectful range
    tqdm.pandas()
    df['location'] = df['name'].progress_apply(geocode)
    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    import concurrent.futures

    geolocator = OpenMapQuest(api_key="...")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1/20)

    with concurrent.futures.ThreadPoolExecutor() as e:
        locations = list(e.map(geocode, search))
    '''

def city_extraction(string):
    ic()
    string_spaces = 0
    s_iters = []
    string_commas = 0
    c_iters = []
    iterator = 0
    for i in string:
        if i == ' ':
            string_spaces +=1
            s_iters.append(iterator)
        if i == ',':
            string_commas +=1
            c_iters.append(iterator)
        iterator += 1

    #blinding,2021-03-13,2010-08-14 9:15PM,it was a bright blue light flying over head,Bogalusa LA US,,Long Description of Sighting Report Driving home at dark we’re on a new road that boarded Ft Knox KY. Three huge brights started descending towards us. I thought it was an airplane though all we could see were these blinding lights. I said that I thought it was going to land on us. Then it was stationary over the road. Two more light turned on on either side of the three. Then as in one second they simultaneously darted down to the side I’d the road and all lights and evidence of it was gone. In the daytime I looked at spot where they went down and it was a depression of weeds and tree saplings. It bordered on Ft Know property line. It wasn’t until years later I realized there was no sound. In fact I felt numb after seeing it. Content-type: text/html
    #count commas
    commas = 0 # init
    spaces = 0 # init
    end_of_loc = string.find(',')
    if end_of_loc == -1:
        end_of_loc = len(string)
        mode = 2
    loc_string = "" # holds Bogalusa LA US
    iterator = 0

    if mode == 1:
        #ic(mode)
        for i in string:
            if iterator < end_of_loc:
                if i == ",":
                    commas+=1
                if commas == 4:
                    if i != ' ':
                        loc_string += str(i)
                    elif i == ' ' and spaces < 1:
                        loc_string += ','
                        spaces += 1
                        #ic(spaces)
                        #ic(i)
                    else:
                        #ic(spaces)
                        #ic(i)
                        continue
                if spaces == 5:
                    return loc_string #exit with the string saved
                iterator+=1
            else:
                return loc_string[1:] #returns city,Statecode (i.e. Austin,TX)
    if mode == 2:
        #ic(mode)
        iterator = -1 # init one lower to compensate for line beneath for i in string  below.
        for i in string:
            iterator+=1
            nothing = 0
            if iterator in c_iters:
                nothing = 1
                #comma was in string
                #ic('comma found in mode 2')
            else:
                continue
            if iterator in s_iters:
                loc_string += str(',')
            if iterator in s_iters and iterator < len(string):
                #space was in string and we are on the last space before state code
                loc_string += str(',')
            else:
                loc_string += str(i)

def writetofile(text,filename):
    ic()
    outfile = open(filename,'w+')
    outfile.write(text)
    outfile.close()

def city_cleaner(filename):
    ic()
    csv_data = pd.read_csv(filename)
    #csv_data.head()
    new_locations = []
    for location in csv_data['Location of Event']:
        new_location = city_extraction(location)
        #ic(new_location)
        new_locations.append(new_location)

    df = pd.read_csv(filename)
    df["Optimized Location"] = new_locations
    df.to_csv(filename, index=False)

def plotly_project():
    ic()
    #Final Project - RSAN 130 - Plotly Visualizations
    import re
    import string
    import time
    import os.path
    import numpy as nmp
    import numpy as np
    import pandas as pd
    import matplotlib
    from tqdm import tqdm
    from tqdm import tqdm_gui
    import plotly.express as px
    import plotly.graph_objects as go
    import datetime
    import csv

    #! multi plot
    import csv
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    ThisDay = 1 #! this holds the day of the week for each column
    fig = make_subplots(rows=7, cols=6, start_cell="top-left",x_title='Your master x-title',
                        y_title='Your master y-title',
                        subplot_titles = [f'Title_{i+1}_{j+1}' for i in range(10) for j in range(2)])
    #!init for the figure with 7 rows and 6 columns
    row = 1
    col = 1
    groupsize = 100 #how large the buckets are
    data = list(csv.reader(open("nycpartyupd.csv")))
    lat = pd.read_csv("nycpartyupd.csv", index_col="Latitude")
    #!lat holds the latitudes column
    long = pd.read_csv("nycpartyupd.csv", index_col="Longitude")
    #!long holds the longitudes column
    barlat  = list(csv.reader(open("bar_locations.csv")))
    BXArray = []#* holds the x coordinate arrays for the bars
    BYArray = []#* holds the y coordinate arrays for the bars
    BCArray = []#* holds the y coordinate arrays for the number of calls at these bars
    i = 0
    j = 0
    for i in tqdm(range(0,len(barlat))): #saving these values for graphing later
        # go down list of bars
        BXArray.append(barlat[i][4])
        BYArray.append(barlat[i][5])
        BCArray.append(barlat[i][6])
        #? 4 and 5 are coordinates and 6 is the number of calls to police

    #!these arrays are for later sections in the code
    CombArrays=[]#! this will hold the comb scores for each iteration of the whileloops below
    XArrays = []
    YArrays = []
    XAxis_Max = 0 # this variable tells what the maximum of the x axis coordinates is
    XAxis_Min = 0 # this variable tells what the minimum of the x axis coordinates is
    YAxis_Max = 0 # this variable tells what the maximum of the y axis coordinates is
    YAxis_Min = 0 # this variable tells what the minimum of the y axis coordinates is

    #! more storage arrays
    xbounds = [] #holds tuples with upper and lower bounds for the x axis on muliple graphs
    ybounds = []
    TimeArrays = [] #will hold event times for analysis
    #!end

    bucket = 0 #size limiter

    while row<8:#! through the days

        while col<7:#!through the locations
            XArray = []#* holds the x coordinate arrays
            YArray = []#* holds the y coordinate arrays

            TimeArray = []#* holds time of day when event occurred
            CombArray = []#* holds the combined rrt score for this day


            #! this row will have six plots side by side.
            day = 0 #? holds a certain row in a certain column
            record = 0 #? this holds length of the whole list of records
            #? https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/


            #! the relevant indeces are: [0][] is the records column and [][4] is the Day of Week Column
            rec = "" #! init
            #?obtaining the coordinates columns
            for record in range(1,len(data)):#for all of the records...

                #! rec can now be used to search
                rec = int(record)
                #print("rec->",rec," day=",day," data[rec][2]=",data[int(rec)][2])
                #print("record:",record)

                day = data[rec][4]# ! day will hold the day of the week

                if int(day) == int(ThisDay): #! if the day matches the current day of the week then save the
                    #!coordinates to the X and Y arrays to be graphed are stored in XArray and YArray
                    if bucket == groupsize:#? if the current bucket is the same size as groupsize then move forward
                        if data[rec][2] != 0 and data[rec][2] != "0" and data[rec][3] != 0 and data[rec][3] != "0": #and grouper==groupsize:
                            XArray.append(data[rec][2]) #! saves the latitude of that record to the XArray to be graphed
                            YArray.append(data[rec][3]) #! saves the longitude of that record to the YArray to be graphed
                            XArrays.append(data[rec][2]) #! saves the latitude of that record to the XArray to be graphed
                            YArrays.append(data[rec][3]) #! saves the longitude of that record to the YArray to be graphed
                            CombArray.append(data[rec][30]) #! saves the value of COMB_AVGRRT combined average reponse time
                            CombArrays.append(data[rec][30]) #! saves the value of COMB_AVGRRT combined average reponse time
                            TimeArray.append(data[rec][13]) #! saves time of event to array: TimeArray
                            TimeArrays.append(data[rec][13]) #! saves time of event to array: TimeArrays


                            if float(data[rec][2])>float(XAxis_Max): #? these if statements show the bounds of the x and y coordinates
                                XAxis_Max = data[rec][2]
                            if float(data[rec][3])>float(YAxis_Max):
                                YAxis_Max = data[rec][3]
                                print("[",YAxis_Max,"],",record,end=",")# todo: erase this debug step
                            if float(data[rec][3])<float(YAxis_Min):
                                YAxis_Min = data[rec][3]
                            if float(data[rec][2])<float(XAxis_Min):
                                XAxis_Min = data[rec][2]
                            bucket = 0 #! reset the bucket value
                    else:
                        bucket+=1
                        continue
                else:
                    #print("*",end="") # debugging tool
                    continue
                #!save the bounds
                xbounds.append([XAxis_Min,XAxis_Max])
                ybounds.append([YAxis_Min,YAxis_Max])
            #!Now the X and Y arrays are plottable and a trace can be added to the figure.

            fig.add_trace(go.Scatter(x=XArray, y=YArray,mode="markers"), row=row, col=col)
            fig.add_trace(go.Scatter(x=BXArray, y=BYArray,fillcolor = '#ff0000',mode="markers",marker_symbol='x'), row=row, col=col)

            print("||||",col,",",row,"||||    ",end="") #! for visual reference
            col+=1

        col=1


        ThisDay+=1 #! Goes to the next day of the week
        print("")
        row+=1

    fig.update_layout(title_text="New York Noise Complaints by Geography")
    fig.update_yaxes(automargin=True)




    fig2 = px.density_heatmap(x=XArrays, y=YArrays) #! holds heatmap comparing the x coordinates to the y coordinates
    fig2.show()

    # Update xaxis properties
    '''for i in range(0,7):
        for j in range(0,6):
            title = "xaxis title"
            ytitle = "yaxis title"
            print('fig.update_xaxes(title_text="',title,'", row=',i,' col=',j,')')
            print('fig.update_yaxes(title_text="',ytitle,'", row=',i,' col=',j,')')
        '''
    fig.update_xaxes(title_text="xaxis 1 title", row=1, col=1)


    # Update title and height
    fig.update_layout(title_text="Customizing Subplot Axes", height=700)

    fig.show()

def city_csv_to_location(filename):
    ic()
    coordinates_dict = {'Bogalusa/LA':['Bogalusa', 'LA', 30.7812, -89.8633]}
    cities_df = convert_csv_to_pandas("MUFON_uscities.csv","city")
    cities2_df = convert_csv_to_pandas("MUFON_2014_Cities_updated.csv","city")
    cities_df.head()

    csv_data = pd.read_csv(filename)
    #csv_data.head()
    new_locations = []
    csv_data_states = []
    coordinates = []
    for i in range(0,len(csv_data)):
        csv_data_states.append(csv_data['state_id'][i])
    #ic(csv_data_states)
    iterator = 0
    spot = ['','','','']
    for location in csv_data['city_ascii']:
        new_location_city = location
        new_location_state = csv_data_states[iterator]
        new_location = location + "," + new_location_state[0:2]
        spot = finding_nemopolis(new_location_city,new_location_state[0:2],cities_df,cities2_df)
        city_state = location + "/" + new_location_state[0:2]
        coordinates_dict[city_state] = spot
        coordinates.append(spot)
        #ic(new_location)
        #new_locations.append(new_location)
        print(coordinates_dict[location + "/" + new_location_state[0:2]])
        iterator +=1
    #now find coordinates

    '''for city_state in tqdm(new_locations):
        dory_bull = city_state.split (",") #splits string into array city,state to [city,state]
        spot = finding_nemopolis(dory_bull[0],dory_bull[1])
        coordinates.append(spot)'''
    return coordinates_dict

def save_dict_as_csvfile(dict_name):
    ic()
    filename = 'MUFON_' + str("dictionary") + '.csv'
    with open(filename, 'w+') as f:
        for key in dict_name.keys():
            f.write("%s,%s\n"%(key,dict_name[key]))

#*coordinates = city_csv_to_location("citiestocheck.csv")
#*save_dict_as_csvfile(coordinates)
#writetofile(coordinates,"MUFON_dictionary_cities_locations.csv")
#ic()

#todo function to get closest "n" reports to a report (report_i) based on the location of report_i

def Jones_Effect(point_x,dataset):
    '''
    README
    Q is len(dataset)/(2) round down so for len(dataset) = 1203 the Q =  1203/2 = 601.5 round down to 601
    find the Q closest points by longitude
    find the Q closest points by latitude
    find which points occur in both sets
    get their distances
    point_x = the dataframe below
    Date/Time of Event  date posted city    state   country latitude    longitude   Description shape   duration (seconds)
    10/10/49 20:30      4/27/04   san marcostx        us    29.8830556  -97.9411111         cylinder     2700

    Topic   Date Submitted  Date/Time of event  Short Description   Location of Event length    upper   Long Description    Attachments705  DRIVING HOME AT DARK WE’RE ON A NEW ROAD THAT BOARDED FT KNOX  KY.
    blinding    3/13/21 2010-08-14 9:15PM   it was a bright blue light flying over head Bogalusa   LA  US

    '''

    #will call distance functions and lat long from findingnempolis function
    dataset

#todo function to get the closest "n" reports to a report (report_i) based on date of event

#todo function to compare the text of a report A with a report B and give similarity

#todo function to generate the value of a report_i given the similarity of their description to others in the area

#todo use geopy to find coordinates of cities mentioned in the reports and return those
#todo cities' coordinates, google rated importance, and bounding box for lat and longitude.
def geopy_city_to_coordinates(cityname,statename):
    '''
    README
    city name must be like "Austin"
    statename must be in form "Texas"
    no spaces they will be combined with space between them
    '''
    inputstring = cityname + " " + statename
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(inputstring)
    print(location.address)
    print(location.raw)
    #coordinates = [0,0]
    coordinates = [location.point[0],location.point[1]]
    other_city_data = [location.raw['importance'],location.raw['boundingbox']]
    returnable_array = [coordinates,other_city_data] # [[lat,long],[importance,boundingbox]
    return returnable_array
'''
    result: [[30.2711286, -97.7436995],[0.8694265717866669,['30.0984576', '30.5166255', '-97.9367663', '-97.5605288']]]
'''
#todo this function is working properly and gives coordinates of cities if available.
def finding_nemopolis(city_name,state_name):

    location_data = ['']
    if len(state_name)>2:
        location_data = geopy_city_to_coordinates(city_name,state_name)
    else:
        return location_data
    return location_data # no coordinates found.
result = geopy_city_to_coordinates("Austin","Texas")
var = finding_nemopolis("Austin","Texas")
ic(var)
ic(result)





#city_text = city_extraction("blinding,2021-03-13,2010-08-14 9:15PM,it was a bright blue light flying over head,Bogalusa LA US,,Long Description of Sighting Report Driving home at dark we’re on a new road that boarded Ft Knox KY. Three huge brights started descending towards us. I thought it was an airplane though all we could see were these blinding lights. I said that I thought it was going to land on us. Then it was stationary over the road. Two more light turned on on either side of the three. Then as in one second they simultaneously darted down to the side I’d the road and all lights and evidence of it was gone. In the daytime I looked at spot where they went down and it was a depression of weeds and tree saplings. It bordered on Ft Know property line. It wasn’t until years later I realized there was no sound. In fact I felt numb after seeing it. Content-type: text/html")
#ic(city_text)
'''loc_data = finding_nemopolis('Austin','Texas')
loc_data2 = finding_nemopolis('San Diego','California')
#ic(loc_data)
#ic(loc_data2)
distance = chasm_between(loc_data,loc_data2)
#ic(distance)
#ic(loc_data)
#ic()'''
#?city_cleaner("MUFON_Database_Scraped_Reports.csv")

#todo find coordinates for the cities
'''coordinates_file = open("citiescoordinates.txt","w+")
coordinates_file.write("city,state_id\n")
coordinates_file.close()
cities = open("citiestocheck.csv",'r')
commas = 0
newcity = ""
newstate = ""

for city in tqdm(cities):
    if city != "\ufeffcity, state_id\n":
        coordinates_file = open("citiescoordinates.txt","a+")
        coordinates = "" # init and reset
        for i in city:
            if i == ',':
                commas += 1
            else:
                if commas == 0:
                    newcity += i
                else:
                    if i != ' ' and i != '\n':
                        newstate += i
                    else:
                        continue
        try:
            #ic(newcity)
            #ic(newstate)
            coordinates = finding_nemopolis(newcity,newstate)
        except Exception:
            #ic(city)
            nothing = 1
        if coordinates != "":
            coordinates_file.write(coordinates)
        newcity = ""
        commas = 0 #reset
        newstate = ""
        coordinates_file.close()

'''
def point_finder(R_x,R_y):
    '''
    README
    R_x =
    R_y =
    M_x =
    M_y =
    file headers are below
    Source,Date/Time of Event,date posted,duration (seconds),city,state (ABBR),STATE(FULL),country,latitude,longitude ,comments,shape, ,,,
    '''
    import pandas as pd
    csvfilename = "NUFORC_CONSOLIDATED_DB.csv"
    data_file = open('/Users/GrahamAtWork/Documents/Automate-with-Python-_-Form-Filling-Script-/TextTester/NUFORC_CONSOLIDATED_DB.csv')
    write_file = open("POINTSOFINTEREST.csv","a+")
    df = pd.read_csv(csvfilename,usecols = [0,1,2,8,9])
    #now parse
    R_x = 0
    R_y = 0
    points_of_interest = []
    iterator = 0 #Init
    bounds = 0.5 # preset boundaries for significance
    for R in df[0]:
        if R == "MUFON": #source is mufon
            R_x = R[8] #get latitude for the report
        iterator += 1 # what row number the report is on
    for i in range(0,len(df)): # parse the other reports from NUFORC and MUFON
        if i != iterator: # for all other records
            lat = df.loc[i]['latitude'] #check latitude
            if lat > R_x-bounds and lat < R_x + bounds: #if latitude is within bounds of R_x latitude then check longitude
                lng = df.loc[i]['longitude']
                if lng > R_y-bounds and lng < R_y + bounds:
                    points_of_interest.append(df.loc[i]) # save the record as within the range
    write_file.write(points_of_interest)
    data_file.close()
    write_file.close()
    return points_of_interest

results = point_finder(30.2711286,-97.7436995)
ic(results)
