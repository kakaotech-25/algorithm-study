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

  const input = [];
  for await (const line of rl) {
    input.push(line);
  }
  rl.close();
  input.shift();
  const input2 = input[0].split(" ").map(Number);

  const dp = [];
  dp[0] = input2[0];

  for (let i = 1; i < input2.length; ++i) {
    dp[i] = Math.max(input2[i], dp[i - 1] + input2[i]);
  }

  console.log(Math.max(...dp));

  process.exit();
})();
