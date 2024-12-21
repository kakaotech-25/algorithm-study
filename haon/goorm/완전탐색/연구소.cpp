#include <bits/stdc++.h>
using namespace std;

int n, m;
int mx;
int board[10][10];
int tmp[10][10];
vector<pair<int,int>> wall;
vector<pair<int,int>> virus;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for(int i=0; i<n; i++) {
        for(int j=0; j<m; j++) {
            cin >> board[i][j];

            if(board[i][j] == 0) {
                wall.push_back({i, j});
            }

            if(board[i][j] == 2) {
                virus.push_back({i, j});
            }
        }
    }

    vector<int> brute(wall.size(), 1);
    fill(brute.begin(), brute.begin() + wall.size() - 3, 0);

    do {
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                tmp[i][j] = board[i][j];
            }
        }

        for(int i=0; i<brute.size(); i++) {
            if(brute[i] == 1) {
                tmp[wall[i].first][wall[i].second] = 1;
            }
        }

        queue<pair<int,int>> q;
        for(int i=0; i<virus.size(); i++) {
            q.push(virus[i]);
        }

        while(!q.empty()) {
            auto cur = q.front();
            q.pop();

            int x = cur.first;
            int y = cur.second;

            tmp[x][y] = 2;

            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }

                if(tmp[nx][ny] != 0) {
                    continue;
                }
                tmp[nx][ny] = 2;
                q.push({nx, ny});
            }
        }

        int cur = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                if(tmp[i][j] == 0) {
                    cur++;
                }
            }
        }
        mx = max(cur, mx);

    } while(next_permutation(brute.begin(), brute.end()));

    cout << mx;

    return 0; 
}