# from task5 import*
# import json
# from pprint import pprint


# def analyse_movie_gener(movie_list):
#     gener_list=[]
#     for movie in get_movie_list_details:
#         json_2_dict=json.load(movie)
#         gener=json_2_dict['gener']
#         for i in gener:
#             if i not in gener_list:
#                 gener_list.append(i)
#     analyse_gener={gener_type:0 for gener_type in gener_list}
#     for gener_type in gener_list:
#         for movie in movie_list:
#             json_2_dict=json.load(movie)
#             if gener_type in json_2_dict['gener']:
#                 analyse_gener[gener_type]+=1
#     return analyse_gener
# gener_analysis=analyse_movie_gener(get_movie_list_details)

# pprint.pprint(analyse_movie_gener)

# name="shalini"
# def get():
#     name="madhu"
#     print(name)
# get()
# print(name)

# def num(a):
#     i=0
#     sum=0
#     count=0
#     while i<len(a):
#         sum=sum+a[i]
#         count=count+1
#         i=i+1
#     print(sum)
#     print(count)
#     avg=sum/count
#     print(avg)
# num([8,9,10,11,12,14,18])

num=int(input("enter the number"))
i=0
while i<num:
    print(num%10)