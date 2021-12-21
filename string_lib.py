#言葉に注意 文字コード変換->utf-8とか
#(1) asciiコード変換
def changeCharToAscii(c):
    return ord(c)

def changeAsciiToChar(i,add=0):
    return chr(i+add)


#テストコード
#print(changeCharToAscii('a'),changeAsciiToChar(97))

#(1) https://qiita.com/ell/items/6eb48e934a147898d823