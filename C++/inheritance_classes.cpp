#include<iostream>
using namespace std;
class A{
public:
    void show(){cout<<"A function called"<<endl;}
    A(){
        cout<<"Constructor A called"<<endl;
    }
    ~A(){
        cout<<"Destructor A called"<<endl;
    }
};
class B{
public:
    void show(){cout<<"B function called"<<endl;}
    B(){
        cout<<"Constructor B called"<<endl;
    }
    ~B(){
        cout<<"Destructor B called"<<endl;
    }
};
class C:public virtual A,public B{
public:
    C(){
        cout<<"Constructor C called"<<endl;
    }
    ~C(){
        cout<<"Destructor C called"<<endl;
    }
};
int main(){
    C c1;
        c1.show();
}
