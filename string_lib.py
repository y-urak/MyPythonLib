#言葉に注意 文字コード変換->utf-8とか
##(1) asciiコード変換 ord,chr
def changeCharToAscii(c):
    return ord(c)

def changeAsciiToChar(i,add=0):
    return chr(i+add)

##2 0で文字を埋める→パディングzero fill
def zerofill(s="1234"):
    return s.zfill(8)

#テストコード

if __name__ =='__main__':
    print(changeCharToAscii('a'),changeAsciiToChar(97))
    print(zerofill())

#(1) https://qiita.com/ell/items/6eb48e934a147898d823
#(2) https://it-engineer-info.com/language/python/5664/