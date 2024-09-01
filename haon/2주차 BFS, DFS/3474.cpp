#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int t; // 테스트 개수
int n;
int two;
int five;
int temp;
vector<int> v;
void sol(int num) {
	while (num > 1) {
		temp = num;
		while (num > 1) {
			if (num % 2 == 0) {
				two++;
				num /= 2;
			}
			else break;
		}
		num = temp;
		while (num > 1) {
			if (num % 5 == 0) {
				five++;
				num /= 5;
			}
			else break;
		}
		num = temp - 1;
	}
}


int main() {
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> n;
		sol(n);
		if (two >= five) v.push_back(five);
		else v.push_back(two);
		two = 0; five = 0;
		
	}

	for (int j = 0; j < t; j++) {
		cout << v[j] << endl;
	}


	return 0;
}
