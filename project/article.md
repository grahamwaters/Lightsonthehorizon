

# Lights on the Horizon
Valence Density and Lexical Variance as a Significant Factor for Detecting Erroneous Reporting of Unidentified Aerial Phenomena at MUFON and NUFORC

Graham G. Waters, M.S. Strategic Analytics
Began project March 24, 2021 as a Graduate Student at Brandeis University.
Department of Graduate Studies, Brandeis University
RSAN 175: Analytics Strategy and Management


# EXECUTIVE SUMMARY:

This paper provides a cursory introduction to improvements MUFON and NUFORC could make to their data warehousing solutions and gives some data analysis. MUFON and NUFORC are two civilian UFO-reporting organizations that have been around for decades. There is still potential in using the Star Link Satellite sightings for a control group, allowing researchers to generate quantitative measures that gauge the potential value of a UAE report in near-real-time. I want to see MUFON and NUFORC develop an autonomous detection system that integrates with webcams worldwide and potentially implements deep learning to detect outlying events.
My analysis of MUFON and NUFORC data led to the following findings:
Using two methods of pattern detection that reduce or eliminate bias and subjectivity, hierarchical clustering and density estimation, I found that the data was highly insight-rich. Therefore, hierarchical clustering was selected as a pilot study because it would introduce some pattern recognition capability into the analysis while being straightforward enough for exploratory analysis.
Site Valence Density Analysis led to some interesting correlations between erroneous reporting and various levels of UFO activity that are worth exploring more deeply. Unfortunately, the correlation took a lot of work to quantify under the time constraints placed on the project. Given time, the report-site density analysis would benefit from a more sophisticated model that supports artificial intelligence or machine learning. It can consider various levels of impact on the reported sighting.

# Abstract
To many, the Mutual UFO Network (MUFON) and its quasi-competitor, the National UFO Reporting Center (NUFORC), are two of another group of conspiracy theorist organizations. To others, they represent the lone gunmen searching for what is happening, believing firmly that the truth is out there. As for MUFON, the nonprofit is one of the oldest and is entirely volunteer-based. As a 501(c)3 Charitable organization, they invite people from across the world to work together and collaborate on a subject they are passionate about (MUFON - Recent UFO Sightings | Daily Alien News & Encounters, n.d.). Close on their heels, in 1974, NUFORC was founded, also as a nonprofit (National UFO Reporting Center, n.d.). These organizations may need help finding how much data they process through their reporting dashboards and, even worse, the backlog of historical data sitting on a shelf in a warehouse. This study examines whether valence density is a viable factor to determine the value of a report or whether value can be quantified without extensive machine learning or artificial intelligence backgrounds. It will also touch on how balanced score carding and identification of critical metrics for MUFON, in particular, could assist them with changing the organizational design, human capital, or decision-making practices to enable them to deal with a notoriously unruly data set: American UFO Sightings.

# Problem Statement:
The two giants in the hunt for the unseen, NUFORC and MUFON, maintain massive data repositories they have collected from amateur and professional alien hunters worldwide. The analytical challenge for these researchers is how they can get past the hype mentality that causes many erroneous reports of unusual events without governing the volume of data flowing into the website. The core of the problem truly lies in their inability to come to a consensus about what a valuable report looks like. So, what organizational challenges can strategic analytics address for these organizations, and how can the application of techniques in Python and SPSS inform an analysis of clusters within their data and improve their ability to generate high-quality data insights about sightings of unusual phenomena?

# Hypotheses:
    The reality is that such an in-depth issue generates many hypotheses and that it necessitates them. The limiting factor, besides mental block, always includes time, computing power, and data availability. With this in mind, consider the following hypotheses, some of which will become opportunities for further research.

1. Through careful analysis of reports from MUFON and NUFORC that have high similarity factors in lexical format and location of sighting, a more holistic understanding of the reporting individual will aid researchers in determining the value of their report.

2. In 2020, more people were up late at night and homebound, which could have caused higher volumes of data for analysis than ever before. This should be researched further through analysis of Social Media posts about phenomena.

3. The geospatial density, as defined by valences, of Reports has been mentioned as a factor in the successful efforts of some self-proclaimed ufologists of isolating actual events.

4. Text analysis of unstructured and public reports would provide a method of determining the strategic value of each individual report. This will allow researchers at MUFON to assess centrality points within report clusters more accurately.

# Chat GPT Suggestions

Sure, I can help you with that. Here is a high-level outline of the steps you could take to analyze UFO reports using Python:



Collect and clean the data: You'll need to gather the UFO reports from MUFON and NUFORC and clean the data to get rid of any invalid or missing entries. This may involve formatting dates, removing duplicates, and handling missing values.

Gather data from MUFON and NUFORC: You can scrape the data from these organizations' websites using Python libraries such as BeautifulSoup or Selenium.

Clean and preprocess the data: This involves removing missing values, formatting columns correctly, and converting data into a usable format. You can use pandas for this.

Explore the data: Use visualizations and statistical analyses to get a sense of the data and identify any patterns or trends. You can use matplotlib and seaborn for visualizations and scipy for statistical tests.

Select and apply a clustering algorithm: Choose a clustering algorithm that is suitable for your data, such as K-Means or DBSCAN. Use scikit-learn to implement the algorithm and cluster the data.

Analyze the results: Interpret the clusters that were created and try to identify any common characteristics or patterns among them. You may also want to try different parameters or algorithms to see if you can improve the results.

Validate the results: Use external sources to verify the accuracy of the clusters and make sure that they are meaningful and useful. You can also ask domain experts to provide input on the results.

Communicate the findings: Present the results in a clear and concise manner, either in a report or through visualizations. Make sure to highlight the implications of the findings and any recommendations for future research or action.

# Data Sources
