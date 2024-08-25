#include <bits/stdc++.h>
using namespace std;

int m, n, k;
int board[102][102];
bool visited[102][102];
vector<int> areas;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

void bfs(int x, int y) {
    queue<pair<int,int>> q;
    q.push({x, y});

    int area = 0;
    while(!q.empty()) {
        int curX = q.front().first;
        int curY = q.front().second;

        visited[curX][curY] = true;
        area++;
        q.pop();

        for(int i=0; i<4; i++) {
            int nx = curX + dx[i];
            int ny = curY + dy[i];

            if(nx < 1 || nx > n || ny < 1 || ny > m) {
                continue;
            }

            if(visited[nx][ny] || board[nx][ny] == 1) {
                continue;
            }
            q.push({nx, ny});
            visited[nx][ny] = true;
        }
    }
    areas.push_back(area);
}

void draw() {
    int x1, y1, x2, y2;

    while(k--) {
        cin >> x1 >> y1 >> x2 >> y2;
        for(int i=x1+1; i<=x2; i++) {
            for(int j=y1+1; j<=y2; j++) {
                board[i][j] = 1; // board[i][j] = 1   ==> 벽돌이 있는 경우 
            }
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> m >> n >> k;

    draw();

    int count = 0;
    for(int i=1; i<=n; i++) {
        for(int j=1; j<=n; j++) {
            if(!visited[i][j] && board[i][j] == 0) {
                bfs(i, j);
                count++;
            }
        }
    }
    cout << count << "\n";
    sort(areas.begin(), areas.end());

    for(int i=0; i<areas.size(); i++) {
        cout << areas[i] << ' ';
    }

    return 0;
}