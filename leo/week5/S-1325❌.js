const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  const lines = [];

  for await (const line of rl) {
    lines.push(line);
    if (lines.length === parseInt(lines[0].split(" ")[1]) + 1) {
      rl.close();
    }
  }

  const [firstLine, ...restLines] = lines;
  const [N, M] = firstLine.trim().split(" ").map(Number);
  const adj = Array.from({ length: N + 1 }, () => []);
  const counts = Array(N + 1).fill(0);

  for (let line of restLines) {
    const [A, B] = line.trim().split(" ").map(Number);
    adj[B].push(A);
  }

  const maxCounts = [];
  let maxCount = 0;

  for (let i = 1; i <= N; i++) {
    const visited = Array(N + 1).fill(false);
    const stack = [i];
    visited[i] = true;
    let count = 1;

    while (stack.length > 0) {
      const node = stack.pop();
      for (const neighbor of adj[node]) {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          stack.push(neighbor);
          count++;
        }
      }
    }

    counts[i] = count;

    if (count > maxCount) {
      maxCount = count;
      maxCounts.length = 0;
      maxCounts.push(i);
    } else if (count === maxCount) {
      maxCounts.push(i);
    }
  }

  console.log(maxCounts.sort((a, b) => a - b).join(" "));
})();
