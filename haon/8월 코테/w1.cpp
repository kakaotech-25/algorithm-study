#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> arr;
int n;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    // 쿠키의 맛있는 정도와 원래 인덱스를 저장
    for (int i = 1; i <= n; i++) {
        int data;
        cin >> data;
        arr.push_back({data, i});
    }

    // 맛있는 정도를 기준으로 오름차순 정렬
    sort(arr.begin(), arr.end());

    // 사전순으로 제일 앞서는 순서로 출력 (정렬된 순서대로 인덱스를 출력)
    for (int i = 0; i < n; i++) {
        cout << arr[i].second << ' ';
    }

    return 0;
}
