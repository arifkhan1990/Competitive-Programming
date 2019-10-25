#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 13: Abstract Classes
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-abstract-classes/problem
#

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    price = 0
    def __init__(self,title,author,price):
        super(Book,self).__init__()
        self.price = price
    def display(self):
        print('Title: %s'%title)
        print('Author: %s'%author)
        print('Price: %d'%price)

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()