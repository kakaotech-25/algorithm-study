/**
 *  제목 : 괄호 짝맞추기
 *  제한사항 : ? 전형적인 스택문제
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let input = [];

  rl.on("line", (line) => {
    input.push(line.trim());
  });

  rl.on("close", () => {
    const N = parseInt(input[0]); // 단어의 수
    let goodWordCount = 0;

    for (let i = 1; i <= N; i++) {
      let stack = [];
      let word = input[i];

      for (let char of word) {
        if (stack.length > 0 && stack[stack.length - 1] === char) {
          stack.pop(); // 짝이 맞으면 스택에서 제거
        } else {
          stack.push(char); // 그렇지 않으면 스택에 추가
        }
      }

      if (stack.length === 0) {
        goodWordCount++; // 스택이 비어 있으면 '좋은 단어'
      }
    }

    console.log(goodWordCount);

    process.exit();
  });
})();
