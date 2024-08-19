#include <bits/stdc++.h>
using namespace std;

int a, b, c;
int arr[105];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> a >> b >> c;

    for(int i=0; i<3; i++) {
        int st, en;
        cin >> st >> en;

        for(int j=st; j<en; j++) {
            arr[j]++;
        }
    }

    int sum = 0;
    for(int i=0; i<105; i++) {
        if(arr[i] == 1) {
            sum += arr[i] * a;
        } 
        else if(arr[i] == 2) {
            sum += arr[i] * b;
        }
        else if(arr[i] == 3) {
            sum += arr[i] * c;
        }
    }
    cout << sum;

    return 0;
}