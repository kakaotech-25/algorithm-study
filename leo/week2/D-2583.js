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

let M, N, K;
let grid = [];

rl.on("line", function (line) {
  if (!M) {
    [M, N, K] = line.split(" ").map(Number);
    grid = Array.from({ length: M }, () => Array(N).fill(0));
  } else {
    const [x1, y1, x2, y2] = line.split(" ").map(Number);
    for (let i = y1; i < y2; i++) {
      for (let j = x1; j < x2; j++) {
        grid[i][j] = 1;
      }
    }
    K--;
    if (K === 0) rl.close();
  }
}).on("close", function () {
  const directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ];

  function isValid(x, y) {
    return x >= 0 && y >= 0 && x < M && y < N;
  }

  function bfs(startX, startY) {
    let queue = [[startX, startY]];
    grid[startX][startY] = 1;
    let areaSize = 0;

    while (queue.length > 0) {
      const [x, y] = queue.shift();
      areaSize++;

      for (const [dx, dy] of directions) {
        const nx = x + dx;
        const ny = y + dy;

        if (isValid(nx, ny) && grid[nx][ny] === 0) {
          grid[nx][ny] = 1;
          queue.push([nx, ny]);
        }
      }
    }

    return areaSize;
  }

  let areas = [];
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (grid[i][j] === 0) {
        areas.push(bfs(i, j));
      }
    }
  }

  areas.sort((a, b) => a - b);
  console.log(areas.length);
  console.log(areas.join(" "));
  process.exit();
});
