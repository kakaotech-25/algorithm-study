// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  const input = [];
  for await (const line of rl) {
    input.push(line.trim());
    if (input.length === parseInt(input[0].split(" ")[0]) + 1) {
      rl.close();
    }
  }

  const [N, M] = input[0].split(" ").map(Number);
  const lab = input.slice(1).map((line) => line.split(" ").map(Number));

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  let maxSafeArea = 0;

  const emptySpaces = [];
  const viruses = [];

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (lab[i][j] === 0) {
        emptySpaces.push([i, j]);
      } else if (lab[i][j] === 2) {
        viruses.push([i, j]);
      }
    }
  }

  const combinations = getCombinations(emptySpaces, 3);

  combinations.forEach((walls) => {
    const tempLab = lab.map((row) => row.slice());

    walls.forEach(([x, y]) => {
      tempLab[x][y] = 1;
    });

    const infectedLab = spreadVirus(tempLab, viruses);

    const safeArea = countSafeArea(infectedLab);
    if (safeArea > maxSafeArea) {
      maxSafeArea = safeArea;
    }
  });

  console.log(maxSafeArea);

  process.exit();

  function getCombinations(arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((value) => [value]);
    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = getCombinations(rest, selectNumber - 1);
      const attached = combinations.map((combination) => [
        fixed,
        ...combination,
      ]);
      results.push(...attached);
    });
    return results;
  }

  function spreadVirus(labMap, virusPositions) {
    const N = labMap.length;
    const M = labMap[0].length;
    const queue = virusPositions.map((pos) => pos.slice());

    while (queue.length) {
      const [x, y] = queue.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (labMap[nx][ny] === 0) {
          labMap[nx][ny] = 2;
          queue.push([nx, ny]);
        }
      }
    }
    return labMap;
  }

  function countSafeArea(labMap) {
    let count = 0;
    for (let i = 0; i < labMap.length; i++) {
      for (let j = 0; j < labMap[0].length; j++) {
        if (labMap[i][j] === 0) {
          count++;
        }
      }
    }
    return count;
  }
})();
