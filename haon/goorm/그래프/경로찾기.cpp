#include <bits/stdc++.h>
using namespace std;

int n;
int board[102][102];
bool visited[102];

bool dfs(int start, int end) {
    fill(visited, visited + n+2, false);

    stack<int> s;
    s.push(start);

    while(!s.empty()) {
        int cur = s.top();
        s.pop();

        if(visited[cur]) {
            continue;
        }

        if(cur != start) {
            visited[cur] = true;
        }

        for(int next=0; next<n; next++) {
            if(visited[next]) {
                continue;
            }

            if(board[cur][next] == 1) {
                if(next == end) {
                    return true;
                }
            }

            s.push(next);
        }
    }
    return false;
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

    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cout << dfs(i, j) << " ";
        }
        cout << "\n";
    }

    return 0;
}