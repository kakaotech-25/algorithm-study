// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  const input = [];
  for await (const line of rl) {
    input.push(line.trim());
  }

  const [N, M] = input[0].split(" ").map(Number);
  const grid = input.slice(1).map((line) => line.split(" ").map(Number));

  let time = 0;
  let prevCheese = 0;
  let totalCheese = 0;

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (grid[i][j] === 1) totalCheese++;
    }
  }

  while (totalCheese > 0) {
    prevCheese = totalCheese;
    const visited = Array.from({ length: N }, () => Array(M).fill(false));
    const queue = [[0, 0]];
    visited[0][0] = true;

    while (queue.length) {
      const [x, y] = queue.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y - dy[i];
        if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny]) {
          if (grid[nx][ny] === 0) {
            visited[nx][ny] = true;
            queue.push([nx, ny]);
          } else if (grid[nx][ny] === 1) {
            visited[nx][ny] = true;
            grid[nx][ny] = 2;
          }
        }
      }
    }

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (grid[i][j] === 2) {
          grid[i][j] = 0;
          totalCheese--;
        }
      }
    }

    time++;
  }

  console.log(time);
  console.log(prevCheese);

  process.exit();
})();
