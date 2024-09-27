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
  const dp = [0, 1, 1, 1];
  for (i = 3; i <= 100; ++i) {
    dp[i] = dp[i - 3] + dp[i - 2];
  }

  let input = [];
  for await (const line of rl) {
    input.push(parseInt(line));
  }
  rl.close();
  input.shift();

  input.forEach((el) => {
    console.log(dp[el]);
  });

  process.exit();
})();
