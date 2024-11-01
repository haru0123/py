#! ★★★サーバー立ち上げ(テンプレ)★★★
# cd C:\Users\pcgam\nkz.ac.jp\OHS23-IH22 IA22-NAKAO TAKAGI - SK21_05班 - SK21_05班\StudyBuddy
# env\Scripts\activate
# python app.py


from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.datastructures import ImmutableMultiDict
from datetime import datetime, timedelta
from PIL import Image
from random import randint, randrange
import time
import os
import random
import csv

# csvファイル
filename = "correct.csv"

app = Flask(__name__)

app.secret_key = "app"

app.permanent_session_lifetime = timedelta(minutes=1)

keyName="aaa"


#! ****************************************************
#!       index.html（ログイン画面表示）の処理内容       *
#! ****************************************************
# ホームページ
@app.route('/',methods=["get"])
def index():
    return render_template('index.html')


#! ****************************************************
#!       /c-selectの処理内容       *
#! ****************************************************
@app.route('/c-select',methods=['POST'])
def c_select():
    msg={}
    return render_template('c-select.html',msg=msg)


#! ****************************************************
#!       characterの処理内容       *
#! ****************************************************
@app.route('/character', methods=['POST'])
def character():

    result = request.form
    if keyName not in request.form:
        return render_template("c-select.html")
    session["file"]=result["aaa"]
    print(session)

    

    # # 画像ファイルのパス
    # image_path = session["file"]
    # # 画像の読み込み
    # image = Image.open(image_path)
    # # リサイズ後のサイズを指定。(幅,高さ)
    # new_size = (100,200)
    # # リサイズ
    # resized_image = image.resize(new_size)
    # # ファイル名にタイムスタンプを追加して新しいファイル名を作成
    # timestamp = int(time.time())
    # resized_image_filename = f"resized_image_{timestamp}.jpg"
    # # リサイズされたファイル名を保存
    # resized_image_path = os.path.join(app.config['UPLOAD_FOLDER'],resized_image_filename)
    # resized_image.save(resized_image_path)
    # # セッションにリサイズ後の画像ファイルのパスを保存
    # session["resized_file"] = resized_image_path


    
    return render_template('character.html', result=result,session=session)

#! ****************************************************
#!       lobby_inputの処理内容       *
#! ****************************************************
@app.route('/lobby_input', methods=['POST'])
def lobbyinput():

    result = request.form
    session["charactername"]=result["bbb"]
    print(session)

    return render_template('lobby_input.html', result=result, session=session)

#! ****************************************************
#!       lobby_confirmの処理内容       *
#! ****************************************************
@app.route('/lobby_confirm', methods=['POST'])
def lobbyconfirm():
    result = request.form
    session["playername"]=result["ccc"]
    print(session)
    return render_template('lobby_confirm.html', result=result, session=session)

#! ****************************************************
#!       mainの処理内容       *
#! ****************************************************
@app.route('/main')
def main():
    return render_template('main.html')


#! ****************************************************
#!       NOTEの処理内容       *
#! ****************************************************
@app.route('/NOTE')
def note():
    return render_template('NOTE.html')


#! ****************************************************
#!       NOTE OKの処理内容       *
#! ****************************************************
@app.route('/NOTE OK', methods = ["post"])
def noteok():
    note = request.form['note']
    if note == '':
        return render_template('NOTE.html',note=note)
    else:
        return render_template('NOTE OK.html')
    

#! ****************************************************
#!       NOTE KAKUNINの処理内容       *
#! ****************************************************
@app.route('/NOTE KAKUNIN')
def notekakunin():
    return render_template('NOTE KAKUNIN.html')







#! ****************************************************
#!       NOTE_detail1の処理内容       *
#! ****************************************************
@app.route('/NOTE_detail1')
def NOTE_detail1():
    return render_template('NOTE_detail1.html')





#! ****************************************************
#!       NOTE_detail2の処理内容       *
#! ****************************************************
@app.route('/NOTE_detail2')
def NOTE_detail2():
    return render_template('NOTE_detail2.html')






#! ****************************************************
#!       NOTE_detail3の処理内容       *
#! ****************************************************
@app.route('/NOTE_detail3')
def NOTE_detail3():
    return render_template('NOTE_detail3.html')





#! ****************************************************
#!       NOTE_detail4の処理内容       *
#! ****************************************************
@app.route('/NOTE_detail4')
def NOTE_detail4():
    return render_template('NOTE_detail4.html')





#! ****************************************************
#!       QUSTION INPUTの処理内容       *
#! ****************************************************
# teach画面
@app.route('/QUSTION INPUT')
def question():
    return render_template('QUSTION INPUT.html')


#! ****************************************************
#!       QUSTION INPUT OKの処理内容       *
#! ****************************************************
@app.route('/QUSTION INPUT OK', methods = ["post"])
def questionok():
    question = request.form['question']
    answer = request.form['answer']
    ex = request.form['ex']
    if question == '' or answer == '' or ex == '':
        return render_template('QUSTION INPUT.html',question=question,answer=answer,ex=ex)
    else:
        return render_template('QUSTION INPUT OK.html')

