/**
 *  제목 : 주몽 투포인터
 *  입력 : 15000
 *  제한사항 : 2중 for문으로 해결불가
 *  시간 제한 : O 투포인터 사용하면 nlogn
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
    const N = parseInt(input[0]);
    const M = parseInt(input[1]);
    let materials = input[2].split(" ").map(Number);

    materials.sort((a, b) => a - b);

    let count = 0;
    let left = 0;
    let right = N - 1;

    while (left < right) {
      const sum = materials[left] + materials[right];

      if (sum === M) {
        count++;
        left++;
        right--;
      } else if (sum < M) {
        left++;
      } else {
        right--;
      }
    }

    console.log(count);

    process.exit();
  });
})();
