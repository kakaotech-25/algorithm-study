#include <bits/stdc++.h>
using namespace std;

int m, n, h;
int board[102][102][102];
bool visited[102][102][102];
int dx[6] = {0, 1, 0, -1, 0, 0};
int dy[6] = {-1, 0, 1, 0, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};

void bfs() {

}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> m >> n >> h;

    queue<tuple<int,int,int>> q;

    for(int i=0; i<h; i++) {
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                
            }
        }
    }

    return 0;
}