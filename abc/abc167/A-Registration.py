# 入力受付
s = input()
t = input()

# 最初の入力に2番目の入力の最後の文字を追加する
str = s + t[-1]

# strとtの比較
if str == t:
    print('Yes')

else :
    print('No')