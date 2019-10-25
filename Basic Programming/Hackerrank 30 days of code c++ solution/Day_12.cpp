/*                    Name : Arif Khan
                      Judge: HACKERRANK
                      University: Primeasia University
                      problem: Day 12: Inheritance
                      Difficulty: Easy
                      Problem Link: https://www.hackerrank.com/challenges/30-inheritance/problem
*/

#include <iostream>
#include <vector>

using namespace std;


class Person{
	protected:
		string firstName;
		string lastName;
		int id;
	public:
		Person(string firstName, string lastName, int identification){
			this->firstName = firstName;
			this->lastName = lastName;
			this->id = identification;
		}
		void printPerson(){
			cout<< "Name: "<< lastName << ", "<< firstName <<"\nID: "<< id << "\n"; 
		}
	
};

class Student :  public Person{
	private:
		vector<int> testScores;  
	public:
        Student(string firstname, string lastname,int identification,vector<int> inArray)
            :Person(firstname,lastname, identification)
            {
            this-> testScores=inArray;
        }
  		// Write your constructor
    char calculate(){
        int sum = 0,i;
        char ch ;
        for( i = 0; i<testScores.size() ;i++)
             sum += testScores[i];
        sum/=i;
        if(sum < 40)
            ch = 'T';
        else if(sum < 55)
            ch = 'D';
        else if(sum < 70)
            ch = 'P';
        else if(sum < 80)
            ch = 'A';
        else if(sum < 90)
            ch = 'E';
        else
            ch = 'O';
            
            return ch;
    }
};


int main() {
	string firstName;
  	string lastName;
	int id;
  	int numScores;
	cin >> firstName >> lastName >> id >> numScores;
  	vector<int> scores;
  	for(int i = 0; i < numScores; i++){
	  	int tmpScore;
	  	cin >> tmpScore;
		scores.push_back(tmpScore);
	}
	Student* s = new Student(firstName, lastName, id, scores);
	s->printPerson();
	cout << "Grade: " << s->calculate() << "\n";
	return 0;
}