#! ****************************************************
#!       studyの処理内容       *
#! ****************************************************
@app.route('/study', methods=['GET','POST'])
def study():

    question_dict = {
        # IT
        "001":['サービスデスク組織の構造とその特徴のうち、サービスデスクを利用者の近くに配置することによって，言語や文化の異なる利用者への対応，専用要員によるVIP対応などができることを何というか。','ローカルサービスデスク','サービスデスクの組織構造には次のような形態があります。ユーザーのローカルサイト内、若しくは地理的に近い場所に設置されたサービスデスク。担当者の直接派遣が容易であり、ユーザーの問題や改善点を把握しやすい。'],
        "002":['階層構造のモジュール群から成るソフトウェアの結合テストを，上位のモジュールから行う。この場合に使用する，下位モジュールの代替となるテスト用のモジュールを答えよ。','スタブ','ソフトウェア結合テストにおいて、未完成のモジュールの代わりに接合されるテスト用モジュールにスタブとドライバがあります。スタブとはトップダウンテストにおいて未完成の下位モジュールの代わりに結合されるテスト用モジュール。上位モジュールからの呼び出しに対して適切な値を返す役割をもつ。'],
        "003":['共通フレームのプロセスのうち，成果物が利用者の視点から意図された正しいものになっているかどうかを確認するプロセスを答えよ。','妥当性確認プロセス','妥当性確認プロセスは、作成されたソフトウェア作業成果物及びサービスが指定された使用方法に対する要件を満たしているかを確認するプロセスです。'],
        "004":['MTBFを2倍にし，MTTRを半分にすると稼働率は大きくなるか小さくなるか。','大きくなる','2／(2＋1/2)＝2／2.5＝0.8分子が大きくなるので稼働率は大きくなります。'],
        "005":['個人が制作したデジタルコンテンツの閲覧者・視聴者への配信や利用者同士の共有を可能とするものは何か。','CGM','CGM(Consumer Generated Media)は、主にインターネットを利用して消費者やユーザーがその内容を生成する形態のメディアです。不特定多数の個人によって書きこまれる記事や作品をデータベース化してコンテンツとするWebサイトがこれに該当し、ブログやSNS、口コミサイト、Q&Aコミュニティ、写真共有サイトや動画共有サイトなどが代表的な存在です。'],
        # 国語
        "006":['次の文中の「“の”」のうち、１つだけ働きが違うものを１番目～３番目で答えよ。今週“の”土曜日に、駅“の”ホールで、私“の”好きな歌手がコンサートを行う予定だ。','２番目','この文の中で、役割が違う「の」は、「駅のホールで」の中に含まれる２番目です。これは場所を示すための「の」であり、他の「の」は名詞を修飾するためのものです。'],
        "007":['次の“”の動詞の活用形は何か。少しは言うことを“聞け”。','命令形','この文の中で、役割が違う「の」は、「駅のホールで」の中に含まれる２番目です。これは場所を示すための「の」であり、他の「の」は名詞を修飾するためのものです。'],
        "008":['“”の動詞の活用形がほかと異なるものを,次から1つ選びなさい。 "起き"ている "走ろ"う "打っ"た "受け"ます','走ろう','「う」に続いている「走ろ」は「未然形」。「た」に続いている「打っ」,「て」に続いている「起き」,「ます」に続いている「受け」は「連用形」である。「未然形」は“ない·う·よう”などに続く形,「連用形」は“ます·た·て”などに続く形である。'],
        "009":['次の“”の助詞の種類として正しいものを,次から1つ選びなさい。デパートは駅の北側"に"ある。終助詞、接続助詞、格助詞、副助詞','格助詞','直前の「北側」という体言(名詞)に付いて,直後の「ある」に対する連用修飾語を作っているので「格助詞」である。'],
        "010":['次の読みを答えよ “演繹”','えんえき','なし'],
        # 数学
        "011":['(2-3i)-(4-2i)を計算せよ','-2-i','(2-3i)-(4-2i)=2-3i-4+2i=2-4-3i+2i=-2-i()を外して〇i同士と〇同士の係数を計算'],
        # "012":['x³+64を因数分解せよ','(x+4)(x2–4x+16)','x3+64=x3+43=(x+4)(x2–x⋅4+42)=(x+4)(x2–4x+16)'],
        # "013":['次の方程式を解け　x³=8 ','x=2, −1±3–√i ','与式から　x³-8=0左辺を因数分解すると　(x−2)(x²+2x+4)=0よって　x−2=0または　x²+2x+4=0x−2=0 より x=2x²+2x+4=0 より x=−1±3–√i'],
        "014":['log₆4+log₆9 を簡単にせよ。','2','log₆4+log₆9=log₆(4⋅9)=log₆36=log₆6²=2'],
        "015":['|a|=2, |b|=5 で，a  と b  のなす角が60°のとき，内積 a ⋅b  を求めよ','5','a・b=|a||b|cos60∘=2×5×12=5'],
        # 英語
        "016":['次の()を答えよ　He will get his girlfriend ( ) some sandwiches for us.','to make','「彼はガールフレンドに我々のためにサンドイッチを作ってもらうつもりだ」☆get O C「OにCしてもらう」去分詞がくる。OC間の「ガールフレンドがサンドイッチを作る」の主述関係(能動関係)に注目。'],
        "017":['次の()を答えよ　Are you going to keep me ( ) all the morning?','wating','「あなたは私を朝の間中待たせておくつもりですか」☆keep OC「OをCの状態に保つ」。OC間の「私が→待っている」の主述関係(能動関係)に注目し現在分詞のwaitingを選ぶ。keepはSVOCのCの部分にto不定詞や動詞の原形を使うことはできない。'],
        "018":['次の()を答えよ　The death of her son has ( ) her another person.','made','「彼女の息子の死が彼女を別の人間にしてしまった」☆第5文型を作っており、補語が名詞。make OCで「OをCにする」の意味。'],
        "019":['次の()を答えよ　I want you ( ) what time will be convenient for you.','to let me know','「何時が都合がいいか私に知らせて欲しいのですが」☆want O to不定詞「Oに~してほしい」let OC 「OにCしてもらう、させる」(使役動詞)。Cには動詞の原形がくる。'],
        "020":['次の()を答えよ　Please ( ) him call me back as soon as he comes back.','have','「彼が戻ってきたらすぐに私に電話をさせてくれませんか」☆SVOCのCに動詞の原形を使えるのはhaveのみ。have OC「OにCさせる」(使役動詞)。Cの部分には動詞の原形か過去分詞がくる。'],
    }
    value=[]

    num = randint(0, 17)  # 0～の範囲の整数値をランダムに取得
    print(num)  # 2など

    for values in question_dict.values():
        value.append(values)
    return render_template('study.html',value=value,num=num)

