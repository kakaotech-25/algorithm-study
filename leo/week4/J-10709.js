/**
 *  제목 : Troyangles
 *  입력 : 첫 줄에 격자의 크기 N이 주어진다. 이후 N개의 줄에 N개의 문자로 이루어진 격자가 주어진다.
 *  제한사항 : 1 ≤ N ≤ 2000, 각 줄은 '.' 또는 '#'로 구성된다.
 *  시간계산 필요 : O(N^2) - DP를 이용해 각 위치에서 가능한 삼각형의 최대 높이를 계산.
 */

// Run by Node.js
const readline = require("readline");

const countTriangles = (grid, N) => {
  let count = 0;
  let dp = Array.from(Array(N), () => Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (grid[i][j] === "#") {
        dp[i][j] = 1; // 최소 높이 1
        if (i > 0 && j > 0 && j < N - 1) {
          dp[i][j] =
            Math.min(dp[i - 1][j - 1], dp[i - 1][j + 1], dp[i - 1][j]) + 1;
        }
        count += dp[i][j];
      }
    }
  }

  return count;
};

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let input = [];
  rl.on("line", (line) => {
    input.push(line);
  }).on("close", () => {
    const N = parseInt(input[0], 10);
    const grid = input.slice(1);
    const result = countTriangles(grid, N);
    console.log(result);
    process.exit(0);
  });
})();
