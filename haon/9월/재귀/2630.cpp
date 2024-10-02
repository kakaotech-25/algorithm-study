#include <bits/stdc++.h>
using namespace std;

int n;
int res[3];
int board[130][130];

void func(int k, int startX, int startY) {
    if(k == 1) {
        res[board[startX][startY]]++;
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
        res[color]++;
    } else {
        int size = k/2;
        for(int i=0; i<2; i++) {
            for(int j=0; j<2; j++) {
                func(size, startX+size*i, startY+size*j);
            }
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> board[i][j];
        }
    }

    func(n, 0, 0);    

    cout << res[0] << "\n";
    cout << res[1];

    return 0;
}