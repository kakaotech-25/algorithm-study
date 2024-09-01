#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(void) {
	int k;
	cin >> k;
	
	while (k > 0) {
		k--;
		string input;
		cin >> input;

		stack<char> st;
		string answer = "YES";
		for (int i = 0; i < input.length(); i++) {
			//'('는 스택에 저장
			if (input[i] == '(') {
				st.push(input[i]);
			}
			//')'가 나오면 스택에 저장된 '('와 짝이 맞는지 확인하고 pop
			else if (!st.empty() && input[i] == ')' && st.top() == '(') {
				st.pop();
			}
			//위의 경우를 제외하고는 모두 vps가 아닌 상황이므로 종료(break)
			else {
				answer = "NO";
				break;
			}
		}
		//'('와 ')'가 짝이 안 맞는 경우 '('가 모두 pop되지 않기 때문에
		// 스택이 비지 않는다. 따라서 이 경우는 vps가 아니므로 "NO"
		if (!st.empty()) answer = "NO";

		cout << answer << endl;
	}
	return 0;
}