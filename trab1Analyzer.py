#Código lab1 Compiladores // Breno Peixoto e Francisco Navarrete
#
import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer
import sys

strcasoteste1=""
for line in sys.stdin:
    if 'Exit' == strcasoteste1.rstrip():
        break
    strcasoteste1=strcasoteste1+line


numerodecimal = "0|[1-9][0-9]*"
sep = "[\{]|[\}]|[\[]|[\]]|[\(]|[\)]|[\.]|[;]|[,]|[@]|[::]"
op = "[<]|[!]|[~]|[\?]|[:]|[->]|==|[=][>]|&&|\|\||\+\+|[\+]|[-]|[\*]|[/]|[&]|[|]|[\^]|[%]"

op_complexo=">>>|\+=|-=|\*=|/=|&=|\|=|\^=|%=|<<=|>>=|>>>=|>=|->|<=|!=|\-\-|<<|>>"

teste = RegexpTokenizer(
r"[_a-zA-Z][_a-zA-Z\d]*"
rf"|{numerodecimal}\.[0-9]+[eE]?[fFdD]?"
r"|\.?[\+-]?[0-9]+[eE]?[fFdD]?"
rf"|{numerodecimal}"
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

caracfloat = ['.', 'e', 'E', 'f', 'F', 'd', 'D']

for tok in tk:
    primeiro = tok[0]
    if primeiro == chr(34):
        print ("STRING " + tok)
    elif tok in reservedKeywords:
        print (tok)
    elif (primeiro >= 'a' and primeiro <= 'z') or (primeiro >= 'A' and primeiro <= 'Z') or primeiro == '_':
        print ("ID " + tok)
    elif (primeiro >= '0' and primeiro <= '9') and tok not in caracfloat:
        print ("NUM_DECIM " + tok)
    elif tok in caracfloat and len(tok) >= 2:
        print ("FLOAT_DECIM " + tok)
    else:
        print (tok)
