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

  for await (const line of rl) {
    console.log("Hello Goorm! Your input is", line);
    rl.close();
  }

  process.exit();
})();
