ji#include <iostream>
#include <string>
using namespace std;

// Base class
class Person {
protected:
    string name;
    int age;

public:
    Person(string name, int age) : name(name), age(age) {}

    void display_info() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

// Derived class
class Student : public Person {
private:
    string student_id;

public:
    Student(string name, int age, string student_id) 
        : Person(name, age), student_id(student_id) {}

    void display_student_info() {
        display_info();  // Calling base class method
        cout << "Student ID: " << student_id << endl;
    }
};

// Main function
int main() {
    Student student("Alice", 20, "S12345");
    student.display_student_info();

    return 0;
}



