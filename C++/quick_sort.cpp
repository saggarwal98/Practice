#include<iostream>
using namespace std;
void swap_numbers(int *a, int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
int partition_array(int a[],int low,int high){
    int pivot=a[high];
    int i=low-1;
    for(int j=i+1;j<=high;j++){
        if(a[j]<pivot){
            i++;
            swap_numbers(&a[i],&a[j]);
        }
    }
    swap_numbers(&a[i+1],&a[high]);
    return i+1;
}
void quick_sort(int a[],int low,int high){
    if(low<high){
        int pi=partition_array(a,low,high);
        quick_sort(a,low,pi-1);
        quick_sort(a,pi+1,high);
    }
}
int main(){
    int n;
    cout<<"Enter array size"<<endl;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    quick_sort(a,0,n-1);
    for(int i=0;i<n;i++){
        cout<<a[i];
    }
    return 0;
}
