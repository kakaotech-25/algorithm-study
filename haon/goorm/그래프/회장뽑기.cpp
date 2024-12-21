#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> adj_list[52];
int dist[52];
int scores[52];

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    while(true) {
        int u, v;
        cin >> u >> v;
        if(u == -1 && v == -1) {
            break;
        }
        adj_list[u].push_back(v);
        adj_list[v].push_back(u);
    }

    for(int i=1; i<=n; i++) {
        fill(dist, dist + n + 1, -1);        

        queue<int> q;
        q.push(i);
        dist[i] = 0;
    
        while(!q.empty()) {
            int cur = q.front();
            q.pop();

            for(auto next : adj_list[cur]) {
                if(dist[next] != -1) {
                    continue;
                }
                dist[next] = dist[cur] + 1;
                q.push(next);
            }
        }

        int score = *max_element(dist + 1, dist + n+1);
        scores[i] = score;
    }

    int minValue = *min_element(scores + 1, scores + n+1);
    vector<int> person;
    for(int i=1; i<=n; i++) {
        if(scores[i] == minValue) {
            person.push_back(i);
        }
    }

    cout << minValue << ' ' << person.size() << "\n";
    for(int i=0; i<person.size(); i++) {
        cout << person[i] << ' ' ;
    }

    return 0;
}