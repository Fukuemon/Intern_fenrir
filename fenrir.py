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
            if not stack:  # 一番最初から閉じ括弧が来た場合
                return False  # 間違い
            elif bra_val == stack[-1]:  # 閉括弧と対応する開括弧がスタックの先頭にあったら
                stack.pop()
                continue
            elif bra_val != stack.pop():  # スタックの先頭の括弧が閉括弧に対応していなかったら
                return False  # 間違い

    return True


s = "({)}"
print(isValid(s))
s = "()"
print(isValid(s))
s = "([]){}"
print(isValid(s))
s = "}()[]{"
print(isValid(s))