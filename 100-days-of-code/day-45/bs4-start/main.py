from bs4 import BeautifulSoup
from requests import get

#--------------------FROM LOCAL PAGE --------------------#
# with open(file="./website.html", mode="r") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify()) #Entire html code

# print(soup.title) # title tag
# print(soup.title.name) #Tag name
# print(soup.title.string) # string inside title tag

# print(soup.a) #first anchor tag
# print(soup.li) #first list item
# print(soup.p) #first paragraph

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)


# for tag in all_anchor_tags:
#     print(tag.getText()) # get text
#     print(tag.get("href")) #get link

# heading = soup.find(name="h1", id="name") #get particular element
# print(heading)

# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading)
# print(h3_heading.get_text())

# company_url = soup.select_one(selector="p a") #Select by tag
# print(company_url)

# name = soup.select_one(selector="#name") #Select by id
# print(name)

# headings = soup.select(selector=".heading") #Select by class
# print(headings)

#--------------------FROM LIVE PAGE --------------------#
response = get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = []
article_texts = []
article_links = []

articles_span = soup.find_all(name="span", class_="titleline")
for article in articles_span:
    article_temp = article.find("a")
    article_text = article_temp.getText()
    article_link = article_temp.get("href")
    
    articles.append(article_temp)
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_index = article_upvotes.index(max(article_upvotes))

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])
