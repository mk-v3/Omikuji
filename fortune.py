import random
import tkinter

def draw_fortune():
    # おみくじ運リスト
    fortune_lists = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '最凶']
    # 各運勢の重みづけ
    fortune_weights = [1, 2, 3, 4, 3, 2, 1]
    #ランダムで1つ引く
    result = random.choices(fortune_lists, k=1, weights=fortune_weights)[0]
    #結果を出力する print("今日の運勢は" + result + "です。")
    result_label.config(text="今日の運勢は" + result + "です。")
    result_label.pack()

#ウィンドウ
root = tkinter.Tk()
root.title("Omikuji")
root.geometry("200x200")

#おみくじを引くボタン
button = tkinter.Button(text="おみくじを引く", width=50, command=draw_fortune)
button.pack()

result_label = tkinter.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

#ウィンドウを表示
root.mainloop()