#! ****************************************************
#!       正解不正解のの処理内容       *
#! ****************************************************
@app.route('/correct', methods = ["get","post"])
def correct():
    response = request.form['response']
    if response == 'ローカルサービスデスク' or response == 'スタブ' or response == '妥当性確認プロセス' or response == '大きくなる' or response == 'CGM' or response == '２番目' or response == '命令形' or response == '走ろう' or response == '格助詞' or response == 'えんえき' or response == '-2-i' or response == '2' or response == '5' or response == 'to make' or response == 'waiting' or response == 'made' or response == 'to let me know' or response == 'have':
    # if response == 'a':
        return render_template('correct.html',response=response)
    else:
        return render_template('miss.html',response=response)
@app.route('/miss', methods = ["get"])
def miss():
   
    return render_template('miss.html')


#! ****************************************************
#!       personal_charの処理内容       *
#! ****************************************************
@app.route('/test')
def test():
    return render_template('test.html')

#! ****************************************************
#!       データベースの接続処理（＊名前は後で変更）       *
#! ****************************************************
# def con_db():
#           con = mysql.connector.connect(
#                host = 'localhost',
#                user = 'py24user',
#                passwd = 'py24pass',
#                db = 'py24db'
#           )

#           return con


#! ****************************************************
#!       データベース SELECT処理（関数名などは後で変更）       *
#! ****************************************************
# def StudyBuddy_select(sql):
     
#      try:
#           con = con_db() 
#           cur = con.cursor(dictionary=True) 
#           cur.execute(sql) 
#           result = cur.fetchall() 
          
#      except mysql.connector.errors.ProgrammingError as e:
#           print('---DB接続エラー---')
#           print(type (e)) #例外名の出力
#           print(e) #例外内容出力

#      except Exception as e:
#           print('---システム運行システムエラー---')
#           print(type (e)) 
#           print(e) 

        
#      finally:
#           cur.close() 
#           con.close() 
          
#      return result



#! ****************************************************
#!        データベース INSERT処理（関数名などは後で変更）                       *
#! ****************************************************
# def StudyBuddy_execute(sql):
#      res=True
     
#      try:
#           con = con_db() 
#           cur = con.cursor() 
#           cur.execute(sql) 
#           con.commit()
          
#      except mysql.connector.errors.ProgrammingError as e:
#           print('---DB接続エラー---')
#           print(type(e)) 
#           print(e) 
#           res=False

#      except mysql.connector.errors.IntegrityError as e:
#           print('---データ挿入エラー---')
#           print(type (e)) 
#           print(e)
#           res=False

#      except Exception as e:
#           print('---システム運行システムエラー---')
#           print(type (e)) 
#           print(e) 
#           res=False

        
#      finally:
#           cur.close() 
#           con.close() 

#      return res




#! ****************************************************
#!                  サーバー設定                       *
#! ****************************************************
if __name__ == '__main__':
    app.run(host='localhost', port=5000 ,debug=True)