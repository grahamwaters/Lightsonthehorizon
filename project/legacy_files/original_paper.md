



Lights on the Horizon
Valence Density and Lexical Variance as a Significant Factor for Detecting Erroneous Reporting of Unidentified Aerial Phenomena at MUFON and NUFORC

Graham G. Waters
Department of Graduate Studies, Brandeis University
RSAN 175: Analytics Strategy and Management
Dr. Paul Dooley
March 24, 2021
















Keywords: MUFON, NUFORC, Balanced Scorecard, Python 
EXECUTIVE SUMMARY:
This paper provides a cursory introduction to improvements that MUFON and NUFORC could make to their data warehousing solutions and gives some analysis of the data. MUFON and NUFORC are two civilian UFO reporting organizations that have been around for decades. I still believe that there is potential in using the Star Link Satellite sightings for a control group, allowing researchers to generate quantitative measures that gauge the potential value of a UAE report in near-real-time. Longer-term, I would like to see MUFON and NUFORC develop an autonomous detection system that integrates with webcams worldwide and potentially implement deep learning to detect outlying events.
My analysis of MUFON and NUFORC data led to the following findings:
Using two methods of pattern detection that reduce or eliminate bias and subjectivity, hierarchical clustering and density estimation, I found that the data was highly insight-rich. Therefore, hierarchical clustering was selected as a pilot study because it would introduce some pattern recognition capability into the analysis while being straightforward enough for exploratory analysis.
Site Valence Density Analysis led to some interesting correlations between erroneous reporting and various levels of UFO activity that are worth exploring more deeply. Unfortunately, the correlation was difficult to quantify under the time constraints placed on the project. Given time I believe that the report-site density analysis would benefit from a more sophisticated model that supports artificial intelligence or machine learning and can consider various levels of impact on the reported sighting.
 
Abstract
To many, the Mutual UFO Network (MUFON) and its quasi-competitor, the National UFO Reporting Center (NUFORC), are simply two of another group of conspiracy theorist organizations, and to others, they represent the lone gunmen searching for what is really happening, believing firmly that the truth is out there. As for MUFON, the nonprofit is one of the oldest of its kind and is entirely volunteer-based. As a 501(c)3 Charitable organization, they invite people from across the world to work together and collaborate on a subject they are passionate about (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.). Close on their heels, in 1974, NUFORC was founded, also as a nonprofit (National UFO Reporting Center, n.d.). What these organizations may find difficult is how much data they process through their reporting dashboards and, even worse, the backlog of historical data sitting on a shelf in a warehouse. This study is to examine whether valence density is a viable factor to determine the value of a report or whether value can be determined without extensive machine learning or artificial intelligence backgrounds. It will also touch on how balanced score carding and identification of critical metrics for MUFON, in particular, could assist them with changing the organizational design, human capital, or decision-making practices to enable them to deal with a notoriously unruly data set: American UFO Sightings.
 
Problem Statement:
The two giants in the hunt for the unseen, NUFORC and MUFON, both maintain massive data repositories that they have collected from amateur and professional alien hunters around the world. The analytical challenge for these researchers is how they can get past the hype mentality that causes many erroneous reports of unusual events without governing the volume of data flowing into the website. The core of the problem truly lies in their inability to come to a consensus about what a valuable report looks like. So, what organizational challenges can strategic analytics address for these organizations, and how can the application of techniques in Python and SPSS inform an analysis of clusters within their data and improve their ability to generate high-quality data insights about sightings of unusual phenomena?
Hypotheses:
	The reality is that such an in-depth issue generates many hypotheses and that it necessitates them. The limiting factor, besides mental block, always includes time, computing power, and the availability of data. With this in mind, consider the following hypotheses, some of which will become opportunities for further research.
