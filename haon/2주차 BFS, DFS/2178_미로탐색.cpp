#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int board[52][52];
bool visited[52][52];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

void bfs(int x, int y) {
    queue<pair<int,int>> q;
    q.push({x, y});
    visited[x][y] = true;

    while(!q.empty()) {
        auto cur = q.front();
        int x = cur.first;
        int y = cur.second;
        q.pop();

        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            if(visited[nx][ny] || board[nx][ny] != -1) {
                continue;
            }
            visited[nx][ny] = true;
            q.push({nx, ny});
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;
    while(t--) {
        cin >> m >> n >> k;

        while(k--) {
            int x, y;
            cin >> x >> y;
            board[y][x] = 1;
        }

        int cnt = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(board[i][j] == 1 || !visited[i][j]) {
                    bfs(i, j);
                    cnt++;
                }
            }
        }
        cout << cnt << "\n";

        for(int i=0; i<n; i++) {
            fill(board[i], board[i] + m, 0);
            fill(visited[i], visited[i] + m, false);
        }
    }

    return 0;
}