
import function as fun

#--------------------------------------------------------

#既存のデータを管理する
from moviepy.editor import *

#選手のインスタンス化を行う
#FWの選手たち
yamakawa= fun.person_movie("yamakawa","static/movies/動画１.mp4")
nakayama = fun.person_movie("nakayama","static/movies/動画１.mp4")

#MFの選手たち
koyama =fun.person_movie("koyama","static/movies/動画１.mp4")
amano =fun.person_movie("amano","static/movies/動画１.mp4")
hatanaka =fun.person_movie("hatanaka","static/movies/動画１.mp4")
mano =fun.person_movie("mano","static/movies/動画１.mp4")
kobayasi =fun.person_movie("kobayasi","static/movies/動画１.mp4")
isihara =fun.person_movie("isihara","static/movies/動画１.mp4")
enndou =fun.person_movie("enndou","static/movies/動画１.mp4")
nakayama =fun.person_movie("nakayama","static/movies/動画１.mp4")

#DFの選手たち
sugawara = fun.person_movie("sugawara","static/movies/動画１.mp4")
yamaguti  = fun.person_movie("yamaguti","static/movies/動画１.mp4")
satou = fun.person_movie("satou","static/movies/動画１.mp4")
nagafuzi = fun.person_movie("nagafuzi","static/movies/動画１.mp4")
kawamoto = fun.person_movie("kawamoto","static/movies/動画１.mp4")
koshoji = fun.person_movie("koshoji","static/movies/動画１.mp4")

#GKの選手たち
watanabe = fun.person_movie("watanabe","static/movies/動画１.mp4")

#選手のインスタンスをリストにまとめる
FW_list = [yamakawa,nakayama]
MF_list = [koyama,amano,hatanaka,mano,kobayasi,isihara,enndou,nakayama]  
DF_list = [sugawara,yamaguti,satou,nagafuzi,kawamoto,koshoji]
GK_list = [watanabe]

#------------------------------------------------------------------------

# インストールした「flask」モジュールをインポートする
from flask import Flask, render_template,request


# インスタンス化する
app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

#------------------------------------------------------------------------------

#トップページ
@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("index.html")

#-----------------------------------------------------------------------------

#動画作成ページ
@app.route('/movie_make',methods=["GET","POST"])
def download():
    if request.method == "GET":
        return render_template("movie_make.html")
    elif request.method == "POST":
        return render_template("download.html")

#==================================================================================


#動画作成ページ
@app.route('/download',methods=["GET","POST"])
def movie_make():
    if request.method == "GET":
        return render_template("download.html")
    
    elif request.method =="POST":
        #選択された選手の名前（苗字、ローマ字で格納）
        FW1 = (request.form["FW1"])
        FW2 = (request.form["FW2"])
        LMF = (request.form["LMF"])
        CMF1 = (request.form["CMF1"])
        CMF2 = (request.form["CMF2"])
        RMF = (request.form["RMF"])
        LSB = (request.form["LSB"])
        CB1 = (request.form["CB1"])
        CB2 = (request.form["CB2"])
        RSB = (request.form["RSB"])
        GK = (request.form["GK"])
        
        #各データを収納する(苗字、ローマ字)
        input_name = [FW1,FW2,LMF,CMF1,CMF2,RMF,LSB,CB1,CB2,RSB,GK]

        #該当選手の動画を得てリストとして得る
        movie_list = fun.movie_select(input_name,FW_list,MF_list,DF_list,GK_list)


        final_clip = concatenate_videoclips(movie_list)
        final_clip.write_videofile("static/movies/final_cat.mp4")
        return render_template("download.html")


#---------------------------------------------------------------------------------------



if __name__ == "__main__": #最後に記述する
    app.run(debug=True)