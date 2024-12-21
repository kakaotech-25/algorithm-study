#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> adj_list[1002];
bool visited[1002];

void bfs(int st) {
    queue<int> q;
    q.push(st);

    while(!q.empty()) {
        int cur = q.front();
        q.pop();

        for(int next : adj_list[cur]) {
            if(!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for(int i=0; i<m; i++) {
        int u, v;
        cin >> u >> v;
        adj_list[u].push_back(v);
        adj_list[v].push_back(u);        
    }

    int cnt = 0;
    for(int i=1; i<=n; i++) {
        if(!visited[i]) {
            bfs(i);
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}