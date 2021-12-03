
from bs4 import BeautifulSoup
import requests
import json
import pprint

def adventure_movie():
    adventure_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    adventure_api=requests.get(adventure_url)
    htmlcontent=adventure_api.content
    soup=BeautifulSoup(htmlcontent,"html.parser")
    table_tag=soup.find("table",class_="table")
    tr=table_tag.find_all("tr")
    top_movie=[]
    serial_no=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text()
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in  movie_rating:
            rating=rate.get_text().strip()
        movie_name=i.find_all("a",class_="unstyled articleLink")
        # print(movie_name)
        for name in movie_name:
            title=name.get_text().strip()
            list=title.split()
            year=list[-1][1:5]
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            for l in range(name_lenght):
                name+=""
                name+=list[l]
            movie_name=name
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie_URL":"","year":""}
            details["movie_rank"]=rank
            details["movie_rating"]=rating
            details["movie_name"]=movie_name
            details["movie_reviews"]=reviews
            details["movie URL"]=movie_link
            details["year"]=year1
            top_movie.append(details.copy())
        details={'position':'',"name":'','year':'','rating':'','url':''}
        with open("task1.json","w") as file:
            json.dump(top_movie,file,indent=2)
        return top_movie

pprint.pprint(adventure_movie)