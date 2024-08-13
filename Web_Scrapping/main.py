from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

all_spans = soup.find_all(name="span", class_="titleline")

all_scores = soup.find_all(name="span", class_="score")

articles_title = [a.find('a').getText() for a in all_spans]
articles_links = [a.find('a').get("href") for a in all_spans]
articles_scores = [int(a.getText().split()[0]) for a in all_scores]

print(articles_title)
print(articles_links)
print(articles_scores)

index = articles_scores.index(max(articles_scores))

print(index)

print(articles_title[index])
print(articles_links[index])
print(articles_scores[index])






# for i in range(len(titles)):
#     if i % 2 == 0:
#         print(f"{int((i/2)+1)}. {titles[i].getText()} - {titles[i].get('href')}")


















# import lxml

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'lxml.parser')
# soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup)
# print(soup.prettify())

# return first of concurrency
# print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# class_section = soup.find(name="h3", class_="heading")
# print(class_section)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# byid = soup.select_one(selector="#name")
# print(byid)
#
# byclass = soup.select(selector=".heading")
# print(byclass)

