#include <bits/stdc++.h>
using namespace std;

int n, m;
int board[102][102];
int dist[102][102];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for(int i=0; i<n; i++) {
        string s;
        cin >> s;
        for(int j=0; j<s.length(); j++) {
            board[i][j] = s[j] - '0';
        }
    }

    queue<pair<int,int>> q;
    q.push({0, 0});

    while(!q.empty()) {
        auto cur = q.front();
        q.pop();

        int x = cur.first;
        int y = cur.second;

        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }

            if(dist[nx][ny] != 0 || board[nx][ny] != 1) {
                continue;
            }

            dist[nx][ny] = dist[x][y] + 1;
            q.push({nx, ny});
        }
    }

    cout << dist[n-1][m-1] + 1;

    return 0;
}