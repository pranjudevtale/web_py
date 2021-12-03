# from bs4 import BeautifulSoup
# import requests
# import json

# movie_details=[]
# def scrap_movie_details(link):
#     d1={}
#     link_data=requests.get(link)
#     soup=BeautifulSoup(link_data.text,'html.parser')
#     d1["name"]="black panther"
#     movie_bio=soup.find("div",class_="movie_synopis clamp clamp-6 js-clamp").get_text().strip()
#     d1["bio"]=movie_bio
#     title=soup.find_all("div",class_="meta-label subtle")
#     value=soup.find_all("div",class_="meta-value")
    
#     for i in range(len(title)):
#             d1[str(title[i].get_text().strip())[i-1]]=value[i].get_text().strip()
#     movie_details.append(d1)
#     with open("task4.json","w")as f:
#         json.dump(movie_details,f,indent=4)
# scrap_movie_details("https://www.rottentomatoes.com/m/black_panther+2018")
    



