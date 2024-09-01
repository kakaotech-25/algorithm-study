/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

const solve = (n) => {
  let num = 1n;
  let count = 1n;

  while (true) {
    if (num % n === 0n) {
      return count;
    }
    count += 1n;
    num = num * 10n + 1n; // 다음 1로만 이루어진 수
  }
};

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const results = [];

  for await (const line of rl) {
    const n = BigInt(line.trim());
    if (n === null || n === 0n) break;
    results.push(solve(n).toString());
  }

  console.log(results.join("\n"));

  rl.close();
  process.exit();
})();
