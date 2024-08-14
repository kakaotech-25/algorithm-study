/**
 *  제목 : 열받는 포켓몬도감(하.. 문제읽지말걸)
 *  입력 : 100,000줄
 *  제한사항 :
 *    이름에 해당하는 인덱스, 혹은 인덱스에 해당하는 이름
 *      O(n2)은 100초, hash table을 사용해야함
 *  시간계산 필요 : O
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let index = 0;
  let n = 0,
    m = 0;
  const nmap = new Map();
  const imap = new Map();
  const answer = [];
  for await (const line of rl) {
    if (index == 0) {
      [n, m] = line.split(" ").map(Number);
    }
    // create dictionary
    if (index && index <= n) {
      nmap.set(line, index);
      imap.set(index, line);
    }
    // question parsing
    if (line && index > n) {
      if (line[0].charCodeAt() >= "A".charCodeAt()) {
        //문자
        answer.push(nmap.get(line));
      } else {
        //숫자
        answer.push(imap.get(+line));
      }
    }
    ++index;
  }
  rl.close();

  answer.map((el) => console.log(el));
  process.exit();
})();
