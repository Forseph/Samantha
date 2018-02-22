# Samantha
Movie Review Sentiment Analysis

Predicting Sentiment with Rotten Tomatoes Reviews

Zack Zhuang - gzhuang@scu.edu
Justin Read - jread@scu.edu
Michael Fodor - mfodor@scu.edu
February 2, 2018 


Background 
This project focuses on predicting sentiment of “Rotten Tomatoes” reviews by implementing machine learning algorithms. The results of predictions such as these have major applications in big business; machine learning algorithms can make recommendations, insist on investments, and show potential trends of public interest. In other words, based off of public sentiment, investors can foresee trends and companies can make internal improvements. 

The source of movie reviews will come from the Rotten Tomatoes (RT) site, published by Senh Duong and Patrick Lee in 1998. To get clean data we will run series of code to remove the unnecessary aspects of the data strings. We will remove the HTML brackets, de-capitalize all words/phrases, and replace any special characters that do not promote sentiment, such as quotation marks, hyphens, and underscores, with a space. 


Project Ideas
The project can be broken down into four main areas: data acquisition/mining, data analysis, data visualization, and creating a UI tool for users.

Data Collection
In order to collect the data from Rotten Tomatoes, we have decided to research into using the Rotten Tomatoes API to collect data. The Rotten Tomatoes API is a tool that enables the user to access the Rotten Tomatoes database for information on ratings, reviews, etc. Currently, we are working on applying for a Rotten Tomatoes API key. By utilizing the Rotten Tomatoes API, we hope to be able to grab data on a specific movie and put all of the ratings from that movie (both critic and audience reviews) into a Python dictionary. Each rating will be correlated with particular text (the review). For instance:
{4 : “This movie was pretty good”, 1: “This movie was awful”, ………}

Data Analysis
Once the data has been arranged into the Python dictionary, we will need to perform text analysis on the text for each rating. First, we will sort by ratings. We will group ratings from ½ star to 2 stars as “negative”, 2.5 stars to 3.5 stars as “neutral,” and 4 stars to 5 stars as “positive.” Then, we will utilize 4 dictionaries in order to analyze text. The four dictionaries will be called neg_text, neu_text, pos_text, and all_text. Within each of the first three dictionaries, we will essentially keep a count of the words in the text. The “top 50” words from negative, neutral, and positive reviews will be most important. We’ll also add an algorithm to filter out words such as “the”, “a”, “an”, “or”, “not,” which do not provide us any useful emotive information; most likely this will just be an if condition within the algorithm which counts all of the words. In the all_text dictionary, we will plan to map each word to an array of ratings. In other words, the dictionary will look something like this:
{“sensational” : [3.5, 4, 4.5, 4, 3.5, 5, 5, 5, 3, 2, 4.5, …..], “horrendous” : [1, 3, 2.5, 2, …..], …}
Within each word, we will be able to go back and see the “average rating” correlated with that word.

In essence, we will want to analyze the data to come up with the following data points:
Average “rating” for each word (i.e. the word “terrible” on average is correlated with a rating of 1.8)
Top 50 words in each category of rating (negative, neutral, positive) (i.e. the most common words on positive ratings were: “classic,” “fabulous,” “epic,” . . . etc.)

Data Visualization
Once the data has been collected, we will make use of matplotlib to neatly plot our findings. I can imagine a few different plots which can provide important data findings:
Plot the 10 most common words for each category of rating along with their counts
Plot a graph that consists of all average ratings (most likely a histogram); I hypothesize this graph to be roughly a normal distribution, centered on the average of the movie chosen

UI Tool
Lastly, we will develop a UI tool that can provide helpful information to the users about the reviews on Rotten Tomatoes. The UI tool will be designed such that the user can choose two important criteria:
Rating of movie (drop-down select menu of “Positive,” “Neutral”, or “Negative”)
Keywords associated with the movie rating. The user can enter words like “fantastic” or “awful”
The default for both positions, respectively, are “Positive” rating and “good” as a keyword. 

Timeline    
This project will be completed with specific goals in mind, week-by-week. The tentative plan is as follows, keeping in mind that we have only six weeks remaining to have a finished application:
Week 5 - By the end of week 5, we would like to have a working version of the Rotten Tomatoes API. If for some reason our request is denied, we should have another working solution in order to collect the Rotten Tomatoes data. By the end of the week, we basically want to have all of the “data collection” portion of the project complete, including reviews and ratings.

Week 6 - This week will be used to organize the data into the structures as mentioned above under the “analysis” portion of the project. By the end of this week, we should have a pretty good idea of the sentiment that each word invokes (measured by the rating), as well as the top 50 words correlated with negative, neutral, and positive ratings.

Week 7 - This week will be spent using matplotlib to visualize the data into the two graphs mentioned above. If for some reason, the data analysis has been slowed, this week will be spent continuing to work on analysis.

Week 8 - This week will be spent working on the UI tool. Ideally, we’d like to complete the tool before week 9, although we anticipate part of the week needing to be spent on researching about and learning the necessary tools and libraries to create the UI tool.

Week 9 - The penultimate week of class will be used to finalize any parts of the project which have not been completed (i.e. last-minute touches to the UI tool), as well as working on a write-up of the project.

Week 10 - The final week of class will be spent on the presentation and submission of the project.




Bibliography 
Predicting Sentiment from Rotten Tomatoes Movie Reviews
-Jean Y. Wu, Yuanyuan Pao

A machine-learning approach to venture capital
-Gnanasambandam, Chandra, McKinsey Quarterly, 00475394, 2017, Issue 3

A COMPARATIVE STUDY OF MACHINE LEARNING ALGORITHMS USING FEATURE SELECTION METHODS FOR MOVIE REVIEW ANALYSIS
KAUR, RAJWINDER;VERMA, PRINCE 
http://eds.b.ebscohost.com.libproxy.scu.edu/eds/detail/detail?vid=0&sid=6be6c2e5-43b1-410d-9409-b09a2d1d9c88%40sessionmgr104&bdata=JnNpdGU9ZWRzLWxpdmU%3d#AN=125510401&db=aci

Python 101: How to Collect Data from Rotten Tomoatoes. https://www.blog.pythonlibrary.org/2013/11/06/python-101-how-to-grab-data-from-rottentomatoes/. Accessed: February 1, 2018

Rotten Tomatoes API. https://www.programmableweb.com/api/rotten-tomatoes. Accessed: February 1, 2018


