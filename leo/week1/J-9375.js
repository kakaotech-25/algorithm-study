/**
 *  제목 : 패션왕 신해빈
 *  입력 : T(1 ≤ T ≤ 100)
 *  제한사항 : X
 *  시간계산 필요 : O(T * n), 최대 T=100, n=30의 경우를 고려한 시간복잡도 계산
 */

// Run by Node.js
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const T = parseInt(input[0]); // 테스트 케이스의 수
  let result = [];

  let index = 1;
  for (let i = 0; i < T; i++) {
    const n = parseInt(input[index]);
    let clothesMap = {};

    for (let j = 1; j <= n; j++) {
      const [name, type] = input[index + j].split(" ");

      if (clothesMap[type]) {
        clothesMap[type]++;
      } else {
        clothesMap[type] = 1;
      }
    }

    let combinations = 1;

    for (let key in clothesMap) {
      combinations *= clothesMap[key] + 1;
    }

    // 알몸이 아닌 경우만 계산
    result.push(combinations - 1);

    index += n + 1;
  }

  console.log(result.join("\n"));
  process.exit();
});
