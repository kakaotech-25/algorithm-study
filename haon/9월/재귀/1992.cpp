#include <bits/stdc++.h>
using namespace std;

int n;
int board[64][64];

void func(int k, int startX, int startY) {
    if(k == 1) {
        cout << board[startX][startY];
        return;
    }

    bool isSameArea = true;
    int color = board[startX][startY];

    for(int i=startX; i<startX+k; i++) {
        for(int j=startY; j<startY+k; j++) {
            if(color != board[i][j]) {
                isSameArea = false;
                break;
            }
        }
    }

    if(isSameArea) {
        cout << board[startX][startY];
    } else {
        cout << "(";
        int size = k/2;
        for(int i=0; i<2; i++) {
            for(int j=0; j<2; j++) {
                func(size, startX + size*i, startY + size*j);
            }
        }
        cout << ")";
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for(int i=0; i<n; i++) {
        string s;
        cin >> s;
        for(int j=0; j<n; j++) {
            board[i][j] = s[j] - '0';
        }
    }

    func(n, 0, 0);

    return 0;
}