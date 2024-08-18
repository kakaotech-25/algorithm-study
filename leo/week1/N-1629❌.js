/**
 *  제목 : 곱셈 (큰 제곱수구하기)
 *  입력 :
 *  제한사항 : C로 구현하려면 귀찮겠당 ㅎㅎ
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let input;

  for await (const line of rl) {
    input = line;
    rl.close();
  }

  let [A, B, C] = input.split(" ").map(BigInt);
  console.log(A ** B % C);

  process.exit();
})();
