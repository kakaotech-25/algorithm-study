
#include <bits/stdc++.h>
using namespace std;

int n, m;
int board[102][102];
int dist[102][102];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

void bfs(int x, int y) {
    queue<pair<int,int>> q;
    q.push({x, y});
    dist[x][y] = 0;

    while(!q.empty()) {
        auto cur = q.front();
        q.pop();

        for(int i=0; i<4; i++) {
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }

            if(dist[nx][ny] != -1 || board[nx][ny] == 0) {
                continue;
            }

            dist[nx][ny] = dist[cur.first][cur.second] + 1;
            q.push({nx, ny});
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for(int i=0; i<n; i++) {
        string s;
        cin >> s;
        for(int j=0; j<m; j++) {
            board[i][j] = s[j] - '0';
        }
    }

    for(int i=0; i<n; i++) {
        fill(dist[i], dist[i] + m + 1, -1);
    }

    bfs(0, 0);
    cout << dist[n-1][m-1] + 1;

    return 0;
}
