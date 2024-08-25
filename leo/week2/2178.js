/**
 *  제목 : 미로탐색
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });

  let input = [];
  for await (const line of rl) {
    input.push(line);
  }
  rl.close();

  const [height, width] = input.shift().split(" ").map(Number);
  const maze = input.map((line) => line.split("").map(Number));

  const directions = [
    [0, 1], // 아래
    [1, 0], // 오른쪽
    [0, -1], // 위
    [-1, 0], // 왼쪽
  ];

  const bfs = () => {
    let queue = [[0, 0, 1]]; // 시작점 (x, y, depth)
    let visited = Array.from({ length: height }, () =>
      Array(width).fill(false)
    );
    visited[0][0] = true;

    while (queue.length > 0) {
      let [x, y, depth] = queue.shift();

      // 도착지에 도달한 경우
      if (x === width - 1 && y === height - 1) {
        return depth;
      }

      for (const [dx, dy] of directions) {
        const nx = x + dx;
        const ny = y + dy;

        // 유효한 범위 내에 있고, 방문하지 않았으며, 벽이 아닌 경우
        if (
          nx >= 0 &&
          nx < width &&
          ny >= 0 &&
          ny < height &&
          !visited[ny][nx] &&
          maze[ny][nx] === 1
        ) {
          visited[ny][nx] = true;
          queue.push([nx, ny, depth + 1]);
        }
      }
    }

    return -1; // 도달할 수 없는 경우 (문제의 조건상 항상 도달 가능)
  };

  // BFS 실행 및 결과 출력
  const result = bfs();
  console.log(result);

  process.exit();
})();
