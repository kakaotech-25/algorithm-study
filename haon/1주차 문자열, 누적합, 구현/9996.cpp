#include <bits/stdc++.h>
using namespace std; 


int main(void) 
{
	int n; 
    cin >> n; 
	string s; 
    cin >> s; 

    int index = s.find('*');
    string part1 = s.substr(0, index);
    string part2 = s.substr(index+1);
    
	while (n--) { //n번 동안
		string cmp = ""; 
		cin >> cmp; //string 하나 생성

		if (part1.size() + part2.size() > cmp.size()) { 
            cout << "NE\n"; //part1,2 의 사이즈를 합했을때보다 cmp문자열 보다 더 작으면 NE 출력
        }

        else if(cmp.find(part1) == 0) {
            string ex = cmp.substr(cmp.size() - part2.size());
            if(ex == part2) {  //자른 문자열이 part2와 동일하냐? 그렇다면 DA출력
                cout << "DA\n";
            } else {
                cout << "NE\n";
            }
        }

		else { 
            cout << "NE\n";// part1과 cmp문자열이 일치하지 않으면 NE 바로 출력
        }
	}
}
