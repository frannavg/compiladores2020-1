#Código lab1 Compiladores // Breno Peixoto e Francisco Navarrete #

import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer
import sys

strcasoteste1=""
for line in sys.stdin:
    if 'Exit' == strcasoteste1.rstrip():
        break
    strcasoteste1+=line


numerodecimal = "0|[1-9][0-9]*"
sep = "[\{]|[\}]|[\[]|[\]]|[\(]|[\)]|[\.]|[;]|[,]|[@]|::"
op = "[<]|[!]|[~]|[\?]|[:]|[->]|==|[=]|[>]|&&|\|\||\+\+|[\+]|[-]|[\*]|[/]|[&]|[|]|[\^]|[%]"

op_complexo=">>>=|\+=|-=|\*=|/=|&=|\|=|\^=|%=|<<=|>>=|>>>|>=|->|<=|!=|\-\-|<<|>>"

teste = RegexpTokenizer(
r"[_a-zA-Z][_a-zA-Z\d]*"
r"|[-\+]?\d+\.\d+[eE]?[-\+]?\d+[DdFf]?"
rf"|[-\+]?\d+[eE]?[-\+]?\d+[DdFf]?"
rf"|\.\d+[eE]?[-\+]?\d+[DdFf]?"
rf"|[-\+]?{numerodecimal}"
r'|["].*?["]'
rf"|{op_complexo}"
rf"|{sep}"
rf"|{op}")


tk=teste.tokenize(strcasoteste1)

reservedKeywords = ["abstract", "continue", "for", "new", "switch",
"assert", "default", "if", "package", "synchronized",
"boolean", "do", "goto", "private", "this",
"break", "double", "implements", "protected", "throw",
"byte", "else", "import", "public", "throws",
"case", "enum", "instanceof", "return", "transient",
"catch", "extends", "int", "short", "try",
"char", "final", "interface", "static", "void",
"class", "finally", "long", "strictfp", "volatile",
"const", "float", "native", "super", "while", "_"]

chrf = ['.', 'e', 'E', 'f', 'F', 'd', 'D']

#print (tk)

for tok in tk:
    primeiro = tok[0]
    if primeiro == chr(34):
        print ("STRING " + tok)
    elif tok in reservedKeywords:
        print (tok)
    elif (primeiro >= 'a' and primeiro <= 'z') or (primeiro >= 'A' and primeiro <= 'Z') or primeiro == '_':
        print ("ID " + tok)
    elif ((chrf[0] in tok) or (chrf[1] in tok) or (chrf[2] in tok) or (chrf[3] in tok) or (chrf[4] in tok) or (chrf[5] in tok) or (chrf[6] in tok)) and (len(tok) >= 2):
        print ("FLOAT_DECIM " + tok)
    elif (primeiro >= '0' and primeiro <= '9'):
        print ("NUM_DECIM " + tok)
    else:
        print (tok)

print (len(tk))
