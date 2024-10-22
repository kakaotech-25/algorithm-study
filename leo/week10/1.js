// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let input = [];
  for await (const line of rl) {
    input.push(line);
  }
  rl.close();

  const n = parseInt(input[0]);
  const h = input[1].split(" ").map(Number);

  let cnt = 0;

  for (let e of h) {
    let remain = e % 10;
    cnt += Math.floor(e / 10) * 4;
    if (remain > 0) {
      for (let i = 0; i < 4; i++) {
        cnt += 1;
        remain -= ((cnt - 1) % 4) + 1;
        if (remain <= 0) {
          break;
        }
      }
    }
  }

  console.log(cnt);
  process.exit();
})();
