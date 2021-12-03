import json
def movie_directors():
    file2=open("task5.json","r")
    h=json.load(file2)
    # print(h)
    list=[]
    for i in h:
        if i["original language:"]not in list:
            list.append(i["original launguage:"])
    dict8={}
    list9=[]
    for k in list:
        i=0
        count=0
        while i<len(h):
            if k==h[i]["original launguage:"]:
                count+=1
            i+=1
        dict8.update({k:count})
    list.append(dict8)
    with open("task6.json","w")as file:
        json.dump(dict8,file,indent=4)
    return dict8
movie_directors()
