#include <bits/stdc++.h>
using namespace std;

int n, m;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m; // 시험 개수, 과목 개수

    unordered_map<int, int> scores;
    unordered_map<int, int> counts;

    for(int i=0; i<n; i++) {
        int num, score;
        cin >> num >> score;

        scores[num] += score;
        counts[num]++;
    }

    double maxAverage = -1;
    int maxKey = -1;

    for(unordered_map<int,int>::iterator it = scores.begin(); it != scores.end(); it++) {
        int key = it -> first; // 현재 과목 번호
        int totalScore = it -> second; // 현재 과목의 총 점수 

        double average = (double) totalScore / counts[key]; // 과목별 평균 계산 

        if(average > maxAverage || (average == maxAverage && key < maxKey)) {
            maxAverage = average;
            maxKey = key;
        }
    }

    cout << maxKey;

    return 0;
}