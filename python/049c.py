s = input()[::-1]

words = ["maerd", "remaerd", "esare", "resare"
]

while len(s) > 0:
    matched = False
    for w in words:
        if s.startswith(w):
            s = s[len(w):]
            matched = True
            break
    if not matched:
        print("NO")
        exit()
print("YES")


"startswith() メソッドは、文字列が特定の文字や文字列で始まっているかを判定するためのメソッドです。引数に指定した文字列が、対象の文字列の先頭に存在する場合は True を返し、そうでない場合は False を返します。"