from FunctionsPalindromme import *
from Functions import *
bcl = 1

while bcl != 0 : 
    printHeader(title="Est-ce un Palindrome ? ", char="")
    a = lowerCaps (input("Veuillez entrez une phrase: "))
    if is_palindrome(a) ==True:
        print("c'est un palindrome. ")
    else : 
        print("ce n'est pas un palindrome. ")

