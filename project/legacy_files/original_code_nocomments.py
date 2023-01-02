
from tqdm import tqdm
from tqdm import tqdm_gui
import time
import datetime
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
import re
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

maincontrols_tab_dateyear_id = "date_year"
maincontrols_tab_datemonth_id = "date_month"
maincontrols_tab_dateday_id = "date_day"
maincontrols_tab_time_hour_id = "time_hour"
maincontrols_tab_time_minute_id  = "time_minute"
maincontrols_tab_time_second_id = "time_second"
maincontrols_tab_fieldofview_id = "view_fov"
location_tab_id = "ui-id-21"
location_tab_latitude_id = "loc_latitude"
location_tab_longitude_id = "loc_longitude"
location_tab_altitude_id = "loc_altitude"
location_tab_name_id = "loc_name"
timejump_tab_id = "ui-id-10"
location_tab_latitude_id = "loc_latitude"
location_tab_longitude_id = "loc_longitude"
location_tab_altitude_id = "loc_altitude"
location_tab_name_id = "loc_name"
atmosphere_tab_id = "ui-id-6"
lightpollution_class = "stelaction"
actions_tab_class = "checkableaction"
actions_tab_datetime_value = "actionShow_DateTime_Window_Global"
actions_button_id = "bt_doaction"
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
description_x_front = "/html/body/center/form/table/tbody/tr["
date_sub_x_front = "/html/body/center/form/table/tbody/tr["
date_time_front = "/html/body/center/form/table/tbody/tr["
sdescr_front = "/html/body/center/form/table/tbody/tr["
location_of_event_front = "/html/body/center/form/table/tbody/tr["
attachments_front = "/html/body/center/form/table/tbody/tr["
description_css_front = "body > center:nth-child(1) > form:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child("
description_css_end = ") > td:nth-child(6) > input:nth-child(1)"
description_x_end = "]/td[6]/input"
date_sub_x_end = "]/td[2]"
date_time_end = "]/td[3]"
sdescr_end = "]/td[4]"
location_of_event_end = "]/td[5]"
attachments_end = "]/td[7]"
keywordfield_x = "/html/body/center/div[2]/form/table/tbody/tr[9]/td[2]/input[1]"
date_of_event_x = "/html/body/center/div[2]/form/table/tbody/tr[2]/td[2]/input[5]"
submit_button_x = "/html/body/center/div[2]/form/input[2]"
pagerows = 50
timestamp_string = str(datetime.now())
popup_text = "/html/body/center/table/tbody/tr[2]/td"
popup_x_text = "/html/body/center/table/tbody/tr[2]/td"
popup_text_x_button = "/html/body/center/form/table/tbody/tr[3]/td[6]/input"
casesfound_css = "body > center:nth-child(1) > form:nth-child(4) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > font:nth-child(1)"
xfiles_original_airdate_x_front = "/html/body/font[3]/table[1]/tbody/tr["
xfiles_original_airdate_x_end = "]/td[3]"
ancient_aliens_original_airdate_x_front = ""
ancient_aliens_original_airdate_x_front = ""
topics = ['low in the sky','line formation','bright','green','blue','fbi was there','swat','I saw police','Angels','lights in a line','strange light','cave']
buzzwords = ['God','Jesus','Heaven']
odd_words = ['spouse']
Main_Cities = ['','Austin','Miami','Reno','Tinley Park','New York','Houston','El Paso']
Main_HotSpots = {'Tinley Park':['10/2004','10/2005']}
Primary_States = ['Utah','Idaho','Montana','West Virginia','New Hampshire','Maine']
Cities_to_avoid = ['Chicago']
another_search_x = "/html/body/center/form/input[1]"
def scrollment():
    ic()

    readme
    scrolls down one page length to see invisible content.

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight-1)")
def shifty(bottom,top):
    ic()
    temp = 0
    if bottom > top:
        temp = top
        top = bottom
        bottom = temp
    x = random.uniform(top,top+4)
    while x < top and x > bottom:
        x = random.random()*float(random.uniform(0,top))
    x = round(x)
    time.sleep(x)
