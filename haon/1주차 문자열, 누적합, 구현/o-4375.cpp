#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    int k = 0;

    while(cin >> n) {
        int ans = 1;
        k = 1;

        while(1) {
            if(ans % n == 0)  {
                break;
            }
            else {
                k++;
                ans = ans * 10 + 1;
                ans %= n;
            }
        }
        cout << k << "\n";
    }

    return 0;
}