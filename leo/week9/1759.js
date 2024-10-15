// Run by Node.js
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
let lines = [];
rl.on("line", (l) => lines.push(l)).on("close", () => {
  const [L, C] = lines[0].split(" ").map(Number);
  const S = lines[1].split(" ").sort();
  const V = new Set(["a", "e", "i", "o", "u"]);
  let r = [];
  const f = (i, a) => {
    if (a.length === L) {
      let c = a.filter((x) => V.has(x)).length;
      if (c >= 1 && L - c >= 2) r.push(a.join(""));
      return;
    }
    for (let j = i; j < C; j++) f(j + 1, a.concat(S[j]));
  };
  f(0, []);
  console.log(r.join("\n"));
});