def xpathcreator(frontend,iterator,backend):
    ic()
    xpaths_array = []
    fullxpath = ""
    for i in range(int(iter_start),int(iter_end)):
        fullxpath = frontend + str(i) + backend
        xpaths_array.append(fullxpath)
        fullxpath = frontend + str(i) + backend
    if fullxpath == "":
        fullxpath = frontend + str(iterator) + backend
    return(fullxpath)
def xfiles_spyder():
    ic()
    firefox_driver = "/Users/GrahamAtWork/Documents/firefoxdriver"
    driver = webdriver.Firefox()
    url = "http://www.insidethex.co.uk/"
    print("Beginning the program sequence: ",end="")
    driver.get(url)
    print(url)
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
                    print("no such element")
                xfiles_script = open("MUFON_XFiles_Episodes_Scraped.txt",'a+')
                title = elems[elem].text
                xfiles_script.write(title)
                xfiles_script.write('\n')
                this_element = elems[elem]
                this_element.click()
                time.sleep(.15)
                xfiles_script.write(airdate)
                xfiles_script.write('\n')
                paragraphs = driver.find_elements_by_tag_name('p')
                p_counter = 0
                for paragraph in paragraphs:
                    first_paragraph = 3
                    p_counter+=1
                    if p_counter >= first_paragraph:
                        p_text = paragraph.text
                        xfiles_script.write(p_text)
                driver.back()
                time.sleep(random.uniform(1,4))
                elems = driver.find_elements_by_tag_name('a')
                xfiles_script.write('\n')
                tagnumber+=1
    print("completed")
    xfiles_script.close()
    driver.quit()
def ancient_aliens_spyder():
    ic()
    firefox_driver = "/Users/GrahamAtWork/Documents/firefoxdriver"
    driver = webdriver.Firefox()
    url = "https://subslikescript.com/series/Ancient_Aliens-1643266"
    print("Beginning the program sequence: ",end="")
    driver.get(url)
    elems = driver.find_elements_by_tag_name('a')
    tagnumber = 2
    for elem in tqdm(range(0,len(elems))):
        href = elems[elem].get_attribute('href')
        if href is not None:
            if href.find("/episode") > -1:
                try:
                    airdate = driver.find_element_by_xpath(airdate_x).text
                except NoSuchElementException:
                tv_show_script = open("MUFON_Ancient_Aliens_Episodes_Scraped.txt",'a+')
                this_element = elems[elem]
                this_element.click()
                time.sleep(random.uniform(1,4))
                title = driver.find_element_by_tag_name('h1')


                real_title = title.text
                tv_show_script.write(real_title)
                tv_show_script.write('\n')
                real_title = ""
                title = ""
                transcript = driver.find_element_by_class_name("full-script")
                transcript_text = transcript.text
                tv_show_script.write(transcript_text)
                driver.back()
                time.sleep(random.uniform(1,4))
                elems = driver.find_elements_by_tag_name('a')
                tv_show_script.write('\n')
                tagnumber+=1
    print("completed")
    tv_show_script.close()
    driver.quit()

def cosine_sim_vectors(vec1,vec2):
    ic()
    vec1 = vec1.reshape(1,-1)
    vec2 = vec2.reshape(1,-1)
    return cosine_similarity(vec1,vec2)[0][0]
def clean_string(text):

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

    ic()
    from nltk.corpus import stopwords
    stopwords = stopwords.words('english')
    sentences = phrases
    cleaned = list(map(clean_string, sentences))
    vectorizer = CountVectorizer().fit_transform(cleaned)
    vectors = vectorizer.toarray()
    csim = cosine_similarity(vectors)
    csimilarity = cosine_sim_vectors(vectors[0],vectors[1])
    return csimilarity


def my_next_step(driver):
    ic()
    driver.refresh()
    time.sleep(10)
    element=driver.switch_to_frame('iframe')
def wordstemmer(description_string):
    ic()
    words = description_string.split(" ")
    print(words)
    ps = PorterStemmer()
    for word in words:
        print(ps.stem(word))