1.	Through careful analysis of reports from MUFON and NUFORC that have high similarity factors in lexical format and location of sighting, a more holistic understanding of the reporting individual will aid researchers to determine the value for their report.
2.	In the year 2020, there were more people who were up late at night and homebound, and this could have caused higher volumes of data for analysis than ever before. This should be researched further through analysis of Social Media posted about phenomena.
3.	The geospatial density, as defined by valences, of Reports has been mentioned as a factor in the successful efforts of some self-proclaimed ufologists of isolating real events.
4.	Text analysis of unstructured and public reports would provide a method of determining the strategic value of each individual report. This will allow researchers at MUFON to more accurately determine centrality points within report clusters. Word Usage within clusters is an indicator of credibility
Areas for MUFON to improve in organization and reporting
Data Warehousing
The data storage solutions that the organization is currently using are increasingly arcane as they are rarely used by those who can afford to use a real solution with an actual GUI. They limit their users to fifty records at a time and provide no API access or developer solutions. This is sharp contrast to the NUFORC site, which is downloadable in moments and free. The data in the comments for NUFORC is sparse when compared to MUFON’s rich tomes of commentary from reporters and thus offers less in the way of sentiment analysis; however, their consistent maintenance of the geospatial data and integrity of records is evident as the quality of their dataset is very high. MUFON could do a better job at keeping their data clean and analyzable.
Data Quality Assurance
Some of the online comments are credible, and even possible scenarios that could occur. These types of sightings should be getting higher value and better ratings than sightings with low corroboration and core valance density. Extrapolating the concept of density analysis to the country requires a talented team of Quality focused professionals who are aware of the needs at the company and also have passion in their work. Below are several examples of low-quality data in MUFON’s Database.
The Overly Spiritual Commentary
“At first, I thought it was a star, the north star, but it was in the west sky. As I was goin back in my house, it moved, I grabbed my door frame n case I was moving, and it moved again. I stepped back outside and hunkered down grabbing my knees so I could be sure I wasnt moving, it moved again. I went inside to get my brother n law, n we watched it for 45min. It would squiggle around, then elevate, then go into a serpantine motion, like a snake on water… Now about who they are, genesis 11:1-9 explains bout tower of babel, God said, I can see when man comes together, nothin is impossible,, then God destroyed the city not the tower. They are humans, in NASAs studies theyve learned that you cant develope babies without gravity. In Texas, in the 50s our govt did autopsies on pregnant aliens. They are in the skies developing their babies. They are humans that have lived up there for thousands of years, they are smarter than we are. This shouldnt surprise anyone, we have only been able to fly for around 109 years, and we can already keep people in space for years at a time. God wants them to be restored, malachi 3:5 do not deprive the aliens of justice. God never lets his people wander forever and he always reserves a remnant. Jesus said he is coming SOON, he said that 2000 years ago. Every star in the sky. They got my attention, then I awoken spiritually” (Recent UFO Sightings | Daily Alien News & Encounters, n.d.).
The admittedly prepared but unsubstantiated post
	“I have a Sigma mirrorless camera that lI enjoy taking cloud pictures with. I looked up and saw this tiny white solid object moving across the sky. It was a dot but it was moving faster than most planes. So I started taking pictures using the viewfinder. I have trouble finding small objects in the viewfinder without my glasses. I didn't have my glasses own so, I was not sure if I actually got a picture of the object. It was a strange-looking because it didn't look like anything I have seen before. Luck was on my side because I did get 4 pictures. When I looked at the pictures zoomed in, it was fascinating. I thought it could be a satellite, but I doubt that it is” (Recent UFO Sightings | Daily Alien News & Encounters, n.d.).
This post admits to capturing four photos of an unidentified flying object yet they do no upload the photos to MUFON’s database as shown in the figure below.

The dramatic and inappropriate commentary
	“It was a normal night. I had put my 1 year old son to bed and had laid down to go to sleep. I woke up a few hours later and the room I was in looked similar to my bedroom - large, king size bed and dresser in the same position inside the 20'x15' room. But surrounding the room was sheer curtains hanging from ceiling to floor and on the other side of the room were people, medical staff of some sort, watching everything I did. I couldn't see them clearly through the curtains…I then went back to sleep and woke the next morning to a normal day” (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.).
