/**
 *  제목 : 교수님을 대신하여 팩토리얼의 끝 0의 개수 구하기
 *  입력 : 첫 줄에 테스트 케이스의 수 T가 주어지고, 이어서 T개의 줄에 자연수 N이 주어진다.
 *  제한사항 : 1 ≤ N ≤ 1,000,000,000
 *  시간계산 필요 : 각 테스트 케이스에 대해 O(log N)의 시간 복잡도
 */

// Run by Node.js
const readline = require("readline");

const countTrailingZeros = (n) => {
  let count = 0;
  while (n >= 5) {
    n = Math.floor(n / 5);
    count += n;
  }
  return count;
};

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let input = [];
  rl.on("line", (line) => {
    input.push(line);
  }).on("close", () => {
    const T = parseInt(input[0], 10); // 첫 줄에서 테스트 케이스 수 T를 읽음
    for (let i = 1; i <= T; i++) {
      const N = parseInt(input[i], 10);
      console.log(countTrailingZeros(N));
    }
    process.exit(0);
  });
})();
