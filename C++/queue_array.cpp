#include<iostream>
#include<conio.h>
using namespace std;
int main(){
    int a[20],front=-1,rear=-1;
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
            if(rear>=19){
                cout<<"\nMemory insufficient"<<endl;
            }else{
                rear+=1;
                cout<<rear<<endl;
                a[rear]=dat;
                cout<<dat<<" inserted"<<endl;
                if(front==-1){front=0;}
            }
            break;
        case 2:
            if(front==-1){
                cout<<"\nQueue Empty!"<<endl;
            }else{
                cout<<a[front]<<" deleted!"<<endl;
                for(int i=0;i<rear;i++){
                    a[i]=a[i+1];
                }
                a[rear]=0;
                rear--;
                if(rear==-1){front=-1;}
            }
            break;
        case 3:
            if(front==-1){
                cout<<"\nQueue Empty!"<<endl;
            }else{
                int pos=front;
                while(pos>=rear){
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
