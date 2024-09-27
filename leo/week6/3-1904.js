/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let n;
  for await (const line of rl) {
    n = parseInt(line);
  }
  rl.close();

  let dp = [0, 1, 2];
  for (let i = 3; i <= n; ++i) {
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746;
  }

  console.log(dp[n]);

  process.exit();
})();
