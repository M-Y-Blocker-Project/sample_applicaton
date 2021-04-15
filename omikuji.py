import tkinter as tk
import random

def omikuji():
    list_kuji =  ["Good Luck!","Wasted!"]
    result = random.choice(list_kuji)
             # 明日の予定ラベルにを表示
    response_area.configure(text=result)

#=================================================
# 画面描画用の関数
#=================================================
def run():
    # グローバル変数を使用するための記述
    global response_area

    # メインウィンドウを作成
    root = tk.Tk()
    # ウィンドウのタイトルを設定
    root.title('おみくじ')

    # キャンバスの作成
    canvas = tk.Canvas(width = 600,height = 400)
    canvas.pack()
    img = tk.PhotoImage(file = 'mentos_tea.gif')
    canvas.create_image(0,0,image = img,anchor = tk.NW)

    # 応答エリアを作成
    response_area = tk.Label(width=66,height=5,bg='gray')
    response_area.pack()

    # ボタンの作成
    button = tk.Button(text='  おみくじ　　',command=omikuji)
    button.pack()

    def fix():
        a = root.winfo_geometry().split('+')[0]
        b = a.split('x')
        w = int(b[0])
        h = int(b[1])
        root.geometry('%dx%d' % (w+1,h+1))
    root.update()
    root.after(0, fix)

    # メインループ
    root.mainloop()

#=================================================
# プログラムの起点
#=================================================
if __name__  == '__main__':
    run()

#コマンドプロンプトで　$pyinstaller omikuji.py --onefile と入力すれば exeファイルがdistの中に完成する。
