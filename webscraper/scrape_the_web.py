from bs4 import BeautifulSoup
import requests, datetime

# html = input("Enter your url to search: ")
# Url to pull
html = "http://www.startribune.com/"

now_time = datetime.datetime.now()

# Request html from page
r = requests.get(html)

# Pass html to BeautifulSoup for beautification
soup = BeautifulSoup(r.text, 'html.parser')

teaser_title = soup.find_all('h3', limit=2)
print('Recent Headline: ')
print(teaser_title[1].text)

headline_file = open('headlines.txt', 'a')

headline_file.write(teaser_title[1].text + ' - ' + str(now_time) + '\n')

headline_file.close()

# soup = BeautifulSoup(open("htmlfiles\star_tribune.html"), 'html.parser')
# # soup = BeautifulSoup("<html>data</html>")
#
# print("Title: ")
# print(soup.title.string)