There is a significant portion of this removed out of necessity. One thing to mention about this description is the inclusion of the dimensions of the room makes the story less believable. Something that could inform the value, mentioned earlier, to some investigators are comments that include rational thought. If a post says the phrase, “it could be a satellite” yet the person still reported the sighting then it suggests that the event, whatever it was, was at least out of the ordinary.
The Rational Report
“I was laying on a swing outside while my kiddo was laying on her trampoline. We were both looking up at the sky (she was looking for constellations) when she pointed out a small (Star-like) bright light that was flying out of the NW sky to the SW. My first response was “it’s probably a satellite”. Note: These did not have any flashing lights (there were obvious planes flying over head at a much lower altitude (identifiable by their wing lights & some by engine sound) as they flew over. These star-like lights continued to fly over in a consistent line. My kiddo exclaimed, “mom, there’s more, they just keep coming” so I sat up and saw a continuing line of them flying towards us. After about 20 flew over (amongst airplanes which were clearly at a lower level) and more of the star-like lights were visible in the distance I went inside & called my husband out. In total, I probably saw between 40-50 of these star-like lights fly over. They made no noise, they did not blink or flash. They appeared the same size as the stars in the sky around them, except they were moving. They had a steady pace to them. My husband called a friend of ours who lives about 7 miles away to the west of us and she and her husband went out side and observed them as well. The lights were high enough that we would not have been able to pick them up on cell phone cameras” (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.).
This report even has an additional group of witnesses seven miles away, it mentions planes flying with the lights, a believable plotline and lots of witnesses and relatable contexts. These are very challenging to isolate and even more challenging to do in a short period of time. For this reason, this study will not delve into this aspect of value; instead, consider the concept of valence density.
Valence Density
	One aspect that neither MUFON nor NUFORC have made a clear part of their strategy online is the concept of valence density. In chemistry electrons live in spheres surrounding atoms that are called valences and this analogy is perfect for this study. In the rational commentary above the woman mentions that they called their neighbors seven miles away to see if they saw the same thing. This is an example of a valence radius. For this couple they have connections up to (as far as they revealed) seven miles away. This could be incorporated into the bio of the person that posts on MUFON and used to inform machine learning to learn about how these people and people in their sphere react to these kinds of unexplained events. One place that this shows up a lot is in classification. Clustering algorithms essentially find these valences through comparison and iteration. Some have even applied them to bee hive development (Gambhir et al., 2018).






The Issues of these Companies’ Online Interfaces
	Another limiting factor for MUFON and NUFORC is the lack of imagination in their UI and thus UX on the websites. These websites are shown in the two figures below.
Figure 1. NUFORC Main Page (National UFO Reporting Center, n.d.)


Figure 2. MUFON Interface for logging in (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.).
If picking between the color schemes alone NUFORC has the better-looking site. This is not a marketing critique however, and there may be more utility in simply suggesting that higher UX may drive up profitability.

Research Design/Data Collection
The data used in this analysis has been paid for despite the strange loopholes that MUFON has in their database system that is secure in all the wrong ways. In total 419 rows of records were gathered from MUFON for analysis after cleaning and removing the most unusable of the reports.

Data Visualizations
•	Plotly
o	Plotly is a free, open-source library for creating interactive, publication-quality graphics on the web.
I plan to use these libraries to generate a variety of charts and maps of my data in order for me to understand the information I am analyzing, as well as share my findings with other collaborators that are not as familiar with statistics or software.
What credibility factors should be considered when evaluating reports?
1.	Similar reporting in a certain mile radius of the report
2.	Similar reports on that day
3.	Airports in the area
4.	Likelihood of falsification based on word choices
5.	Key buzzwords that should flag interest
6.	Key locations that have reputations for UFO activity.
7.	Reported shape of UFO.¬¬
Methods of data mining to improve the quality of MUFON reports
	The first step towards quality assurance in this large dataset is to narrow down the data into scannable subsets that represent clusters within the reports. One method used for this is known as K-means Clustering. This can be done in SPSS and will be shown later on in a cursory manner as there is much to explore on the data side.
Initial Format of Extracted Corporal Data

2021-03-15ø2021-03-15ø1955-06-012:10PMø1955-06-012:10PMøStopped to observe us, then moved slowly.øStopped to observe us, then moved slowly.øLos Angeles , CA, USøLos Angeles , CA, USøøøLong Description of Sighting ReportI was performing hydrographic surveys in the port of Los Angeles. At about 645 pm I went out on the back of the boat and layed down to take a break. I saw 3 white lights flying north to south very fast. They were in a parallel line and the distance between them didn't vary. All the lights we saw were the same white, circular, and slightly brighter than your average star. I called to my boat captain (Robert) to come out and look. It was clear out. He came out
…
and saw the first 3 lights. text/htmlø<selenium.webdriver.firefox.webelement.FirefoxWebElement (session="dea773d6-7ba6-ab4e-b4f8-03ddb1542ca0", element="45379dca-6836-f749-b09a-b247128ea959")>ø2021-03-07ø2021-03-07ø2021-03-071:05AMø2021-03-071:05AMøstrange light moving in different directionsøstrange light moving in different directionsøAldie, VA, USøAldie, VA, USøøø.

Adapted and extracted from: (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.)

To clean the dataset and transform it into usable data for analytics required the creation of the following python codes snippet which is taken from a larger function included as Appendix A.

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

Once the dataset was transformed into usable data that matched the formatting of the NUFORC database each record was cross-referenced with the records within NUFORC for the state of Texas. The scope of the NUFORC data is beyond the scope of this study and a more granular focus should improve the outcome. For this reason this case study will primarily focus on the state of Texas. Shown in the figure below, there are several variables that are considered in the paper.

Figure 3. SPSS Dataset generated with python code in Appendix A.
Geospatial Considerations for MUFON and NUFORC data
Two functions were developed to measure geospatial distances between points defined by coordinates. These are: finding_nemopolis() and chasm(). These functions are included in Appendix A. As a metric this study considers valances around each report. The square, referred to as valence area, that surrounds each report will be tested for the following key metric:
1.	How many other reports are there within the valence area? This will become known as the reports in cluster variable.
This, and sentiment of the clusters would be the two metrics are integral to MUFON’s strategic success in reaching their self-proclaimed goals of being the voice of UFO hunters everywhere.





Considering Air Traffic

Figure 4. Plotly-generated scatterplot geoplot map in Python. Shows locations of major airports in the country and previews the clusters of reporting in Texas.
Airports
	Many people may be witnessing air traffic from local airports and mistaking it for UFO activity. Airports are a consideration when plotting reports on a map, but we must distinguish the difference between commercial and military airfields. This fails to mention the abundance of space debris that can be seen from the earth occasionally and the thousands of satellites there are in orbit around the earth right now  (Satellites/Debris/Rocket Bodies Currently in Orbit, n.d.).



Areal Coverage
Sizing and comparing two valance areas presumes that there is some underlying variable that is being measured. What if there are multiple UFO reports within the same area? In addition to these metrics to describe UFO activity, another metric has been used as a proxy for human population density: reporting density. This metric was selected over a neural network or regression because it is more general in nature.
Military Bases
The subjective nature of UFO activity renders statistical inference methodologies nearly useless. In order to overcome the skepticism of those that do not believe in the facts of UFO phenomena, an unbiased, third-party approach was taken. The use of a machine-learning algorithm was explored but ultimately deemed beyond the scope due to the sparsity of data that such specialized silos represent.
Quantifying a Lie
The fundamental difficulty with this study has been quantifying lying or dishonesty in text. There have been many studies on what lying looks like in person but far fewer on written lies. Sometimes a lie may be nothing more than a truth that is misleadingly represented. This makes determining a lie so much more challenging for UFO reports. Not everyone experiences UFOs, but it seems that not everyone that does experience UFO-like phenomena reports it. It seems like a logical step to task a bot to reach out to people that lived in the areas of significant encounter clusters to find more people that witnessed potential events. Newman [8] found that across five studies, deceptive communications were characterized by fewer first-person singular pronouns, fewer third-person pronouns, more negative emotion words, fewer exclusive words, and more motion verbs. When compared to non-deceptive communications, deceptive communications were more likely to contain words related to lying and concealment. In a study by Bond and DePaulo, college students in the United States were recruited through an online crowdsourcing site (Mechanical Turk) to complete an online survey about their childhood experiences with deception. They found that those who were more likely to deceive others lied more often, but conversely, those who lied often were not necessarily more likely to be deceived (Accuracy of Deception Judgments - Charles F. Bond, Bella M. DePaulo, 2006, 2006). The link between lying as an action and being lied to as a recipient of lies is tenuous at best.
Findings
	This study focuses on reports in the state of Texas and investigates whether clustering reports based on proximity could yield higher lexical similarity  within clusters. If MUFON data can be clustered in conjunction with the data that is procurable from NUFORC then there will be much more potential insight than if viewed alone. An analysis of the text of five-hundred MUFON Reports scraped from the database reveals several interesting significant connections between terms within the comments. The top used words in these reports collected from both sources were I, light, my, star, red, low, line, time, object, and bright. These will have been biased by the queries submitted to the database: blinding, beautiful, lights in a line, moving star, like star, line, starlink, string of, and strange light. Using SPSS to model the data yielded a two-cluster system within the state of Texas with centroid coordinates shown in the table above. Due to constraints on the research timeline there was very little lexical analysis that could be done programmatically on the dataset. There are other resources that have proven useful for this. An anomaly test returned several cases that should be investigated further to determine what causal factors there are, if any, that could be indicative of potential organizational improvements.

Data Analysis/ Results:
	Using python to parse results found in the NUFORC database as well as data from MUFON’s database, the following database was generated. There were two, one from MUFON and the other from NUFORC and each had separate issues that needed to be addressed before they could be used for insight and comparison.
Data Formatting
Table 2. Format of Data from MUFON in Excel.

Data procured from NUFORC is organized differently that the MUFON data available online which made combining the two data sets time-consuming as an intermediate Python Coder. One critical area for MUFON to improve is a standardization of their data formatting to allow for easier analysis and quicker insight generation. This is if their goal is to find if the truth is out there. The following code was written to determine distances between cities coordinates. It could be adaptable for further papers in the next months.

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
    try:
        coordinates = [location.point[0],location.point[1]]
        other_city_data = [location.raw['importance'],location.raw['boundingbox']]
    except AttributeError:
        coordinates = ['','']
        other_city_data = ['','']
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

Preliminary Findings
	As the research progressed in the NUFORC area it became clear that the volume of data available through their website was an unviable option given the scope of this project. As a result the data used in this study focuses on reports in the state of Texas from both MUFON and NUFORC and investigates whether clustering reports based on proximity with python could allow testing for higher lexical similarity within clusters. If MUFON data can be clustered in conjunction with the data that is procurable from NUFORC, the results could prove interesting. If we can identify high-frequency linguistic features associated with certain clusters, then we may be able to predict whether someone has a propensity for lying or not. Not every cluster in this study is considered a UFO cluster because there are no frequent mentions of occupation in these reports. There are several factors that were considered, but one of the most important was how close an area was to where the event occurred. Perhaps there is some correlation between human population density and UFO sightings that can be quantified. Anecdotally, it seems like Ufologists use this approach when searching for possible cases. Two distinct methods have been used to uncover the hidden patterns in the data while reducing or eliminating bias and subjectivity. These are hierarchical clustering and density estimation. Hierarchical clustering was selected as a pilot study because it would introduce some pattern recognition capability into the analysis while being straightforward enough for exploratory analysis. Hierarchical clustering was selected as a high-level means of organizing the data into meaningful clusters.
Computing a Density Estimate for UFO Activity
In order to understand UFO activity, both NUFORC and MUFON were considered from 1947 to the present day. The NUFORC dataset was downloaded in 2015, while the MUFON dataset has been continuously updated since its inception in 1974. The NUFORC data was filtered to only include reports originating from Texas, where the MUFON data includes all records since its inception. This process created a three-year window of sorts where each cluster was assumed to be valid UFO activity, with the exception of anomalous clusters that represent false positives or class anomalies.
 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import icecream as ic
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#texas points of interest
#city,state,latitude,longitude,event_date,report_date,source,cluster_number,reports_in_cluster,comments,Levenshtein_Similarity,cosine_sim_vectors
'''df = pd.read_csv('TX_pointsofinterest.csv')
df.head()
'''
import plotly.graph_objects as go

import pandas as pd
df2 = pd.read_csv('TX_pointsofinterest.csv')

def plotthis():
    for col in df2.columns:
        df2[col] = df2[col].astype(str)

    df2['text'] = df2['city'] + '<br>' + \
        'event_date ' + df2['event_date'] + ' cluster size ' + df2['reports_in_cluster'] + '<br>'

    fig = go.Figure(data=go.Choropleth(
        locations=df2['city'],
        z=df2['reports_in_cluster'].astype(float),
        locationmode='USA-states',
        colorscale='Reds',
        autocolorscale=False,
        text=df2['text'], # hover text
        marker_line_color='white', # line markers between states

    ))

    fig.update_layout(
        title_text='MUFON and NUFORC Reporting Analysis',
        geo = dict(
            scope='usa',
            projection=go.layout.geo.Projection(type = 'albers usa'),
            showlakes=True, # lakes
            lakecolor='rgb(255, 255, 255)'),
    )
    df = pd.read_csv('TX_pointsofinterest.csv')
    df['text'] = df['city'] + ' ' + df['state'] + ', date:' + df['event_date'] + '' + 'source: ' + df['source'].astype(str)

    fig.add_trace(go.Scattergeo(
            lon = df['longitude'],
            lat = df['latitude'],
            text = df['text'],
            mode = 'markers',
            marker = dict(
                size = 8,
                opacity = 0.8,
                symbol = df['cluster_number'],
            ),
            marker_color = df['reports_in_cluster'],
            showlegend = True,
            #size = 10,
            ))

    df = pd.read_csv('2011_february_us_airport_traffic.csv')
    df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)
    fig.add_trace(go.Scattergeo(
            lon = df['long'],
            lat = df['lat'],
            text = df['text'],
            mode = 'markers',
            marker = dict(
                size = 10,
                opacity = 0.5,
                symbol = 'pentagon',
            ),
            marker_color = 'red',

            ))
    fig.update_layout(
            title = 'MUFON and NUFORC Data Clusters in Texas',
            geo_scope='usa',
        )
    # focus point
    lat_foc = 31.3915
    lon_foc = -99.1707
    fig.update_layout(
            geo = dict(
                projection_scale=3, #this is kind of like zoom
                center=dict(lat=lat_foc, lon=lon_foc), # this will center on the point
            ))

    fig.show()

