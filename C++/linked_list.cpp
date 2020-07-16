#include<iostream>
using namespace std;
struct Node{
    int info;
    Node *next;
}*start,*ptr,*save,*newptr;
Node *create_new_node(int inf){
    ptr=new Node;
    ptr->info=inf;
    ptr->next=NULL;
    return ptr;
}
void insert_beg(Node *ptr){
    if(start==NULL){
        start=ptr;
    }
    else{
        save=start;
        start=ptr;
        ptr->next=save;
    }
}
void display_list(Node *ptr){
    cout<<"\nThe list is";
    while(ptr){
        cout<<"\n"<<ptr->info;
        ptr=ptr->next;
    }
}
int main(){
    int inf;
    char ch='y';
    while(ch=='y' || ch=='Y'){
        cout<<"\nDo you want to create new node(Y/N)";
        cin>>ch;
        if(ch=='y' || ch=='Y'){
            cout<<"\nEnter the information for node";
            cin>>inf;
            newptr=create_new_node(inf);
            if(newptr!=NULL){
                    cout<<"\nNode created successfully";
                    insert_beg(newptr);
                    cout<<"\nInserted the node at beginning";
            }
            else{
                cout<<"\nUnable to create node";
            }
        }
    }
    display_list(start);
    return 0;
}
