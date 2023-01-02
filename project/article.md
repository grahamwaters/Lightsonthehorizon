

# Lights on the Horizon
Valence Density and Lexical Variance as a Significant Factor for Detecting Erroneous Reporting of Unidentified Aerial Phenomena at MUFON and NUFORC

Graham G. Waters
Department of Graduate Studies, Brandeis University
RSAN 175: Analytics Strategy and Management
Dr. Paul Dooley
March 24, 2021

# EXECUTIVE SUMMARY:

This paper provides a cursory introduction to improvements that MUFON and NUFORC could make to their data warehousing solutions and gives some analysis of the data. MUFON and NUFORC are two civilian UFO reporting organizations that have been around for decades. I still believe that there is potential in using the Star Link Satellite sightings for a control group, allowing researchers to generate quantitative measures that gauge the potential value of a UAE report in near-real-time. Longer-term, I would like to see MUFON and NUFORC develop an autonomous detection system that integrates with webcams worldwide and potentially implement deep learning to detect outlying events.
My analysis of MUFON and NUFORC data led to the following findings:
Using two methods of pattern detection that reduce or eliminate bias and subjectivity, hierarchical clustering and density estimation, I found that the data was highly insight-rich. Therefore, hierarchical clustering was selected as a pilot study because it would introduce some pattern recognition capability into the analysis while being straightforward enough for exploratory analysis.
Site Valence Density Analysis led to some interesting correlations between erroneous reporting and various levels of UFO activity that are worth exploring more deeply. Unfortunately, the correlation was difficult to quantify under the time constraints placed on the project. Given time I believe that the report-site density analysis would benefit from a more sophisticated model that supports artificial intelligence or machine learning and can consider various levels of impact on the reported sighting.
 
# Abstract
To many, the Mutual UFO Network (MUFON) and its quasi-competitor, the National UFO Reporting Center (NUFORC), are simply two of another group of conspiracy theorist organizations, and to others, they represent the lone gunmen searching for what is really happening, believing firmly that the truth is out there. As for MUFON, the nonprofit is one of the oldest of its kind and is entirely volunteer-based. As a 501(c)3 Charitable organization, they invite people from across the world to work together and collaborate on a subject they are passionate about (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.). Close on their heels, in 1974, NUFORC was founded, also as a nonprofit (National UFO Reporting Center, n.d.). What these organizations may find difficult is how much data they process through their reporting dashboards and, even worse, the backlog of historical data sitting on a shelf in a warehouse. This study is to examine whether valence density is a viable factor to determine the value of a report or whether value can be determined without extensive machine learning or artificial intelligence backgrounds. It will also touch on how balanced score carding and identification of critical metrics for MUFON, in particular, could assist them with changing the organizational design, human capital, or decision-making practices to enable them to deal with a notoriously unruly data set: American UFO Sightings.
 
# Problem Statement:
The two giants in the hunt for the unseen, NUFORC and MUFON, both maintain massive data repositories that they have collected from amateur and professional alien hunters around the world. The analytical challenge for these researchers is how they can get past the hype mentality that causes many erroneous reports of unusual events without governing the volume of data flowing into the website. The core of the problem truly lies in their inability to come to a consensus about what a valuable report looks like. So, what organizational challenges can strategic analytics address for these organizations, and how can the application of techniques in Python and SPSS inform an analysis of clusters within their data and improve their ability to generate high-quality data insights about sightings of unusual phenomena?

# Hypotheses:
	The reality is that such an in-depth issue generates many hypotheses and that it necessitates them. The limiting factor, besides mental block, always includes time, computing power, and the availability of data. With this in mind, consider the following hypotheses, some of which will become opportunities for further research.

1.	Through careful analysis of reports from MUFON and NUFORC that have high similarity factors in lexical format and location of sighting, a more holistic understanding of the reporting individual will aid researchers to determine the value for their report.

2.	In the year 2020, there were more people who were up late at night and homebound, and this could have caused higher volumes of data for analysis than ever before. This should be researched further through analysis of Social Media posted about phenomena.

3.	The geospatial density, as defined by valences, of Reports has been mentioned as a factor in the successful efforts of some self-proclaimed ufologists of isolating real events.

4.	Text analysis of unstructured and public reports would provide a method of determining the strategic value of each individual report. This will allow researchers at MUFON to more accurately determine centrality points within report clusters. Word Usage within clusters is an indicator of credibility.
