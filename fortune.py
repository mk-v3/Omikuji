import random

#おみくじ運リスト
fortune_lists = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "最凶"]

#各運勢の重みづけ
fortune_weights = [1, 2, 3, 4, 3, 2, 1]

#ランダムで1つ引く
result = random.choices(fortune_lists, k=1, weights=fortune_weights)[0]

#結果を出力する
print("今日の運勢は" + result + "です。")