plotthis()

The above code was influenced by the works of (Dataman, 2020) and (plotly.com, 2020).
	Getting deeper into sentiment analysis of each of these clusters is the next step in this research effort. As is noted by leaders in the field, deep learning is a key element of successful sentiment analysis, and especially with the speed that the world’s lexicon is expanding (Understanding Emotions in Text Using Deep Learning and Big Data | Elsevier Enhanced Reader, n.d.).



Figure 6. MUFON and NUFORC Data Cluster Illustration on the State of Texas using Plotly and Geoplots (Dataman, 2020).
Focusing on MUFON specifically, how can balanced scorecarding help them in their key performance areas?
Business Units
1.	Data Collection
2.	Research and Investigation
3.	Education
O: (Objective)
MUFON will increase database quality  by 10% and grow the database by an additional 25,000 reports from social media listening in the next year. Collect data on purported UFO sightings in the MUFON Database and disseminate this data to researchers around the world. One of the goals of MUFON is to educate the public on UFO phenomenon and their potential impacts on society. In the next year MUFON will increase their educational impact and reach  by 10% year-over-year.
A: (Advantage)
MUFON has no direct competition as it is a nonprofit in a niche market. As an education platform it competes with YouTube Channels such as (insert name here) for viewers. It’s primary advantage over other potential competitors is its name recognition and compiled data.
S: (Scope):
MUFON’s scope is limited to the data available in current repositories and any social media data collected from primary sites. The company will not utilize any methodology that has been previously characterized as pseudoscience or innuendo in their education.





