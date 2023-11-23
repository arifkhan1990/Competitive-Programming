from os import *
from sys import *
from collections import *
from math import *

def handleAll(n):
    teens = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
    tens = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

    
    def Find(n, s):
        str_ = ""

        if (n > 19):

            str_ += tens[n // 10] + teens[n % 10]

        else:

            str_ += teens[n]

        if (n):

            str_ += s

        return str_

 

    ans = ""
    ans += Find((n // 10000000), "crore ")
    ans += Find(((n // 100000) % 100), "lakh ")
    ans += Find(((n // 1000) % 100), "thousand ")
    ans += Find(((n // 100) % 10), "hundred ")

    if (n > 100 and n % 100):
        ans += "and "

    ans += Find((n % 100), "")

    if (ans == ""):

        ans = "zero"

    return ans

