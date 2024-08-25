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

let N;
let matrix = [];

rl.on("line", function (line) {
  if (!N) {
    N = parseInt(line);
  } else {
    matrix.push(line.split("").map(Number));
    if (matrix.length === N) rl.close();
  }
}).on("close", function () {
  function compress(x, y, size) {
    const firstValue = matrix[x][y];
    let isHomogeneous = true;

    // Check if all elements in the current part are the same
    for (let i = x; i < x + size; i++) {
      for (let j = y; j < y + size; j++) {
        if (matrix[i][j] !== firstValue) {
          isHomogeneous = false;
          break;
        }
      }
      if (!isHomogeneous) break;
    }

    // If homogeneous, return the single value
    if (isHomogeneous) {
      return firstValue.toString();
    }

    // Otherwise, divide into 4 parts
    const half = size / 2;
    const topLeft = compress(x, y, half);
    const topRight = compress(x, y + half, half);
    const bottomLeft = compress(x + half, y, half);
    const bottomRight = compress(x + half, y + half, half);

    return `(${topLeft}${topRight}${bottomLeft}${bottomRight})`;
  }

  const result = compress(0, 0, N);
  console.log(result);
  process.exit();
});
