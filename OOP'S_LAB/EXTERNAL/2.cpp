#include<iostream>
#include<cmath>
using namespace std;

class shape
{
    public:
    virtual double area() const = 0;
};

class rectangle : public shape
{
    private:
    double width,height;
    public:
    rectangle(double width, double height) : width(width), height(height) { }
    double area() const
    {
    return width*height;
    }
};
class circle : public shape
{
    double radious;
    public:
    circle(double radious) : radious(radious) { }
    double area() const
    {
        return M_PI*radious*radious;
    }
};

int main()
{
    shape* shapes[] = {new rectangle(5,10), new circle(7)};
    for(shape* shape : shapes)
    {
        cout<<"the area is: "<<shape ->area()<<endl;
    }
    delete shapes[0];
    delete shapes[1];
    return 0;
}