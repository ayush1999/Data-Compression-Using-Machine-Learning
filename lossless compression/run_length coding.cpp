#include<iostream>
#include<string>
using namespace std;

// Run-length endcoding algorithm.
// Used for lossless data compression.
// Eg. Input: AABBBCCCCDEE.
//     Output: A2B3C4D1E2

string run_length(string s){
    string result="";
    int i;
    for(i=0;i<s.length();i++){
        int count=1;
        while(s[i]==s[i+1]){
            count++;
            i++;
        }
        result = result.push_back(s[i])
        result = result.push_back(static_cast<char>i); 
    }
    return result;
}

int main(){
    cout<<run_length("AABBBCCCCDEE");
    return 0;
}