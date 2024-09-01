/**
 *  제목 : 영화감독 숌
 *  입력 : 첫 줄에 N이 주어진다 (1 ≤ N ≤ 10,000)
 *  출력 : N번째로 작은 종말의 수를 출력한다.
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const input = await new Promise((resolve) => rl.question("", resolve));
  const N = parseInt(input.trim(), 10);

  let count = 0;
  let number = 666;

  while (true) {
    if (String(number).includes("666")) {
      count += 1;
    }
    if (count === N) {
      console.log(number);
      break;
    }
    number += 1;
  }

  rl.close();
  process.exit();
})();
