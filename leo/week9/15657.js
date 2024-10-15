// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  const input = [];

  for await (const line of rl) {
    input.push(line.trim());
  }

  rl.close();

  const [N, M] = input[0].split(" ").map(Number);
  const numbers = input[1]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  const result = [];
  const combination = [];

  const backtrack = (start, depth) => {
    if (depth === M) {
      result.push([...combination]);
      return;
    }

    for (let i = start; i < N; i++) {
      combination.push(numbers[i]);
      backtrack(i, depth + 1);
      combination.pop();
    }
  };

  backtrack(0, 0);

  console.log(result.map((seq) => seq.join(" ")).join("\n"));
})();
