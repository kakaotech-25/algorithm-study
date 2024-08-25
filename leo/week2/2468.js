/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n;
let heights = [];

rl.on("line", function (line) {
  if (!n) {
    n = parseInt(line);
  } else {
    heights.push(line.split(" ").map(Number));
    if (heights.length === n) {
      rl.close();
    }
  }
}).on("close", function () {
  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];

  function isSafe(x, y, rainLevel, visited) {
    return (
      x >= 0 &&
      y >= 0 &&
      x < n &&
      y < n &&
      !visited[x][y] &&
      heights[x][y] > rainLevel
    );
  }

  function dfs(x, y, rainLevel, visited) {
    let stack = [[x, y]];
    visited[x][y] = true;

    while (stack.length > 0) {
      let [cx, cy] = stack.pop();

      for (let [dx, dy] of directions) {
        let nx = cx + dx;
        let ny = cy + dy;

        if (isSafe(nx, ny, rainLevel, visited)) {
          visited[nx][ny] = true;
          stack.push([nx, ny]);
        }
      }
    }
  }

  let maxSafeAreas = 0;

  for (let rainLevel = 0; rainLevel <= 100; rainLevel++) {
    let visited = Array.from({ length: n }, () => Array(n).fill(false));
    let safeAreas = 0;

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (heights[i][j] > rainLevel && !visited[i][j]) {
          dfs(i, j, rainLevel, visited);
          safeAreas++;
        }
      }
    }

    maxSafeAreas = Math.max(maxSafeAreas, safeAreas);
  }

  console.log(maxSafeAreas);
  process.exit();
});
