#include <bits/stdc++.h>
using namespace std;

bool comp(const string& str1, const string& str2){
    if(str1.size() == str2.size()) return str1 < str2;
    else return str1.size() < str2.size();
}

int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    vector<string> v;
    string str, num;

    cin >> t;
    cin.ignore();
    while(t--) {
        cin >> str;
        for(const auto& token : str) {
            if(isdigit(token)) {
                num += token;
            }
            else if(!num.empty()){
                while (num.length() >= 2 && num[0] == '0') {
                    num.erase(0, 1);
                }
                v.push_back(num);
                num = "";
            }
        }
        if(!num.empty()) {
            while (num.length() >= 2 && num[0] == '0') {
                num.erase(0, 1);
            }
            v.push_back(num);
            num = "";
        }
    }
    sort(v.begin(), v.end(), comp);
    for(const auto& x : v) cout << x << '\n';
}