def transcript_parser(transcript_file,heading_text):


    ic()
    heading_text = str(heading_text)
    newfilename = ""
    myfile = open(transcript_file,'r')
    newfilename = "MUFON_scrubbed_" + transcript_file
    outfile = open(newfilename,'w')
    new_item_line = ""
    for item in tqdm(myfile):
        endofline = 0
        new_item = ""
        if item.find(heading_text)>-1:
            outfile.write(new_item_line)
            outfile.write('\n')
            outfile.write(item)
            new_item_line = ""
        else:
            if item.find("\n") > -1:
                endofline = item.find("\n")
                for i in range(0,endofline):
                    if item[i] != '\n':
                        new_item = new_item + item[i]
                    else:
                        continue
            else:
                new_item = item
        new_item_line = new_item_line + new_item
    outfile.close()
    myfile.close()
    print("cleaned up the ",transcript_file," file and saved in new location --> ",newfilename)
def initializer(download_choice,scrape_more):
    ic()
    if download_choice == True:
        xfiles_spyder()
        ancient_aliens_spyder()
        transcript_parser("MUFON_Ancient_Aliens_Episodes_Scraped.txt","ANCIENT ALIENS")
    else:
        print("transcripts have been downloaded\nChecking updated MUFON Reports Database for Quality")
        transcript_parser("MUFON_Database_Scraped_Reports.txt",'Long Description of Sighting Report')
    if scrape_more == "NO" or scrape_more == False or scrape_more == "n" or scrape_more == "N":
        return 0
    elif scrape_more == 'y' or scrape_more == 'Y' or scrape_more == True:
        print("crawling for more data")
        selenium_crawler(topics,Main_Cities,Primary_States,Main_HotSpots,Cities_to_avoid)
    else:
        print("major issues...")
