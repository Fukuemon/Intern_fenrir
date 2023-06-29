def isValid(s):
    # 各鉤括弧に対応した辞書
    brackets = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    # スタック
    stack = []

    for bra in s:
        if bra in brackets.values():  # 開括弧の場合
            stack.append(bra)  # スタックに入れる
        elif bra in brackets.keys():  # 閉括弧の場合
            bra_val = brackets[bra]  # 対応する開括弧
            if bra_val == stack.pop(): # 閉括弧と対応する開括弧がスタックの先頭にあったら
                pass
            elif bra_val != stack.pop():  #
                return False
            elif stack == []:  # 一番最初から閉じ括弧が来た場合
                return False  # 間違い
    return True


s = "({)}"
print(isValid(s))
s = "()"
print(isValid(s))
s = "([]){}"
print(isValid(s))