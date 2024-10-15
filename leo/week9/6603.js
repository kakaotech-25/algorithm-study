// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  const input = [];

  for await (const line of rl) {
    input.push(line.trim());
  }

  rl.close();

  const generateCombinations = (arr, start, combination, results) => {
    if (combination.length === 6) {
      results.push([...combination]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      combination.push(arr[i]);
      generateCombinations(arr, i + 1, combination, results);
      combination.pop();
    }
  };

  let idx = 0;
  while (idx < input.length) {
    const line = input[idx];
    if (line === "0") break;

    const parts = line.split(" ").map(Number);
    const k = parts[0];
    const S = parts.slice(1);

    const results = [];
    generateCombinations(S, 0, [], results);

    results.forEach((seq) => {
      console.log(seq.join(" "));
    });

    console.log("");
    idx++;
  }
})();
