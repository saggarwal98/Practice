#include<iostream>
using namespace std;
class A{
    int a;
    char name[15];
    int rollno;
public:
    void getdata(){
        cin>>a;
    };
    void putdata(){
        cout<<"\n"<<a;
    };
    void calc(A a1, A a2){
        cout<<"\n"<<a1.a+a2.a;
    }
    A(){
        cout<<"\nClass A Contructor caled";
    }
    ~A(){
        cout<"\nDestructor A called";
    }
};
class B:public A{
public:
    B(){
        cout<<"\nClass B Contructor caled";
    }
    ~B(){
        cout<"\nDestructor B called";
    }
};
class C:public B{
public:
    C(){
        cout<<"\nClass C Contructor caled";
    }
    ~C(){
        cout<"\nDestructor C called";
    }
};
int main(){
    /*int n;
    cin>>n;
    A obj[n];
    for(int i=0;i<n-1;i++){
        obj[i].getdata();
    }
    for(int i=0;i<n-1;i++){
        obj[i].putdata();
    }
    obj[n-1].calc(obj[n-3],obj[n-2]);*/
    C c1;
    return 0;
}
