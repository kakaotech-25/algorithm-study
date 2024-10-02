#include <bits/stdc++.h>
using namespace std;

int n;
int zero, one, minusone;
int board[2200][2200];

void func(int size, int startX, int startY) {
    if(size == 1) {
        if(board[startX][startY] == 1) {
            one++;
        }
        else if(board[startX][startY] == -1) {
            minusone++;
        } 
        else if(board[startX][startY] == 0) {
            zero++;
        }
        return;
    }

    bool isSameArea = true;
    int color = board[startX][startY];
    for(int i=startX; i<startX+size; i++) {
        for(int j=startY; j<startY+size; j++) {
            if(color != board[i][j]) {
                isSameArea = false;
                break;
            }
        }
    }

    if(isSameArea) {
        if(color == 0) {
            zero++;
        }
        else if(color == 1) {
            one++;
        }
        else {
            minusone++;
        }
    } else {
        int newSize = size/3;        

        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                func(newSize, startX + newSize*i, startY + newSize*j);
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

    cout << minusone << "\n";
    cout << zero << "\n";
    cout << one << "\n";

    return 0;
}