Table 1. Change Agenda for MUFON based on (Kaplan & Norton, 1996).

 	PRESENT	FUTURE
We are Getting	Financial	Subscriptions 	Varying Levels of Subscriptions
		Current tuition for MUFON University coursework.	MUFON University coursework tuition as well as paid influencers that teach online.
		 	Grants based on meritorious research in the field.
		Donations from hundreds of benefactors	Donations from more benefactors.

	Customer	Random Website Traffic	Website Traffic Driven by Ads
		Repeat Customers (subscribers)	Higher numbers of subscribers
		Purchasers of Training Materials	More trainers until reaches economy of scale.
	Data	Data from thousands of reporters	Data from thousands of reporters
		n/a	Social Media Listening data
		Data from news outlets	Data from more news outlets
		 	Web Scraping Data, news, Google, RSS feeds, Webcams, Foreign country support.
		Compiled UFO data from various data lakes dedicated to UFO knowledge management. 	Maintain the compiling of these data
We are Doing	Product Service Process	Providing Data on the Website along with map data and other useful tools for UFO researchers.	Providing Data on the Website along with map data and other useful tools for UFO researchers that boost performance.
		 	MUFON Research Library, New Website, MARRS Archive System Hosting, CUFOS Documents scanned into the CMS worldwide UFO Database.
		Creating courses (MUFON University) to educate people about UFO phenomena and providing trainings to become a ufologist researcher in the field	Same
		Testing Facilities around the world are occasionally used to test extraterrestrial materials. 	Utilization of CISION for PR. ($13k/yr.), MUFON TV service for MUFON members. Highest Quality Materials Testing facilities around the world.

	People & Process	Attracts people with a tendency to paranoia that typically have a conspiratorial view of the world.	Secure the services of a few trusted researchers and individuals that add credence to the ufology field, limiting the pseudoscientific approach to the study.
		Processes are very opaque and do not promote a trustworthy face to the public. Average people are less likely to donate. 	They employ high levels of transparency to promote public trust. They also show dedication to quality and accuracy to truly send out the MUFON message.
		 	MUFON will grow their member population.
		MUFON Partners with over 70 scientists and thousands of members worldwide. 	MUFON will partner with over 200 scientists and labs around the world.

