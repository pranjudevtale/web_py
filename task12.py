import requests
import bs4
raw=requests.get("https://www.rottentomatoes.com/title/tt0066763/fullcredits?ref_=_tt_cl_sm#cast")
print(raw)

soup=bs4.BeautifulSoup(raw.text,'html.parser')
table_data=soup.find('table',class_='cast_list')
actors=table_data.findall('td',class_="")

# print(actors)
actot=actors[0]
movie_id=actors.find('a').get('href')[6:15]
name=actors.getText.strip()

# print(movie_id)
actors.getText()
actors.getText.strip()


