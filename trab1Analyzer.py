#Código lab1 Compiladores // Breno Peixoto e Francisco Navarrete

import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer

strcasoteste1=("""public class Puppy {

    int puppyAge;

    public Puppy(String name) {
        System.out.println("Name chosen is :" + name );
    }

    public void setAge( int age ) {
        puppyAge = age;
    }

    public int getAge( ) {
        System.out.println("Puppy's age is :" + puppyAge );
        return puppyAge;
    }

    public static void main(String []args) {
        Puppy myPuppy = new Puppy( "tommy" );

        myPuppy.setAge( 2 );

        myPuppy.getAge( );

        System.out.println("Variable Value :" + myPuppy.puppyAge );
    }
}""")

str=('''(000 1111 9999 12.34 29.09 0.0 .15 3.14151643 1F
    1D 1.0E1 1E -1E 1.09e10f __aaaa; "asad" gg ''')


'''#Estratégia do analisador#

    Regex para ids, numeros flutuantes e inteiros,
    strings(""), separadores e operadores

    Definir as keywords após isso
'''

numerodecimal = "0|[1-9][0-9]*"
sep = "[\{]|[\}]|[\[]|[\]]|[\(]|[\)]|[\.]|[;]|[,]|[@]|[::]"
op = "[=]|[>]|[<]|[!]|[~]|[\?]|[:]|[->]|[==]|[>=]|[<=]|[!=]|[&&]|[||]|[\+\+]|[--]"
"|[\+]|[-]|[\*]|[/]|[&]|[|]|[\^]|[%]|[<<]|[>>]|[>>>]|[\+=]|[-=]|[\*=]|[/=]|[&=]|[|=]|[\^=]|[%=]|[<<=]|[>>=]|[>>>=]"


teste = RegexpTokenizer(
r"[_a-zA-Z][_a-zA-Z\d]*"
rf"|{numerodecimal}\.[0-9]+[eE]?[fFdD]?"
r"|\.?[\+-]?[0-9]+[eE]?[fFdD]?"
rf"|{numerodecimal}"
r'|["].*?["]'
rf"|{sep}"
rf"|{op}")


tk=teste.tokenize(str)
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