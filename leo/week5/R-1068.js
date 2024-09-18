// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });

  const input = [];
  for await (const line of rl) {
    input.push(line.trim());
  }

  const N = parseInt(input[0]);
  const parentInput = input[1].split(" ").map(Number);
  const deleteNode = parseInt(input[2]);

  const children = Array.from({ length: N }, () => []);
  let root = -1;

  for (let i = 0; i < N; i++) {
    const p = parentInput[i];
    if (p === -1) {
      root = i;
    } else {
      children[p].push(i);
    }
  }

  function removeNode(node) {
    for (const child of children[node]) {
      removeNode(child);
    }
    children[node] = [];
  }

  if (deleteNode === root) {
    root = -1;
  } else {
    const parentOfDeleteNode = parentInput[deleteNode];
    const index = children[parentOfDeleteNode].indexOf(deleteNode);
    if (index !== -1) {
      children[parentOfDeleteNode].splice(index, 1);
    }
  }

  removeNode(deleteNode);

  let leafCount = 0;

  function dfs(node) {
    if (children[node].length === 0) {
      leafCount++;
      return;
    }
    for (const child of children[node]) {
      dfs(child);
    }
  }

  if (root !== -1) {
    dfs(root);
  }

  console.log(leafCount);

  process.exit();
})();
