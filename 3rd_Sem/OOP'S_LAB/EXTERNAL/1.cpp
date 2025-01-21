#include<iostream>
#include<string>
using namespace std;

class person
{
private:
    /* data */
    string name;
    int age;
public:
    person(string n, int a) : name(n), age(a){ }
    void display_info()
    {
        cout<<"Name: "<<name<<endl;
        cout<<"Age: "<<age<<endl;
    }
};

class student : public person
{
    int student_id;
    public:
    student(string n, int a, int id) : person(n,a), student_id(id){ }
    void display_info()
    {
        person::display_info();
        cout<<"student_id: "<<student_id<<endl;
    }
};

int main()
{
    student s("Dharmu Kumar",21,1821);
    s.display_info();
    return 0;
}