def selenium_crawler(topic,city,states,mainhotspots,citiestoavoid):
    PRESET_VARIABLE_MAX = 30
    mufon_file = open("MUFON_Database_Scraped_Reports.txt",'a+')
    mufon_file.write(timestamp_string)
    mufon_file.close()
    topic
    from MUFONVARIABLES import nearest_city_field_x
    from MUFONVARIABLES import event_stateusa_x
    from MUFONVARIABLES import keywordfield_x
    from MUFONVARIABLES import date_of_event_x
    from MUFONVARIABLES import submit_button_x
    topics = [topic]
    maincities = [city]
    low = 3
    high = 15
    highest = PRESET_VARIABLE_MAX
    k = 0
    wallace = 0
    richard = 0
    firefox_driver = "/Users/GrahamAtWork/Documents/firefoxdriver"
    driver = webdriver.Firefox()
    url = "https://mufoncms.com/cgi-bin/report_handler.pl?req=search_page"
    print("Beginning the program sequence: ",end="")
    driver.get(url)
    if topic != topics[0]:
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
    shifty(1,random.uniform(2,4))
    nearest_city_field.send_keys(city)
    shifty(1,2)
    nearest_city_field.send_keys(Keys.RETURN)
    shifty(1,3)
    front_elements = [date_sub_x_front,date_time_front,sdescr_front,location_of_event_front,attachments_front,description_css_front]
    end_elements = [date_sub_x_end,date_time_end,sdescr_end,location_of_event_end,attachments_end,description_css_end]
    descriptions = []
    print("waiting till button is visible")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, casesfound_css)))
    descriptions = driver.find_elements_by_class_name("button")
    pagerows = len(descriptions)
    window_before = driver.window_handles[0]
    print("searching for phrase:",topic," and nearest the city:",city)
    topicstring = topic + ','
    for k in tqdm(range(3,pagerows)):
        mufon_file = open("MUFON_Database_Scraped_Reports.txt",'a+')
        mufon_file.write(topicstring)
        front = ""
        back = ""
        inner_string = ""
        for index in range(1,len(front_elements)+1):
            full_path_x = ""
            front = front_elements[index-1]
            back = end_elements[index-1]
            full_path_x = front + str(k) + back
            if index != 6:
                field_contents = driver.find_element_by_xpath(full_path_x).text
            if index == 6:
                field_text = ""
                field_contents = descriptions[k]
                try:
                    field_contents.click()
                    time.sleep(.25)
                except Exception:
                    driver.quit()
                    field_contents = "n/a"
                shifty(1,2)
                if field_contents != "n/a":
                    p = driver.current_window_handle
                    window_handles = driver.window_handles
                    for w in window_handles:
                        if(w!=p):
                            driver.switch_to.window(w)
                            break
                    shifty(.5,1)
                    el = driver.find_element_by_tag_name('body')
                    field_text = el.text
                    inner_string = inner_string + "ø" +str(field_text)
                p = driver.current_window_handle
                driver.close()
                driver.switch_to_window(window_before)
                shifty(.5,1)
                descriptions = driver.find_elements_by_class_name("button")
            else:
                new_field = ""
                field_contents2 = str(field_contents)
                fields = ""
                for i in field_contents:
                    if i != ',' and i != '\n':
                        fields += i
                    else:
                        fields += " "
                field_contents = fields
                if field_contents.find("\n") < len(str(field_contents2)) and field_contents.find("\n")>-1:
                    new_field = field_contents2[0:field_contents2.find("\n")] + " " + field_contents2[field_contents2.find("\n")+1:len(field_contents2)]
                    inner_string = inner_string + "ø" +str(new_field)
                else:
                    if index < len(front_elements)-1:
                        inner_string = inner_string + "ø" +str(field_contents2)
                    else:
                        inner_string = inner_string + "ø" +str(field_contents2)
        fields = ""
        for i in inner_string:
            if i != ',' and i != '\n':
                fields += i
            else:
                fields += " "
        if fields.find(",")>-1 and len(fields)<=len(inner_string):
            print("success")
        fields_ofgrain = ""
        for i in fields:
            if i != 'ø':
                fields_ofgrain += i
            else:
                fields_ofgrain += ","
        mufon_file.writelines(fields_ofgrain[1:])
        mufon_file.write('\n')
	  time.sleep(10)
        mufon_file.close()
    driver.close()
def corpora_sherlock(text_file,delimeter_used):

        README
            takes in a text file and creates a csv file
            (textfile,delimeter_used) for this case will be 'ø' this is option + o

    ic()
    newfilename = ""
    myfile = open(text_file,'r')
    newfilename = "MUFON_Sherlocked_" + text_file
    outfile = open(newfilename,'w')
    myfile = myfile.read()
    print(myfile[0:200])
    fieldtext = ""
    fields = ""
    linetext = ""
    counter = 0
    columns = 12
    rows = myfile.count("øøø")
    reports = [ '' for i in range(rows)]
    matrix_index = 0
    column_id = 0
    reportsline =  [ '' for i in range(columns)]
    for i in tqdm(range(0,len(fields))):
        if fields[i] == 'ø':
            column_id += 1
            counter+=1
            if counter == 3:
                column_id = 0
                reports[matrix_index] = reportsline
                reportsline = []
                matrix_index += 1
                outfile.write(linetext)
                linetext = ""
                counter = 0
            else:
                linetext = linetext + ',' + fieldtext
                fieldtext = ""
        else:
            counter = 0
            fieldtext += fields[i]
    outfile.close()
city = 'Orlando'

def convert_csv_to_dict(filename):
    ic()
    import csv
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        line_count += 1
    print(f'Processed {line_count} lines.')
    return csv_reader
def convert_csv_to_pandas(filename,indexcolumn):
    ic()
    df = pd.read_csv(filename, index_col=indexcolumn)
    return df
