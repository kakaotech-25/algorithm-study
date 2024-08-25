#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#define INF 987654321
using namespace std;

typedef long long ll;

bool compare(pair<int,pair<int,int>> a, pair<int,pair<int,int>> b) {
	if (a.second.second == b.second.second)
		return a.first < b.first;
	else
		return a.second.second > b.second.second;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int N, C;
	cin >> N >> C;

	vector<pair<int,pair<int, int>>> v;
	map<int, int> m;
	queue<pair<int,int>> q;

	int ps = 1;
	for (int i = 0; i < N; i++) {
		int x; cin >> x;
		if (x <= C) {
			if (m.find(x) == m.end()) {
				m.insert({ x, 1 });
				q.push({ ps, x });
				ps++;
			}
			else {
				m[x]++;
			}
		}
	}

	while (!q.empty()) {
		int fast = q.front().first;
		int data = q.front().second;
		q.pop();

		v.push_back({ fast, {data,m[data] } });
	}

	sort(v.begin(), v.end(), compare);

	for (int i = 0; i < v.size(); i++) {
		int A = v[i].first;
		int B = v[i].second.first;
		int C = v[i].second.second;
		for (int j = 0; j < C; j++) {
			cout << B << " ";
		}
	}
	return 0;
}