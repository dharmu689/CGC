#include<iostream>
using namespace std;

class base
{
    public:
    void show()
    {
        cout<<"Base Class";
    }
};

class Derived : public base
{
    public:
   void show()
    {
        cout<<"Derived Class";
    }
};

int main()
{
    Derived d;
    d.show();
}