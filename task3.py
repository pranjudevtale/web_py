from task import adventure_movie
import json
# import pprint
data=adventure_movie()

def group_year(movie):
    movie_decad_year={}
    list2 = []
    for index in movie:
        m=int(index["year"])%10
        v=int(index["year"])-m
        if v not in list2:
            list2.append(v) #it is created of list of decade
    #print(list12)
    list2.sort()
    for i in list2:
        movie_list=[]
        for x in movie:
            if int(x["year"])>=i and int(x["year"])<=i+10:               
                movie_list.append(x)
                movie_decad_year[i]=movie_list

            with open("task3.json","w")as f:
                json.dump(movie_decad_year,f,indent=3)
    # return movie_decad_year
# print(data)
# pprint.pprint(data) 
group_year(data)
