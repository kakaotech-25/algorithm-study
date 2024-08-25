/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N, M, J;
let positions = [];
let index = 0;

rl.on("line", function (line) {
  if (index === 0) {
    [N, M] = line.split(" ").map(Number);
    index++;
  } else if (index === 1) {
    J = parseInt(line);
    index++;
  } else {
    positions.push(parseInt(line));
    if (positions.length === J) {
      rl.close();
    }
  }
}).on("close", function () {
  let left = 1; // 바구니의 시작 위치 (1-based index)
  let right = M; // 바구니의 끝 위치
  let moveCount = 0;

  for (let i = 0; i < J; i++) {
    const apple = positions[i];

    if (apple < left) {
      // 사과가 바구니의 왼쪽에 떨어진 경우
      moveCount += left - apple;
      right -= left - apple;
      left = apple;
    } else if (apple > right) {
      // 사과가 바구니의 오른쪽에 떨어진 경우
      moveCount += apple - right;
      left += apple - right;
      right = apple;
    }
    // 사과가 바구니 범위 내에 있는 경우에는 이동하지 않음
  }

  console.log(moveCount);
  process.exit();
});
