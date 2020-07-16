#include<iostream>
#include<conio.h>
using namespace std;
int main(){
    int a[20],top=-1;
    char ch='y';
    while(ch=='y' || ch=='Y'){
        int choice;
        cout<<"Enter your choice\n1.Insert Element\n2.Delete Element\n3.Display all elements\n4.Exit\n\tEnter Your Choice";
        cin>>choice;
        system("cls");
        switch(choice){
        case 1:
            int dat;
            cin>>dat;
            if(top>=19){
                cout<<"\nMemory insufficient"<<endl;
            }else{
                top+=1;
                cout<<top<<endl;
                a[top]=dat;
                cout<<dat<<" inserted"<<endl;
            }
            break;
        case 2:
            if(top==-1){
                cout<<"\nStack Empty!"<<endl;
            }else{
                cout<<a[top]<<" deleted!"<<endl;
                a[top]=0;
                top--;
            }
            break;
        case 3:
            if(top==-1){
                cout<<"\nStack Empty!"<<endl;
            }else{
                int pos=top;
                while(pos>=0){
                    cout<<a[pos]<<endl;
                    pos--;
                }
            }
            break;
        case 4:
            exit(0);
        default:
            cout<<"Wrong Choice entered"<<endl;
            break;
        }
        cout<<"Want to continue(Y/N): ";
        cin>>ch;
        system("cls");
    }
    return 0;
}
