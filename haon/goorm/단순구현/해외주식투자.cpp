#include <bits/stdc++.h>
using namespace std;

int n;

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  vector<pair<double, int>> evaluations;

  cin >> n;
  // 평가 금액 = 주식 개수 X 가격
  for (int i = 0; i < n; i++) {
    double price;
    int cnt;

    cin >> price >> cnt;

    double evaluate = price * cnt;

    // 소수점 2째자리까지만 남기고 나머지 버림
    evaluate = floor(evaluate * 10) / 10;
    evaluations.push_back({evaluate, i+1});
  }

  sort(evaluations.begin(), evaluations.end(), [](const pair<double, int>& a, const pair<double, int>& b) {
    if(a.first == b.first) {
      return a.second < b.second;
    }
    return a.first > b.first;
  });

  for(int i=0; i<evaluations.size(); i++) {
    cout << evaluations[i].second << ' ';
  }

  return 0;
}
