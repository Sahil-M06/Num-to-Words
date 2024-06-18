# coding: utf-8

"""
Number to Words by Sahil Mishra

Program takes an integer as an input and returns the word representation of the integer.

Theoretical limit : Constrained only by available memory

Practical limit : Works upto 9.99 x 10^36

The limit can be increased by adding more words "places" tuple. The words are repesentation of number of 10^3n form
                where n is an integer, n=1,2,3,4,....

"""

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=ini_lin*10+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!+0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    word=intia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=ini_lin*10+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    word=intia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=ini_lin*10+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    word=intia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=ini_lin*10+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    word=initia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=ini_lin*10+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)
print(new_lin,ini_lin)
if num==0:
    print("Zero")
else:
    word=initia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)
print(new_lin,ini_lin)
if num==0:
    print("Zero")
else:
    word=initia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    return word

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)
print(new_lin,ini_lin)
if num==0:
    print("Zero")
else:
    word=initia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    print(word)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)
print(new_lin,ini_lin)
if num==0:
    print("Zero")
else:
    word=initia_tens_place()
    print(word)
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
        new_lin[i+1]=0
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)
print(new_lin,ini_lin)
if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
        new_lin[i+1]=0
    print(ini_lin)
    print(new_lin)
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]<2 and lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]<2 and lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin)
    word=" ".join(word.split()).title()
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And;,'and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

get_ipython().run_line_magic('save', 'word_to_num.py')
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

get_ipython().run_line_magic('save', 'word_to_num.py')
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("","ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("","ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("","ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("","ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        else:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("","ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=(ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

get_ipython().run_line_magic('save', 'word_to_num.py')
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 and new_lin[i+2]!=0:
                new_lin{i}+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

get_ipython().run_line_magic('save', 'word_to_num.py')
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 and new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 and new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

for i in range (1000,2000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print("Zero")
    else:
        initia_tens_place()
    
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=" "+places[counter]
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=" "+places[counter]
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            if new_lin[i-2]!=0:
                new_lin[i]=" "+places[counter]
            else:
                new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            if new_lin[i-2]!=0:
                new_lin[i]=" "+places[counter]
            else:
                new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            if new_lin[i-2]!=0:
                new_lin[i]=" "+places[counter]
            else:
                new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if new_lin[i+1]!=0 or new_lin[i+2]!=0:
                new_lin[i]+= " and "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split()).replace('And','and')
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
        else:
            new_lin[i]=""
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 
            new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (1000):
    num=int(input("enter number: "))
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num(186,186+186):
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num(186,186*2):
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num(1000,100000):
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (1000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (186,186*2):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

for i in range (1000,100000):
    num=i
    
    ini_lin=[int(i) for i in str(num)]
    new_lin=list(ini_lin)
    
    if num==0:
        print(f"{num} = Zero")
    else:
        print(num,end=" = ")
        initia_tens_place()
    

#%save word_to_num.py
#initializing basic words

ones=("","one","two","three","four","five","six","seven","eight","nine")
teens=("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty")
tens=("","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
places=("","thousand","million","billion","trillion","quadrillion","quintillion"
        ,"sextillion","septillion","nonillion","undecillion")   #expandable


def initia_tens_place():
    for i in range(-2,-len(ini_lin)-1,-3):
        if ini_lin[i]<2 and ini_lin[i]!=0:
            new_lin[i]=(ini_lin[i]*10)+ini_lin[i+1]
            new_lin[i+1]=0
        
    initia_hund_place()

def initia_hund_place():
    counter=0
    for i in range(-3,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" hundred "
            if ini_lin[i+1]==0 and ini_lin[i+2]==0 :
                new_lin[i]+=" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    initia_ones_place()


def initia_ones_place():
    counter=0
    for i in range (-1,-len(ini_lin)-1,-3):
        if new_lin[i]!=0:
            new_lin[i]=ones[ini_lin[i]]+" "+places[counter]
        else:
            new_lin[i]=""
        counter+=1
    final_tens_place()

def final_tens_place():
    counter=0
    for i in range(-2,-len(ini_lin)-1,-3):
        if new_lin[i]>=10:
            new_lin[i]=teens[new_lin[i]%10]+" "+places[counter]
        elif new_lin[i]<10:
            new_lin[i]=tens[new_lin[i]]
        counter+=1
    word_of_num()

def word_of_num():
    word=" ".join(i for i in new_lin).title()
    word=" ".join(word.split())
    print(word)

num=int(input("enter number: "))

ini_lin=[int(i) for i in str(num)]
new_lin=list(ini_lin)

if num==0:
    print("Zero")
else:
    initia_tens_place()
    
