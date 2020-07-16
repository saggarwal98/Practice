#include<iostream>
#include<string>
#include<cstring>
//#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;


int main(){
    char a[10];
    cin.getline(a,10);
    int l=strlen(a);
    unordered_map<int, int> m;
    for(int i=0;i<l;i++){
        m[a[i]]++;
    }
    for(auto x:m){
        cout<<char(x.first)<<":"<<x.second<<endl;
    }
    return 0;
}
