#include<iostream>
//#include<stdio.h>
#include<stdlib.h>
using namespace std;
//void increment(int *a){
    //cout<<(sizeof(a)/sizeof(a[0]));

  //  *a+=1;
    //cout<<"\nOperation done";
//    return *a;
//}
int dosomething(int a[]){
    cout<<"\n"<<sizeof(a);
    cout<<"\n"<<sizeof(a[0]);
    cout<<"\n"<<a[0]++;
    cout<<"\n"<<a[1]++;
    cout<<"\n"<<a[0];
    return *a;
}
void swap(int *a, int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
    cout<<"\na:"<<*a;
    cout<<"\nb:"<<*b;
}
void bitwiseor(int a,int b){
    cout<<(a|b);
}
int main(){
        /*char a[][10]={"hello","guys"};
        for(int i=0;i<sizeof(a)/sizeof(a[10]);i++){
            for(int j=0;j<10;j++){
                cout<<a[i][j];
            }
            cout<<" ";
        }
        cout<<"\n"<<INT_MAX;*/
    //int a;
   // for(int i=0;i<5;i++){
       // cin>>a;
    //}
    //cout<<(sizeof(a)/sizeof(a[0]));
    //increment(&a);
    //cout<<"\nNew a:"<<a;
    //cout<<"\nNew &a:"<<&a;
        /*int a[3]={-1,-2,-3};
        cout<<sizeof(a)/sizeof(a[0]);
        a[3]=dosomething(a);
        cout<<"\n"<<sizeof(a);
        cout<<"\n"<<a[0];
        cout<<"\n"<<a[1];*/
            /*char abc[5];
            cin.getline(abc,5);
            cout.write(abc,1);
            cout.write(abc,2);*/
                /*int a[5]={1,2,3,4,5};
                cout<<a;
                cout<<&a;
                cout<<&a[0];
                cout<<&a[1];
                cout<<&a+1;*/
    /*int a=3,b=4;
    swap(&a,&b);
    cout<<a<<":"<<b;*/
            /*int a[5]={1,2,3,4,5};
            dosomething(a);
            cout<<"\n"<<a[0];
            cout<<"\n"<<a[1];*/
    bitwiseor(1,2);
    return 0;
}
