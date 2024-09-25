/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

var count = 0;
var count2 = 0;

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let input;
  for await (const line of rl) {
    input = +line;
  }
  rl.close();

  fib(input);
  fib2(input);

  console.log(count, count2);

  process.exit();
})();

function fib(n) {
  if (n == 1 || n == 2) {
    count++;
    return 1;
  } else return fib(n - 1) + fib(n - 2);
}

function fib2(n) {
  if (n <= 2) return;

  const dp = [0, 1, 1];
  for (let i = 3; i <= n; ++i) {
    count2++;
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}
