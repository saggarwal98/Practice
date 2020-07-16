#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int priority(char c){
    if(c=='+' || c=='-')return 1;
    if(c=='*' || c=='/')return 2;
    if(c=='^')return 3;
    return 0;
}
string postfix(string s){
    for(int i=0;i<s.size();i++){
        if(s[i]=='('){
            s[i]==')';
        }
        if(s[i]==')'){
            s[i]=='(';
        }
    }
    //reverse(s.begin(),s.end());
    s='('+s+')';
    stack<char> newstack;
    string output;
    for(int i=0;i<s.size();i++){
        if(isalpha(s[i]) || isdigit(s[i])){
            output+=s[i];
        }
        else if(s[i]=='('){
                    newstack.push(s[i]);
        }
        else if(s[i]==')'){
            while(newstack.top()!='('){
                    output+=newstack.top();
                    newstack.pop();
                  }
            newstack.pop();
        }
        else{
                //cout<<s[i]<<endl;
            if(!isalpha(newstack.top()) && !isdigit(newstack.top())){
                //cout<<"in else case if"<<endl;
                while(priority(newstack.top())>=    priority(s[i])){
                    output+=newstack.top();
                    newstack.pop();
                }
                newstack.push(s[i]);
            }
        }
    }
    return output;
}
string infix(string s){
    stack<string> newstack1;
    for(int i=0;i<s.size();i++){
        if(isalpha(s[i]) || isdigit(s[i])){
            string s1(1,s[i]);
            newstack1.push(s1);
        }
        else{
            string s1,s2,temp;
            s1=newstack1.top();
            newstack1.pop();
            s2=newstack1.top();
            newstack1.pop();
            temp=s2+s[i]+s1;
            newstack1.push(temp);
        }
    }
    return newstack1.top();
}
int main(){
    string s;
    cout<<"enter a string: ";
    cin>>s;
    s=postfix(s);
    cout<<"\nPostfix: "<<s<<endl;
    string inf=infix(s);
    //reverse(inf.begin(),inf.end());
    cout<<"Infix: "<<inf<<endl;
    reverse(s.begin(),s.end());
    cout<<"Prefix: "<<s;
}
