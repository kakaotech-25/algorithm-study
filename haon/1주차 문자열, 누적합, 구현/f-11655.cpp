#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string arr;
    getline(cin, arr);

    for(int i=0; i<arr.length(); i++) {
        if(arr[i] >= 'a' && arr[i] <= 'z') {
            arr[i] += 13;
            // 소문자는 +13 을 해주면 char 범위를 벗어나는 경우가 있어서 오버플로우가 발생한다.
            // 따라서 소문자는 +13 을 했을때 소문자 범위가 아니라면, 다시 -26 을 해준다.
            if(arr[i] > 'z' || arr[i] < 'a') {
                arr[i] -= 26;
            }
        }
        else if(arr[i] >= 'A' && arr[i] <= 'Z') {
            arr[i] += 13;
            if(arr[i] > 'Z') {
                arr[i] -= 26;
            }
        }
        cout << arr[i];
    }

    return 0;
}