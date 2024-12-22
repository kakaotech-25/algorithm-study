#include <bits/stdc++.h>
using namespace std;

int board[66][66];

void func(int n, int startX, int startY) {
  if(n == 1) {
    cout << board[startX][startY];
    return;
  }

  bool isSameArea = true;
  int color = board[startX][startY];
  for(int i=startX; i<startX+n; i++) {
    for(int j=startY; j<startY+n; j++) {
      if(color != board[i][j]) {
        isSameArea = false;
        break;
      }      
    }
  }

  if(isSameArea) {
    cout << board[startX][startY];
  } else {
    int size = n/2;
    cout << "(";
    for(int i=0; i<2; i++) {
      for(int j=0; j<2; j++) {
        int newX = startX + size * i;
        int newY = startY + size * j;
        func(size, newX, newY);
      }
    }
    cout << ")";
  }
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int n;
  cin >> n;

  for(int i=0; i<n; i++) {
    string s;
    cin >> s;
    for(int j=0; j<n; j++) {
      if(s[j] == '0') {
        board[i][j] = 0;
      } else {
        board[i][j] = 1;
      }
    }
  }

  func(n, 0, 0);

  return 0;
}