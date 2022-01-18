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

##4 文字列の一部変更 
# 文字列の参照は簡単にできるが中身を直接書き換えることはできない e.g. A[0]="A"
def changeSubString(start=3,s="abbbbbs",subs="ooo"):
    return s[0:start]+ subs + s[start+len(subs):len(s)]

##5 文字列の書式
# 穴埋め式で文字列を補完できる
from datetime import datetime 
def string_format1(s="hello"):
    today = datetime.now().strftime("%Y%m%d")
    output_str = "Today is {} {} Guys".format(today,s)
    return output_str

# 小数点の切り捨てが簡単に行える+ナンバリングに対応
def string_format2(f1=3.1415, i2=3):
    output_str = "PI is {0:.2f} or {1:.1f}".format(f1,i2)
    return output_str

# 幅をうめるのに対応
def string_format3(n=10):
    #str は右を空白で埋める
    str1="{:10}".format("this")
    str2="{:10}".format("is")
    str3="{:10}".format("it")
    print(str1,str2,str3)
    #左にパディング
    str1="{:>10}".format("this")
    str2="{:*>10}".format("is")
    str3="{:>10}".format("it")
    print(str1)
    print(str2)
    print(str3)
    #intは左を空白で埋める
    i1="{:5d}".format(123)
    i2="{:5d}".format(4433)
    i3="{:5d}".format(11223)
    print(i1)
    print(i2)
    print(i3)

#テストコード
if __name__ =='__main__':
    print(changeCharToAscii('a'),changeAsciiToChar(97))
    print(zerofill())
    matchSubstring()
    print(repeatMuchString())
    print(changeSubString())
    print(string_format1())
    print(string_format2())
    string_format3()

#1 https://qiita.com/ell/items/6eb48e934a147898d823
#2 https://it-engineer-info.com/language/python/5664/
#3 https://note.nkmk.me/python-str-compare/#:~:text=source%3A%20str_compare.py-,%E9%83%A8%E5%88%86%E4%B8%80%E8%87%B4%3A%20in%2C%20not%20in,%E3%81%A8%20False%20%E3%81%8C%E8%BF%94%E3%81%95%E3%82%8C%E3%82%8B%E3%80%82
#4 https://minus9d.hatenablog.com/entry/20130528/1369745960
#5 https://gammasoft.jp/blog/python-string-format/