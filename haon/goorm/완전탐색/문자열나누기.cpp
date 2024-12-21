#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    string s;
    cin >> s;

    unordered_set<string> tmp;
    vector<vector<string>> sub_list;

    for(int st = 1; st < n-1; ++st) {
        for(int en = st + 1; en < n; ++en) {
            string front = s.substr(0, st);
            string mid = s.substr(st, en - st);
            string end = s.substr(en, n - en);

            vector<string> sub;
            sub.push_back(front);
            sub.push_back(mid);
            sub.push_back(end);
            sub_list.push_back(sub);

            tmp.insert(front);
            tmp.insert(mid);
            tmp.insert(end);
        }
    }

    vector<string> dic(tmp.begin(), tmp.end());
    sort(dic.begin(), dic.end());

    int mx = 0;
    for(auto sub : sub_list) {
        int score = 0;
        for(string s : sub) {
            score += find(dic.begin(), dic.end(), s) - dic.begin() + 1;
        }
        mx = max(score, mx);
    }
    cout << mx;

    return 0;
}
