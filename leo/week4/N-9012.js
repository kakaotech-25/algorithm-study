/**
 *  제목 : 괄호 문자열 판별
 *  입력 : 첫 줄에 테스트 케이스 수 T가 주어지고, 이후 T개의 줄에 괄호 문자열이 주어진다.
 *  출력 : 각 테스트 케이스마다 문자열이 VPS인지 아닌지를 "YES" 또는 "NO"로 출력한다.
 */

// Run by Node.js
const readline = require("readline");

const isVPS = (ps) => {
  const stack = [];
  for (let char of ps) {
    if (char === "(") {
      stack.push(char);
    } else if (char === ")") {
      if (stack.length === 0) {
        return "NO";
      }
      stack.pop();
    }
  }
  return stack.length === 0 ? "YES" : "NO";
};

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  const input = [];
  rl.on("line", (line) => {
    input.push(line.trim());
  });

  rl.on("close", () => {
    const T = parseInt(input[0], 10);
    const results = [];
    for (let i = 1; i <= T; i++) {
      results.push(isVPS(input[i]));
    }
    console.log(results.join("\n"));
    process.exit(0);
  });
})();
