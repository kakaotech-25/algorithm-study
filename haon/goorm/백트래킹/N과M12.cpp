#include <bits/stdc++.h>
using namespace std;

int n, m;
int num[10];
int arr[10];
// 1 7 9 

void func(int k, int st) {
    if(k == m) {
        for(int i=0; i<m; i++) {
            cout << arr[i] << ' ';
        }
        cout << "\n";
        return;
    }

    for(int i=st; i<n; i++) {
        arr[k] = num[i];
        func(k+1, i);
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    set<int> s;
    for(int i=0; i<n; i++) {
        int data;
        cin >> data;
        s.insert(data);
    }    

    n = 0;
    for(int x : s) {
        num[n++] = x;
    }
    sort(num, num + n);

    func(0, 0);

    return 0;
}