def write_to_csv_from_pandas(df_name,new_file_name):
    ic()
    import pandas
    df = pandas.read_csv('hrdata.csv',
                index_col='Employee',
                parse_dates=['Hired'],
                header=0,
                names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    newfilename += ".csv"
    df.to_csv(newfilename)
def finding_nemopolis_old(city_name,state_name,cities_df,cities2_df):
    ic()
    from operator import indexOf
    Mode2 = False
    if len(state_name) == 2:
        Mode2 = True
    null_array = ['','','','']
    if city_name not in cities_df['city_ascii']:
        if city_name not in cities2_df['city_ascii']:
            try:
                null_array = ['','','','']
            except KeyError:
                null_array = [city_name,state_name,'n/a','n/a']
                return null_array
            return null_array
        else:
            cities_df = cities2_df
            null_array = [city_name,state_name,'n/a','n/a']
    if Mode2 == False:
        line_count = 0
        location_data = []
        null_array = [city_name,state_name,'n/a','n/a']
        for row in tqdm(range(0,len(cities_df['city_ascii']))):
            if cities_df['city_ascii'][line_count] == city_name and cities_df['state_name'][line_count] == state_name:
                location_data = [cities_df['city_ascii'][line_count],cities_df['state_name'][line_count],cities_df['lat'][line_count],cities_df['lng'][line_count]]
                return location_data
            else:
                location_data = []
                if row > len(cities_df['city_ascii']):
                    location_data = geopy_city_to_coordinates[city_name,state_name]
                    return location_data
            line_count += 1
    else:
        line_count = 0
        location_data = []
        null_array = [city_name,state_name,'n/a','n/a']
        loc = np.nonzero(np.in1d(cities_df['city_ascii'], city_name))[0]
        loc = np.nonzero(np.in1d(cities_df['city_ascii'], city_name))[0]
        iterator = 0
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
                truevar = var1[1][0]
                var = intersection[0]
                city_loc = intersection[0]
                state_loc = intersection_y[0][truevar]
                location_data = [cities_df['city_ascii'][city_loc],cities_df['state_id'][city_loc],cities_df['lat'][city_loc],cities_df['lng'][city_loc]]
                return location_data
            else:
                location_data = geopy_city_to_coordinates[city_name,state_name]
                return location_data
    return null_array
def chasm_between(point1,point2):
    ic()
    import geopy.distance
    from geopy import distance
    coords_1 = (point1[2], point1[3])
    coords_2 = (point2[2], point2[3])
    dist = geopy.distance.distance(coords_1, coords_2).mi
    return dist
def tojulian(day,month,year):

    README
        dd/mm/yyyy

    ic()
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
    geolocator = Nominatim(user_agent="mufon_scanner")
    location = geolocator.geocode("175 5th Avenue NYC")
    print(location.address)
    print((location.latitude, location.longitude))
    print(location.raw)
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    print(geodes
    df = pd.DataFrame({'name': ['paris', 'berlin', 'london']})
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    tqdm.pandas()
    df['location'] = df['name'].progress_apply(geocode)
    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    import concurrent.futures
    geolocator = OpenMapQuest(api_key="...")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1/20)
    with concurrent.futures.ThreadPoolExecutor() as e:
        locations = list(e.map(geocode, search))

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
    commas = 0
    spaces = 0
    end_of_loc = string.find(',')
    if end_of_loc == -1:
        end_of_loc = len(string)
        mode = 2
    loc_string = ""
    iterator = 0
    if mode == 1:
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
                    else:
                        continue
                if spaces == 5:
                    return loc_string
                iterator+=1
            else:
                return loc_string[1:]
    if mode == 2:
        iterator = -1
        for i in string:
            iterator+=1
            nothing = 0
            if iterator in c_iters:
                nothing = 1
            else:
                continue
            if iterator in s_iters:
                loc_string += str(',')
            if iterator in s_iters and iterator < len(string):
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
    new_locations = []
    for location in csv_data['Location of Event']:
        new_location = city_extraction(location)
        new_locations.append(new_location)
    df = pd.read_csv(filename)
    df["Optimized Location"] = new_locations
    df.to_csv(filename, index=False)
def plotly_project():
    ic()
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
    import csv
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    ThisDay = 1
    fig = make_subplots(rows=7, cols=6, start_cell="top-left",x_title='Your master x-title',
                        y_title='Your master y-title',
                        subplot_titles = [f'Title_{i+1}_{j+1}' for i in range(10) for j in range(2)])
    row = 1
    col = 1
    groupsize = 100
    data = list(csv.reader(open("nycpartyupd.csv")))
    lat = pd.read_csv("nycpartyupd.csv", index_col="Latitude")
    long = pd.read_csv("nycpartyupd.csv", index_col="Longitude")
    barlat  = list(csv.reader(open("bar_locations.csv")))
    BXArray = []
    BYArray = []
    BCArray = []
    i = 0
    j = 0
    for i in tqdm(range(0,len(barlat))):
        BXArray.append(barlat[i][4])
        BYArray.append(barlat[i][5])
        BCArray.append(barlat[i][6])
    CombArrays=[]
    XArrays = []
    YArrays = []
    XAxis_Max = 0
    XAxis_Min = 0
    YAxis_Max = 0
    YAxis_Min = 0
    xbounds = []
    ybounds = []
    TimeArrays = []
    bucket = 0
    while row<8:
        while col<7:
            XArray = []
            YArray = []
            TimeArray = []
            CombArray = []
            day = 0
            record = 0
            rec = ""
            for record in range(1,len(data)):
                rec = int(record)
                day = data[rec][4]
                if int(day) == int(ThisDay):
                    if bucket == groupsize:
                        if data[rec][2] != 0 and data[rec][2] != "0" and data[rec][3] != 0 and data[rec][3] != "0":
                            XArray.append(data[rec][2])
                            YArray.append(data[rec][3])
                            XArrays.append(data[rec][2])
                            YArrays.append(data[rec][3])
                            CombArray.append(data[rec][30])
                            CombArrays.append(data[rec][30])
                            TimeArray.append(data[rec][13])
                            TimeArrays.append(data[rec][13])
                            if float(data[rec][2])>float(XAxis_Max):
                                XAxis_Max = data[rec][2]
                            if float(data[rec][3])>float(YAxis_Max):
                                YAxis_Max = data[rec][3]
                                print("[",YAxis_Max,"],",record,end=",")
                            if float(data[rec][3])<float(YAxis_Min):
                                YAxis_Min = data[rec][3]
                            if float(data[rec][2])<float(XAxis_Min):
                                XAxis_Min = data[rec][2]
                            bucket = 0
                    else:
                        bucket+=1
                        continue
                else:
                    continue
                xbounds.append([XAxis_Min,XAxis_Max])
                ybounds.append([YAxis_Min,YAxis_Max])
            fig.add_trace(go.Scatter(x=XArray, y=YArray,mode="markers"), row=row, col=col)
            fig.add_trace(go.Scatter(x=BXArray, y=BYArray,fillcolor = '
            print("||||",col,",",row,"||||    ",end="")
            col+=1
        col=1
        ThisDay+=1
        print("")
        row+=1
    fig.update_layout(title_text="New York Noise Complaints by Geography")
    fig.update_yaxes(automargin=True)
    fig2 = px.density_heatmap(x=XArrays, y=YArrays)
    fig2.show()
    for i in range(0,7):
        for j in range(0,6):
            title = "xaxis title"
            ytitle = "yaxis title"
            print('fig.update_xaxes(title_text="',title,'", row=',i,' col=',j,')')
            print('fig.update_yaxes(title_text="',ytitle,'", row=',i,' col=',j,')')

    fig.update_xaxes(title_text="xaxis 1 title", row=1, col=1)
    fig.update_layout(title_text="Customizing Subplot Axes", height=700)
    fig.show()
def city_csv_to_location(filename):
    ic()
    coordinates_dict = {'Bogalusa/LA':['Bogalusa', 'LA', 30.7812, -89.8633]}
    cities_df = convert_csv_to_pandas("MUFON_uscities.csv","city")
    cities2_df = convert_csv_to_pandas("MUFON_2014_Cities_updated.csv","city")
    cities_df.head()
    csv_data = pd.read_csv(filename)
    new_locations = []
    csv_data_states = []
    coordinates = []
    for i in range(0,len(csv_data)):
        csv_data_states.append(csv_data['state_id'][i])
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
        print(coordinates_dict[location + "/" + new_location_state[0:2]])
        iterator +=1
    for city_state in tqdm(new_locations):
        dory_bull = city_state.split (",")
        spot = finding_nemopolis(dory_bull[0],dory_bull[1])
        coordinates.append(spot)
    return coordinates_dict
def save_dict_as_csvfile(dict_name):
    ic()
    filename = 'MUFON_' + str("dictionary") + '.csv'
    with open(filename, 'w+') as f:
        for key in dict_name.keys():
            f.write("%s,%s\n"%(key,dict_name[key]))
def Jones_Effect(point_x,dataset):

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

    dataset
def geopy_city_to_coordinates(cityname,statename):

    README
    city name must be like "Austin"
    statename must be in form "Texas"
    no spaces they will be combined with space between them

    inputstring = cityname + " " + statename
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(inputstring)
    print(location.address)
    print(location.raw)
    coordinates = [location.point[0],location.point[1]]
    other_city_data = [location.raw['importance'],location.raw['boundingbox']]
    returnable_array = [coordinates,other_city_data]
    return returnable_array

    result: [[30.2711286, -97.7436995],[0.8694265717866669,['30.0984576', '30.5166255', '-97.9367663', '-97.5605288']]]

def finding_nemopolis(city_name,state_name):
    location_data = ['']
    if len(state_name)>2:
        location_data = geopy_city_to_coordinates(city_name,state_name)
    else:
        return location_data
    return location_data
result = geopy_city_to_coordinates("Austin","Texas")
var = finding_nemopolis("Austin","Texas")
ic(var)
ic(result)
loc_data = finding_nemopolis('Austin','Texas')
loc_data2 = finding_nemopolis('San Diego','California')
distance = chasm_between(loc_data,loc_data2)
coordinates_file = open("citiescoordinates.txt","w+")
coordinates_file.write("city,state_id\n")
coordinates_file.close()
cities = open("citiestocheck.csv",'r')
commas = 0
newcity = ""
newstate = ""
for city in tqdm(cities):
    if city != "\ufeffcity, state_id\n":
        coordinates_file = open("citiescoordinates.txt","a+")
        coordinates = ""
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
            coordinates = finding_nemopolis(newcity,newstate)
        except Exception:
            nothing = 1
        if coordinates != "":
            coordinates_file.write(coordinates)
        newcity = ""
        commas = 0
        newstate = ""
        coordinates_file.close()

def point_finder(R_x,R_y):

    README
    R_x =
    R_y =
    M_x =
    M_y =
    file headers are below
    Source,Date/Time of Event,date posted,duration (seconds),city,state (ABBR),STATE(FULL),country,latitude,longitude ,comments,shape, ,,,

    import pandas as pd
    csvfilename = "NUFORC_CONSOLIDATED_DB.csv"
    data_file = open('/Users/GrahamAtWork/Documents/Automate-with-Python-_-Form-Filling-Script-/TextTester/NUFORC_CONSOLIDATED_DB.csv')
    write_file = open("POINTSOFINTEREST.csv","a+")
    df = pd.read_csv(csvfilename,usecols = [0,1,2,8,9])
    R_x = 0
    R_y = 0
    points_of_interest = []
    iterator = 0
    bounds = 0.5
    for R in df[0]:
        if R == "MUFON":
            R_x = R[8]
        iterator += 1
    for i in range(0,len(df)):
        if i != iterator:
            lat = df.loc[i]['latitude']
            if lat > R_x-bounds and lat < R_x + bounds:
                lng = df.loc[i]['longitude']
                if lng > R_y-bounds and lng < R_y + bounds:
                    points_of_interest.append(df.loc[i])
    write_file.write(points_of_interest)
    data_file.close()
    write_file.close()
    return points_of_interest
results = point_finder(30.2711286,-97.7436995)
ic(results)
