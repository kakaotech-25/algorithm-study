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

  let counts = { "-1": 0, 0: 0, 1: 0 };

  function checkSameNumber(x, y, size) {
    let firstNumber = paper[x][y];
    for (let i = x; i < x + size; i++) {
      for (let j = y; j < y + size; j++) {
        if (paper[i][j] !== firstNumber) {
          return false;
        }
      }
    }
    return true;
  }

  function divideAndConquer(x, y, size) {
    if (checkSameNumber(x, y, size)) {
      counts[paper[x][y]]++;
    } else {
      let newSize = size / 3;
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          divideAndConquer(x + i * newSize, y + j * newSize, newSize);
        }
      }
    }
  }

  divideAndConquer(0, 0, N);

  console.log(counts["-1"]);
  console.log(counts["0"]);
  console.log(counts["1"]);

  process.exit();
})();
