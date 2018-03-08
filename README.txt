README.txt Group 9
Justin Read, Zack Zhuang, Michael Fodor
Predicting Sentiment from Movie Reviews

1. datacollection.py
This file is meant to collect all of the data from Rotten Tomatoes. It makes use of Beautiful Soup and
goes through 50 pages of results (20 results per page) for 10 selected movies, making a total of about
10,000 reviews. The data will be stored in a separate dictionary per movie with {review : rating} format
for key, value pairs.

To run the file, simply type python datacollection.py in the command line. No arguments are needed, and the
user should make sure that Python 2.7.13 is installed so that requests and Beautiful Soup modules can be
used. If the user would like to change any of the movies, simply change the links at the bottom of the
file where the collectdata function is called. The link should be to the first page of "Audience Reviews"
for a given movie on Rotten Tomatoes. It would be a good idea, too, to change the name of the movie
in the function call so that the json file is named accordingly.

Important Note: with 50 pages and 10 movies, the total run time is about 30 minutes on a standard laptop

2. starwars.json, ... , piratesofthecaribbean.json
All of the json files have been produced by the datacollection.py file. They must be in the same
directory as the Jupyter notebook in order for the notebook to run correctly. Each contain
the associated movie data with {review1 : rating1, review2 : rating2, ... , reviewn : ratingn}

These files will be provided with our project submission so that the grader does not have
to rerun the datacollection.py file (and have to wait for 30 minutes)

3. project_JupyterNotebook_Group9.ipynb
Here is the main Jupyter notebook for the project. All cells have been commented and take the user through
all of the steps from grabbing the data all the way through comparing naive bayes and logistic regression
accuracy results.

The only important thing to note for this file which hasn't been mentioned in the comments is that
all of the json files produced by datacollection.py MUST be in the same directory as the Jupyter notebook.
Otherwise, the notebook cannot read in the correct data.

Run time for all cells combined is roughly 1.5 - 2 minutes.