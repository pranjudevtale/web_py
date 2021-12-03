from task5 import adventure_movie
import json
data=adventure_movie
def movies_by_director(movie_detailsLst):
    movie_dict={}
    for dic in movie_detailsLst:
        for direc in dic["director"]:
            if direc not in movie_dict:
                movie_dict[direc]=1
            else:
                movie_dict[direc]+=1
    op=open("task7.json","w")
    op.write(json.dumps(movie_dict,indent=4))
    op.close()
    return movie_dict
movies_by_director(data)

