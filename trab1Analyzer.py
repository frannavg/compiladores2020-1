#Código lab1 Compiladores // Breno Peixoto e Francisco Navarrete

import re
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer

#Check if the string starts with "The" and ends with "Spain":
'''
txt = "00000        0000000 99999999 0000000000"
#x = re.search("^The.*Spain$", 'rain')
x=re.search("^[0-9]*", txt)
print(x.group())
'''
strcasoteste=("""public class Puppy { 
  
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

'''Estratégia do analisador

    Ler ids, numeros inteiros e flutuantes, 
    strings(""), separadores e operadores

    Definir as keywords após isso
'''

#b=str.replace(' ','')
#print(b)
numerodecimal = "0|[1-9][0-9]*"
sep = "\{\}\[\]\(\)\.;,...@::"
op = "[=][>][<][!][~][\?][:][->][==][>=][<=][!=][&&][||][\+\+][--][\+][-][\*][/][&][|][^][%][<<][>>][>>>][+=][-=][\*=][/=][&=][|=][^=][%=][<<=][>>=][>>>=]"

'''teste = RegexpTokenizer(r"[_a-zA-Z][_a-zA-Z\d]*"
                        rf"|0|[1-9]\d*|[(-)]|[[{numerodecimal}[[.][\d]*]"
                        r"|[[.][\d]+]][[e|E][+|-]0|[1-9][\d]*]]"
                        r"|[[0|[1-9][\d]*][[e|E][+|-]][0|[1-9][\d]*]")'''

str=('''(000 1111 9999 12.34 29.09 0.0 .15 3.14151643 1F
    1D 1.0E1 1E -1E 1.09e10f __aaaa; "asad" gg ''')

teste = RegexpTokenizer(
r"[_a-zA-Z][_a-zA-Z\d]*"
rf"|{numerodecimal}\.[0-9]+[eE]?[fFdD]?"
r"|\.?[\+-]?[0-9]+[eE]?[fFdD]?"
rf"|{numerodecimal}"
r"|\".\""
rf"|{sep}"
rf"|{op}")


#teste = RegexpTokenizer("")
#teste = RegexpTokenizer("\w+|\$[\d\.]+|\S+")
a=teste.tokenize(str)
b=teste.tokenize(strcasoteste) 
print(a)
print(len(a))

print(b)
print(len(b))

'''
if (x):
  print("YES! We have a match!")
else:
  print("No match")
'''
