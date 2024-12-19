#include <bits/stdc++.h>
using namespace std;

int n;
int goorm_x, goorm_y;
int player_x, player_y;
string board[202][202];
bool visited[202][202];

pair<int,int> move(char commend) {
    if(commend == 'L') {
        return make_pair(0, -1);
    }

    else if(commend == 'R') {
        return make_pair(0, 1);
    }

    else if(commend == 'U') {
        return make_pair(-1, 0);
    }

    return make_pair(0, 1);
}

int play(int x, int y) {
    bool isEnd = false;
    visited[x][y] = true;

    while(!isEnd) {
        int count = board[x][y][0] - '0';
        char commend = board[x][y][1];
        pair<int,int> move_dir = move(commend);

        while(count--) {
            x = (x + move_dir.first + n) % n;
            y = (y + move_dir.second + n) % n;

            if(visited[x][y]) {
                isEnd = true;
                break;
            }
            visited[x][y] = true;
        }
    }

    int ans = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(visited[i][j]) {
                ans++;
            }
        }
    }
    return ans;
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    cin >> goorm_x >> goorm_y;
    cin >> player_x >> player_y;

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            string s;
            cin >> s;
            board[i][j] = s;            
        }
    }

    int res1 = play(goorm_x, goorm_y);

    for(int i=0; i<n; i++) {
        fill(visited[i], visited[i] + n+1, false);
    }

    int res2 = play(player_x, player_y);

    if(res1 > res2) {
        cout << "goorm " << res1;
    } else {
        cout << "player " << res2;
    }

    return 0;
}
