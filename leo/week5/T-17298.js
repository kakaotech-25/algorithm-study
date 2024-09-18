// Run by Node.js

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  const input = [];

  for await (const line of rl) {
    input.push(line);
    if (input.length === 2) {
      rl.close();
    }
  }

  const N = parseInt(input[0]);
  const A = input[1].trim().split(" ").map(Number);
  const stack = [];
  const NGE = Array(N).fill(-1);

  for (let i = 0; i < N; i++) {
    while (stack.length > 0 && A[stack[stack.length - 1]] < A[i]) {
      NGE[stack.pop()] = A[i];
    }
    stack.push(i);
  }

  console.log(NGE.join(" "));

  process.exit();
})();
