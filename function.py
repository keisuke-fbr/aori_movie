from moviepy.editor import *

# 人のクラスを作成
class Movie:
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie

#動画のパスを与えることで動画を読み込み、名前と紐づけてインスタンス化を行う
def person_movie(name,path):
    video = VideoFileClip(path)
    return Movie(name,video)


#入力された選手名リストと既存のデータリストから適切な動画リストを返す関数
def movie_select(input_name,list1,list2,list3,list4):
    movie_list = []

    for i in input_name:
        if add_list(i,list1) != 0:
            movie_list.append(add_list(i,list1))
            continue
        
        if add_list(i,list2) != 0:
            movie_list.append(add_list(i,list2))
            continue

        if add_list(i,list3) != 0:
            movie_list.append(add_list(i,list3))
            continue

        if add_list(i,list4) != 0:
            movie_list.append(add_list(i,list4))
            continue
    
    return movie_list

def add_list(input_name,list):
    for k in list:
        if k.name == input_name:
            return k.movie
    return 0
