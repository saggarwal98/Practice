#include<iostream>
using namespace std;
struct Node{
    int info;
    Node *prev;
}*ptr,*newptr,*top;
Node *create_new_node(int inf){
    ptr=new Node;
    ptr->info=inf;
    ptr->prev=NULL;
    return ptr;
}
void insert_end(Node *ptr){
    if(top==NULL){
        top=ptr;
    }
    else{
        ptr->prev=top;
        top=ptr;
    }
}
void delete_end(){
    if(top!=NULL){
        ptr=top;
        top=top->prev;
        delete ptr;
    }
    else{
        cout<<"Stack Empty!"<<endl;
    }
}
void traverse(){
    if(top!=NULL){
        ptr=top;
        while(ptr){
            cout<<ptr->info<<endl;
            ptr=ptr->prev;
        }
    }
    else{
        cout<<"Stack Empty!"<<endl;
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
            delete_end();
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