Table 2. Strategy Map for Change based on (Kaplan & Norton, 1996).
Verb	Adjective	Noun	Additional	Statement
Generate	highly attractive, new	subscription models	offering various tiers for different types of members. 	MUFON Will Generate highly attractive, new subscription models offering various tiers for different types of members.
maintain current tuition and employ	talented, rational, trusted, and intelligent	online influencers on major social media platforms	to drive up interest in younger people and promote justifiable assertations to the new generation. [Brave new World Campaign]	MUFON Will maintain current tuition and employ talented, rational, trusted, and intelligent online influencers on major social media platforms to drive up interest in younger people and promote justifiable assertations to the new generation. [Brave new World Campaign]
Obtain	Grants	for researching UFO sightings or unexplained phenomena around the world	which shows a philanthropic motivation behind the effort to seek the truth that is out there. 	MUFON Will Obtain Grants for researching UFO sightings or unexplained phenomena around the world which shows a philanthropic motivation behind the effort to seek the truth that is out there.
Secure	larger, more impactful, and visible	donations and funding	from various sources preferably in higher profile positions. 	MUFON Will Secure larger, more impactful, and visible donations and funding from various sources preferably in higher profile positions.
 	 	 	 	MUFON Will
Generate	higher, and more fruitful, easy to convert, 	web traffic on the MUFON website and social media pages	by using targeted ad campaigns and more strategic ad placement. 	MUFON Will Generate higher, and more fruitful, easy to convert, web traffic on the MUFON website and social media pages by using targeted ad campaigns and more strategic ad placement.
Maintain 	the current, brand-loyal, interested, and engaged	subscriber-base on MUFON.com	 	MUFON Will Maintain the current, brand-loyal, interested, and engaged subscriber-base on MUFON.com
Promote and Sell	higher volumes of higher quality and dynamic 	training materials, bundles, and software 	to more trainers online till economy-of-scale is reached.	MUFON Will Promote and Sell higher volumes of higher quality and dynamic training materials, bundles, and software to more trainers online till economy-of-scale is reached.
Collect	All kinds (unstructured, structured, high-quality, low-quality)	of data on UFO sightings or reports of other phenomena	around the globe.	MUFON Will Collect All kinds (unstructured, structured, high-quality, low-quality) of data on UFO sightings or reports of other phenomena around the globe.
scrape	relevant, suspicious, or potentially relevant	posts, pictures, videos, or commentary 	that seems to relate to a UFO-like (or other) event occurring. 	MUFON Will scrape relevant, suspicious, or potentially relevant posts, pictures, videos, or commentary that seems to relate to a UFO-like (or other) event occurring.
scrape	higher volumes of either freely accessible, or purchased	news material	from various websites that are likely to run stories on UFOs or MUFON-related phenomena. 	MUFON Will scrape higher volumes of either freely accessible, or purchased news material from various websites that are likely to run stories on UFOs or MUFON-related phenomena.
scrape	higher volumes of either freely accessible, or purchased	google data, RSS feed data, Webcam footage, and other online sources 	which will be scanned for any statistically significant possibility of a phenomena-event occurring. 	MUFON Will scrape higher volumes of either freely accessible, or purchased google data, RSS feed data, Webcam footage, and other online sources which will be scanned for any statistically significant possibility of a phenomena-event occurring.
maintain	current, updated, secured 	data from various repositories on UFO reports	 	MUFON Will maintain current, updated, secured data from various repositories on UFO reports
provide	free, accessible, and accurate 	data on UFO reporting around the world as well as tools 	for boosting UFO researcher performance 	MUFON Will provide free, accessible, and accurate data on UFO reporting around the world as well as tools for boosting UFO researcher performance
Raise enough funding to begin scanning	the large, valuable, unformatted	 CUFOS documents	into the CMS worldwide UFO Database	MUFON Will Raise enough funding to begin scanning the large, valuable, unformatted CUFOS documents into the CMS worldwide UFO Database
Create and keep creating	educational, nonbiased, science-based	courses through MUFON University	for users that wish to become professional ufologists, researching in the field.	MUFON Will Create and keep creating educational, nonbiased, science-based courses through MUFON University for users that wish to become professional ufologists, researching in the field.
Raise enough funding to secure the use of 	trusted, scientific, transparent, and secure	science laboratories around the world	for the testing of all purported extraterrestrial matter obtained by MUFON	MUFON Will Raise enough funding to secure the use of trusted, scientific, transparent, and secure science laboratories around the world for the testing of all purported extraterrestrial matter obtained by MUFON
Raise enough funding to employ	the powerful	CISION PR platform	for public relations management. 	MUFON Will Raise enough funding to employ the powerful CISION PR platform for public relations management.
Secure the services of 	trusted, influential, nonbiased, and not conspiratorial	leaders’ researchers, and individuals	 that add credence to the ufology field, limiting the pseudoscientific approach to the study.	MUFON Will Secure the services of trusted, influential, nonbiased, and not conspiratorial leaders researchers, and individuals that add credence to the ufology field, limiting the pseudoscientific approach to the study.
Create and cultivate	a transparent, trustworthy, quality-dedicated	public image	to promote public trust which will also show dedication to quality and accuracy to truly send out the MUFON message. 	MUFON Will Create and cultivate a transparent, trustworthy, quality-dedicated public image to promote public trust which will also show dedication to quality and accuracy to truly send out the MUFON message.
generate	organic, findings-based	growth	in member populations by sound practices. 	MUFON Will generate organic, findings-based growth in member populations by sound practices.
partner with	over 200 credible, sound-minded 	scientists, and laboratory specialists around the world	 	MUFON Will partner with over 200 credible, sound-minded scientists, and laboratory specialists around the world
Further Opportunities for Research
There are many other areas that would be fantastic for research in this field. For one there seems to be no social media element that is commonly being used to track unexplained phenomenon. This may be an area for opportunity for the usual UFO network as they were to expand their environmental sensing capabilities and social listening technology.
Starlink Satellite Launches as potential control group
	The unique opportunity the UFO researchers have right now is that for the first time in history there is a control group for the experiment. Identifying reporters that were witnessing star link satellites but did not know this could possibly be the first step for man into the world of science-based deep learning about unidentified phenomena that haunt the skies. As recently as March 11, SpaceX launched 60 Star link satellites from Space Launch Complex 40 (SLC-40) at Cape Canaveral Space Force Station in Florida (Starlink, n.d.). According to amateur astronomers someone as the best chance of witnessing Starlink Satellites in the twilight moments, 30 minutes before sunrise or 30 minutes after sunset. Due to their heat-resistant coating they shine like pearls in a row (Visualization et al., 2015).
