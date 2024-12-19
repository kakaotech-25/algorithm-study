#include <bits/stdc++.h>
using namespace std;

int n, k;
char board[202][202];
int score[202][202];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

void bomb(int x, int y) {
    if(board[x][y] == '0') {
        score[x][y]++;
    }

    if(board[x][y] == '@') {
        score[x][y] += 2;
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> k;

    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            cin >> board[i][j];
        }
    }

    while(k--) {
        int x, y;
        cin >> x >> y;
        bomb(x, y);

        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            bomb(nx, ny);
        }        
    }

    int mx = -199999999;

    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            mx = max(mx, score[i][j]);
        }
    }
    cout << mx;

    return 0;
}