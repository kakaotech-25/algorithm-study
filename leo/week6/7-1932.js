// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  let input = [];
  for await (const line of rl) {
    input.push(line);
  }
  const n = parseInt(input[0]);
  const triangle = [];
  for (let i = 1; i <= n; i++) {
    triangle.push(input[i].split(" ").map(Number));
  }
  const dp = [];
  for (let i = 0; i < n; i++) {
    dp[i] = [];
    for (let j = 0; j <= i; j++) {
      if (i === 0 && j === 0) {
        dp[i][j] = triangle[i][j];
      } else if (j === 0) {
        dp[i][j] = dp[i - 1][j] + triangle[i][j];
      } else if (j === i) {
        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
      } else {
        dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
      }
    }
  }
  const result = Math.max(...dp[n - 1]);
  console.log(result);
})();
