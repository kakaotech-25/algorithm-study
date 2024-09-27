// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  let input = [];
  for await (const line of rl) {
    input.push(line);
  }
  const N = parseInt(input[0]);
  const cost = [];
  for (let i = 1; i <= N; i++) {
    cost.push(input[i].split(" ").map(Number));
  }
  const dp = Array.from({ length: N }, () => [0, 0, 0]);
  dp[0][0] = cost[0][0];
  dp[0][1] = cost[0][1];
  dp[0][2] = cost[0][2];
  for (let i = 1; i < N; i++) {
    dp[i][0] = cost[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);
    dp[i][1] = cost[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);
    dp[i][2] = cost[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
  }
  const result = Math.min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]);
  console.log(result);
})();
