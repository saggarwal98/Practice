#include<iostream>
using namespace std;
struct Node{
    int info;
    Node *next;
}*ptr,*newptr,*rear,*start;
Node *create_new_node(int inf){
    ptr=new Node;
    ptr->info=inf;
    ptr->next=NULL;
    return ptr;
}
void insert_end(Node *ptr){
    if(start==NULL){
        start=ptr;
        rear=ptr;
    }
    else{
        rear->next=ptr;
        rear=ptr;
    }
}
void delete_start(){
    if(start!=NULL){
        ptr=start;
        start=start->next;
        delete ptr;
    }
    else{
        cout<<"Queue Empty!"<<endl;
    }
}
void traverse(){
    if(start!=NULL){
        ptr=start;
        while(ptr){
            cout<<ptr->info<<endl;
            ptr=ptr->next;
        }
    }
    else{
        cout<<"Queue Empty!"<<endl;
    }
}
int main(){
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
            newptr=create_new_node(dat);
            if(newptr!=NULL){
                insert_end(newptr);
            }
            else{
                cout<<"Insufficient Memory!"<<endl;
            }
            break;
        case 2:
            delete_start();
            break;
        case 3:
            traverse();
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
