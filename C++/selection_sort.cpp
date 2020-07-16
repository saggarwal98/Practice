#include<iostream>
using namespace std;
void selection_sort(int *a,int n){
    for(int i=0;i<n;i++){
        int minimum=0;
        for(int j=i+1;j<n;j++){
            if(a[j]<a[i]){
                minimum=j;
            }
        }
        if(minimum!=0){
            int temp=a[minimum];
            a[minimum]=a[i];
            a[i]=temp;
        }
    }
    //for(int i=0;i<n;i++){
    //    cout<<a[i];
    //}
    //return *a;
}
int main(){
    int n;
    cout<<"Enter array size"<<endl;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    selection_sort(a,n);
    /*for(int i=0;i<n;i++){
        cout<<a[i];
    }*/
    for(int i=0;i<n;i++){
        cout<<a[i];
    }
    return 0;
}
