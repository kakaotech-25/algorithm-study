#include <bits/stdc++.h>
using namespace std;

int l, c;
char arr[17];
char res[17];

bool isAeiou(char c) {
    if(c == 'a' || c =='e' || c == 'i' || c == 'o' || c == 'u') {
        return true;
    }
    return false;
}

void func(int k, int st) {
    if(k == l) {
        int num1 = 0;
        int num2 = 0;
        for(int i=0; i<l; i++) {
        if(isAeiou(res[i])) {
            num1++;
        } else{
            num2++;
        }
        }

        if(num1 >= 1 && num2 >= 2) {
            for(int i=0; i<l; i++) {
                cout << res[i];
            }
            cout << "\n";
        }
        return;
  }

    for(int i=st; i<c; i++) {
        res[k] = arr[i];
        func(k+1, i+1);
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> l >> c;

    for(int i=0; i<c; i++) {
        cin >> arr[i];        
    }
    sort(arr, arr + c);

    func(0, 0);

    return 0;
}