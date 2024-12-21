#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> adj_list[502];
int dist[502];

void bfs(int st) {
    queue<int> q;
    q.push(st);

    dist[st] = 0;

    while(!q.empty()) {
        int cur = q.front();
        q.pop();

        for(int next : adj_list[cur]) {
            if(dist[next] != -1) {
                continue;
            }
            dist[next] = dist[cur] + 1;
            q.push(next);
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

    fill(dist, dist + n+1, -1);

    bfs(1);

    int ans = 0;
    for(int i=2; i<=n; i++) {
        if(dist[i] <= 2 && dist[i] != -1) {
            ans++;
        }
    }
    cout << ans;

    return 0;
}