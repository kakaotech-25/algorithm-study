const readline = require("readline");

const memo = Array.from({ length: 101 }, () =>
  Array.from({ length: 101 }, () => Array(101).fill(null))
);

function w(a, b, c) {
  if (a <= 0 || b <= 0 || c <= 0) {
    return 1;
  }

  if (a > 20 || b > 20 || c > 20) {
    return w(20, 20, 20);
  }

  if (memo[a][b][c] !== null) {
    return memo[a][b][c];
  }

  if (a < b && b < c) {
    memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
  } else {
    memo[a][b][c] =
      w(a - 1, b, c) +
      w(a - 1, b - 1, c) +
      w(a - 1, b, c - 1) -
      w(a - 1, b - 1, c - 1);
  }

  return memo[a][b][c];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const [a, b, c] = line.split(" ").map(Number);

  if (a === -1 && b === -1 && c === -1) {
    rl.close();
    return;
  }

  console.log(`w(${a}, ${b}, ${c}) = ${w(a, b, c)}`);
});
