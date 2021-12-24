#言葉に注意 文字コード変換->utf-8とか
##(1) asciiコード変換 ord,chr
def changeCharToAscii(c):
    return ord(c)

def changeAsciiToChar(i,add=0):
    return chr(i+add)

##2 0で文字を埋める→パディングzero fill
def zerofill(s="1234"):
    return s.zfill(8)

##3 文字列の部分一致が簡単にできる
def matchSubstring(s="abcdddxxxd"):
    print('cdd' in s,'dxx' in s,'aci' in s)

## 繰り返しの文字列
def repeatMuchString(s="abc",n=3):
    return s*3


#テストコード

if __name__ =='__main__':
    print(changeCharToAscii('a'),changeAsciiToChar(97))
    print(zerofill())
    matchSubstring()
    print(repeatMuchString())

#1 https://qiita.com/ell/items/6eb48e934a147898d823
#2 https://it-engineer-info.com/language/python/5664/
#3 https://note.nkmk.me/python-str-compare/#:~:text=source%3A%20str_compare.py-,%E9%83%A8%E5%88%86%E4%B8%80%E8%87%B4%3A%20in%2C%20not%20in,%E3%81%A8%20False%20%E3%81%8C%E8%BF%94%E3%81%95%E3%82%8C%E3%82%8B%E3%80%82
