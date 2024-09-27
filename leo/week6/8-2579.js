// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  let input = [];
  for await (const line of rl) {
    input.push(line.trim());
  }
  const n = parseInt(input[0]);
  const score = [0];
  for (let i = 1; i <= n; i++) {
    score.push(parseInt(input[i]));
  }
  const dp = Array.from({ length: n + 1 }, () => [0, 0]);
  dp[1][0] = score[1];
  dp[1][1] = score[1];
  for (let i = 2; i <= n; i++) {
    dp[i][0] = Math.max(dp[i - 2][0], dp[i - 2][1]) + score[i];
    dp[i][1] = dp[i - 1][0] + score[i];
  }
  const result = Math.max(dp[n][0], dp[n][1]);
  console.log(result);
})();
