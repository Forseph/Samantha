import requests
from bs4 import BeautifulSoup
import re
import json

stopwords = set([stopword.strip('\n') for stopword in open('stopwords.csv')])

def clean(review):
    words = (re.sub('[^a-zA-Z]', " ", review)).split()
    return " ".join([word for word in words if not word in stopwords])

def collectData(url, filename):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    maindiv = soup.find(id="main_container")
    outD = {}
    for i in range(50):
        if i != 0:
            updatedurl = url.split('?')[0] + "?page=" + str(i + 1) + "&" + url.split('?')[1] + "&sort="
            page = requests.get(updatedurl)
            soup = BeautifulSoup(page.content, "lxml")
            maindiv = soup.find(id="main_container")

        reviews = maindiv.find_all('div', class_="user_review")
        textReviews = [clean(r.get_text().encode('ascii', 'ignore').decode('utf-8')) for r in reviews]

        ratings = maindiv.find_all('span', class_='fl')

        starReviews = []
        star = 0.0

        for rating in ratings:
            star = 0.0
            if not rating.get_text().isspace():
                star += 0.5
            stars = rating.find_all('span', class_="glyphicon glyphicon-star")
            star += len(stars)
            starReviews.append(star)

        outD.update(dict(zip(textReviews, starReviews)))
  
    with open(filename, 'w') as fp:
        json.dump(outD, fp, indent=2)

collectData('https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?type=user', 'starwars.json')
collectData('https://www.rottentomatoes.com/m/about_time/reviews/?type=user', 'abouttime.json')
collectData('https://www.rottentomatoes.com/m/taken/reviews/?type=user', 'taken.json')
collectData('https://www.rottentomatoes.com/m/toy_story/reviews/?type=user', 'toystory.json')
collectData('https://www.rottentomatoes.com/m/cloud_atlas_2012/reviews/?type=user', 'cloudatlas.json')
collectData('https://www.rottentomatoes.com/m/1193743-step_brothers/reviews/?type=user', 'stepbrothers.json')
collectData('https://www.rottentomatoes.com/m/saw/reviews/?type=user', 'saw.json')
collectData('https://www.rottentomatoes.com/m/saw_ii/reviews/?type=user', 'saw2.json')
collectData('https://www.rottentomatoes.com/m/titanic/reviews/?type=user', 'titanic.json')
collectData('https://www.rottentomatoes.com/m/pirates_of_the_caribbean_the_curse_of_the_black_pearl/reviews/?type=user', 'piratesofthecaribbean.json')

