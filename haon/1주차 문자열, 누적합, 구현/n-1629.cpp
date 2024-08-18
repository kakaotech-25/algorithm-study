#include <bits/stdc++.h>
using namespace std;

long long a, b, c, k;
long long ans;

long long power(long long b) {
    if(b == 0) {
        return 1;
    }
    if(b == 1) {
        return a % c;
    }
    k = power(b/2) % c;
    if(b % 2 == 0) {
        return k*k % c;
    }
	return k * k % c * a % c;
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> a >> b >> c;
    cout << power(b);
}