Stellarium  Integration
	Integrating Astronomy Application: Stellarium’s web-interface with Selenium in Python has potential as well. It has the ability to track these satellites and extrapolate their locations back in time. This would allow cross referencing the locations with coordinates in the databases of MUFON and NUFORC.  
References
Accuracy of Deception Judgments—Charles F. Bond, Bella M. DePaulo, 2006. (2006). https://journals.sagepub.com/doi/10.1207/s15327957pspr1003_2
Dataman, D. (2020, June 5). Powerful Plots with Plotly. Medium. https://medium.com/analytics-vidhya/plot-with-plotly-114ac106e25f
Gambhir, A., Payal, A., & Arya, R. (2018). Performance analysis of artificial bee colony optimization based clustering protocol in various scenarios of WSN. Procedia Computer Science, 132, 183–188. https://doi.org/10.1016/j.procs.2018.05.184
Kaplan, R. S., & Norton, D. P. (1996). Linking the Balanced Scorecard to Strategy. California Management Review, 39(1), 53.
MUFON - Recent UFO Sightings | Daily Alien News & Encounters. (n.d.). Retrieved March 13, 2021, from https://www.mufon.com/
National UFO Reporting Center. (n.d.). Retrieved March 24, 2021, from http://www.nuforc.org/
plotly.com. (2020). Line and Scatter Plots. Plotly.Com/Line-and-Scatter. https://plotly.com/python/line-and-scatter/
Recent UFO Sightings | Daily Alien News & Encounters. (n.d.). MUFON. Retrieved March 13, 2021, from https://www.mufon.com/
Satellites/Debris/Rocket bodies currently in orbit. (n.d.). Retrieved March 21, 2021, from https://www.n2yo.com/satellites/
Starlink. (n.d.). Starlink. Retrieved March 19, 2021, from https://www.starlink.com
Understanding Emotions in Text Using Deep Learning and Big Data | Elsevier Enhanced Reader. (n.d.). https://doi.org/10.1016/j.chb.2018.12.029
Visualization, D., Underst, T. W. T. D. I. T. O., Excel,  ing of the world I. spend a lot of time with my face buried in, here,  when I. find something interesting I. write about it, Cities,  also as a G., & background, H. P. contributor M. about my. (2015, June 3). The Most Credible UFO Sightings And An Interactive Map. Metrocosm. http://metrocosm.com/map-of-ufo-sightings/
