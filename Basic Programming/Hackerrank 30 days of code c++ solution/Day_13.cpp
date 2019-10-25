/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 13: Abstract Classes
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-abstract-classes/problem
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

class Book{
    protected:
        string title;
        string author;
    public:
        Book(string t,string a){
            title=t;
            author=a;
        }
        virtual void display()=0;
};

class MyBook :  public Book{
 private:
    int price;
    public:
      MyBook(string t,string a,int price):Book(t,a)
          {
          this->price = price;
      }
    void display(){
        cout << "Title: " << title << endl << "Author: " << author << endl << "Price: " << price << endl;
    }
};

int main() {
    string title,author;
    int price;
    getline(cin,title);
    getline(cin,author);
    cin>>price;
    MyBook novel(title,author,price);
    novel.display();
    return 0;
}
