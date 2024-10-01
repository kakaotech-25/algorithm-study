// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let input = [];
  for await (const line of rl) {
    input.push(line);
  }

  let N = parseInt(input[0]);
  let paper = [];
  for (let i = 1; i <= N; i++) {
    paper.push(input[i].trim().split(" ").map(Number));
  }

  let counts = { 0: 0, 1: 0 };

  function checkSameColor(x, y, size) {
    let color = paper[x][y];
    for (let i = x; i < x + size; i++) {
      for (let j = y; j < y + size; j++) {
        if (paper[i][j] !== color) {
          return false;
        }
      }
    }
    return true;
  }

  function divideAndConquer(x, y, size) {
    if (checkSameColor(x, y, size)) {
      counts[paper[x][y]]++;
    } else {
      let newSize = size / 2;
      divideAndConquer(x, y, newSize); // Top-left
      divideAndConquer(x, y + newSize, newSize); // Top-right
      divideAndConquer(x + newSize, y, newSize); // Bottom-left
      divideAndConquer(x + newSize, y + newSize, newSize); // Bottom-right
    }
  }

  divideAndConquer(0, 0, N);

  console.log(counts["0"]);
  console.log(counts["1"]);

  process.exit();
})();
