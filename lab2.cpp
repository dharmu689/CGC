#include <iostream>
#include <cmath>
using namespace std;

// Abstract base class
class Shape {
public:
    virtual double area() const = 0;  // Pure virtual function
};

// Rectangle class derived from Shape
class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double width, double height) : width(width), height(height) {}

    double area() const override {
        return width * height;
    }
};

// Circle class derived from Shape
class Circle : public Shape {
private:
    double radius;

public:
    Circle(double radius) : radius(radius) {}

    double area() const override {
        return M_PI * radius * radius;
    }
};

// Main function demonstrating polymorphism
int main() {
    Shape* shapes[] = { new Rectangle(5, 10), new Circle(7) };

    for (Shape* shape : shapes) {
        cout << "The area is: " << shape->area() << endl;
    }

    // Clean up
    delete shapes[0];
    delete shapes[1];

    return 0;
}




