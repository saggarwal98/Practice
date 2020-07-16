#include<iostream>
using namespace std;
int main(){
    /*for(int i=0;i<10;i++){
        cout<<i++<<endl;
        cout<<i<<endl;
    }*/
    char ch='Z';
    switch(ch){
    case 'Z':
    case 'z':
        cout<<int(ch);
        break;
    default:
        cout<<"Wrong token";
    }
}
