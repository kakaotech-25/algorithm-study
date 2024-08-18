#include <bits/stdc++.h>
using namespace std;

string part1;
string part2;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    string s;
    cin >> s;
    int index = s.find('*');
    string part1 = s.substr(0, index);
    string part2 = s.substr(index+1);

    while(t--) {
        string cmp = "";
        cin >> cmp;

        if(part1.size() + part2.size() > cmp.size()) {
            cout << "NE\n";
        }

        // part1 의 문자열이 cmp 문자열안에 있고 첫부분이라면
        else if(cmp.find(part1) == 0) {
            // res 에 part2 의 사이즈만큼 끝부분을 잘라서 저장
            string res = cmp.substr(cmp.size()  - part2.size());
            if(res == part2) {
                cout << "DA\n";
            } else {
                cout << "NE\n";
            }
        } 
        else {
            cout << "NE\n";
        }
    }

    return 0;
}