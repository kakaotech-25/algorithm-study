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

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  let T = parseInt(input[0]); // 테스트 케이스 개수
  let index = 1;

  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1], // 상하좌우 네 방향
  ];

  const dfs = (x, y, field, M, N) => {
    let stack = [[x, y]];
    field[y][x] = 0; // 방문한 곳은 0으로 바꿔줌

    while (stack.length > 0) {
      let [curX, curY] = stack.pop();

      for (let [dx, dy] of directions) {
        let newX = curX + dx;
        let newY = curY + dy;

        if (
          newX >= 0 &&
          newY >= 0 &&
          newX < M &&
          newY < N &&
          field[newY][newX] === 1
        ) {
          stack.push([newX, newY]);
          field[newY][newX] = 0; // 방문 처리
        }
      }
    }
  };

  for (let t = 0; t < T; t++) {
    const [M, N, K] = input[index++].split(" ").map(Number);
    let field = Array.from(Array(N), () => Array(M).fill(0));

    for (let i = 0; i < K; i++) {
      const [x, y] = input[index++].split(" ").map(Number);
      field[y][x] = 1; // 배추가 심어진 위치 표시
    }

    let wormCount = 0;

    for (let y = 0; y < N; y++) {
      for (let x = 0; x < M; x++) {
        if (field[y][x] === 1) {
          // 배추가 있는 곳에서 DFS 시작
          dfs(x, y, field, M, N);
          wormCount++;
        }
      }
    }

    console.log(wormCount);
  }
});
