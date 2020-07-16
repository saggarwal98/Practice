#include<iostream>
#include<iterator>
#include<vector>
using namespace std;
int checkCondition(int a,int b,int B){
    //int len1=0,len2=0,len3=0;
    cout<<a<<":"<<b<<endl;
    if(a==b){
        return 0;
    }
    else if(a>=B){
        return 1;
    }
    else if((b-a)>=B){
        return 1;
    }
    else if((100-b)>=B){
        return 1;
    }
    else{
        return 0;
    }
}
void Solution(vector<int> &A, int B) {
    vector<int>::iterator start=A.begin();
    vector<int>::iterator last=A.end();
    int N=A.size();
    vector<int>::iterator i;
    vector<int>::iterator j;
    int totalPro=(N*(N-1))/2;
    int favPro=0;
    for(i=A.begin();i!=prev(A.end(),1);){
        for(j=next(i,1);j!=A.end();){
            favPro+=checkCondition(*i,*j,B);
            cout<<favPro<<endl;
            j=next(j,1);
        }
        i=next(i,1);
    }
    cout<<(favPro*10000000)/totalPro;
}
int main(){
    vector<int> A={30,60,90};
    int B=50;
    Solution(A,B);
}
