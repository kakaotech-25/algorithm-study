#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> arr;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int mx = -1999999999;
    int mx_idx = 0;
    long long total = 0;

    cin >> n;

    for(int i=0; i<n; i++) {
        int data;
        cin >> data;
        arr.push_back(data);

        if(mx < arr[i]) {
            mx = arr[i];
            mx_idx = i;
        }
        total += arr[i];
    }

    bool isSuccess = true;

    // 왼쪽으로 이동
    for(int i=mx_idx; i>0; i--) {
        if(arr[i] < arr[i-1]) {
            isSuccess = false;
            break;                        
        }
    }

    // 오른쪽으로 이동
    for(int i=mx_idx; i<n-1; i++) {
        if(arr[i] < arr[i+1]) {
            isSuccess = false;
            break;                        
        }
    }

    if(!isSuccess) {
        cout << 0;
    } else {
        cout << total;
    }

    return 0;
}