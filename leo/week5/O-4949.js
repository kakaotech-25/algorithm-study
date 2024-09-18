/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let input = [];
  for await (const line of rl) {
    input.push(line);
  }
  rl.close();

  input.forEach((line) => {
    let stack = [];
    let flag = true;
    let count = 0;
    for (ch of line) {
      switch (ch) {
        case "(":
          stack.push("(");
          ++count;
          break;
        case ")":
          if (stack.at(-1) === "(") stack.pop();
          else flag = false;
          break;
        case "[":
          stack.push("[");
          ++count;
          break;
        case "]":
          if (stack.at(-1) === "[") stack.pop();
          else flag = false;
          break;
        case ".":
          if (count) {
            console.log(stack.length === 0 ? "yes" : "no");
          }
          break;
        default:
          ++count;
      }
      if (!flag) {
        console.log("no");
        break;
      }
    }
  });

  process.exit();
})();
