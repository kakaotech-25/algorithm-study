#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
 
int N;
const int MAX = 101;
int input[MAX][MAX];
int map[MAX][MAX];
bool visited[MAX][MAX];
int dy[] = { 0,0,-1,1 };
int dx[] = { -1,1,0,0 };
queue<pair<int, int>> q;
vector<int> v; //영역 개수 저장 벡터
int cnt; //영역 개수
 
void BFS(int y, int x) {
    visited[y][x] = true;
    q.push(make_pair(y, x));
 
    while (!q.empty()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();
 
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
 
            if (ny < 0 || nx < 0 || ny >= N || nx >= N)
                continue;
            if (map[ny][nx] && !visited[ny][nx]) {
                visited[ny][nx] = true;
                q.push(make_pair(ny, nx));
            }
        }
    }
}
 
void reset() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            map[i][j] = 0;
            visited[i][j] = 0;
        }
    }
    cnt = 0;
}
 
int main() {
    int maxHeight = -1;
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> input[i][j];
            if (input[i][j] > maxHeight) {
                maxHeight = input[i][j];
            }
        }
    }
 
    for (int h = 1; h <= maxHeight; h++) {
        /*h미만 물에 잠김*/
 
        /*h미만=0 h이상=1 */
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (input[i][j] < h) {
                    map[i][j] = 0;
                }
                else {
                    map[i][j] = 1;
                }
            }
        }
 
        /*BFS 영역 개수 구하기*/
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] && !visited[i][j]) {
                    BFS(i, j);
                    cnt++;
                }
            }
        }
        v.push_back(cnt);
        
        /*초기화*/
        reset();
    }
 
    sort(v.begin(), v.end()); //오름차순 정렬
    cout << v[v.size() - 1];  //최댓값 출력
}
