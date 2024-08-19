/**
 *  제목 : 팰린드롬 만들기
 *  입력 : (최대 50글자)
 *  시간계산 필요 : X
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let input = "";

  rl.on("line", (line) => {
    input = line.trim();
    rl.close();
  });

  rl.on("close", () => {
    const freq = {};
    for (let char of input) {
      freq[char] = (freq[char] || 0) + 1;
    }

    let oddCount = 0;
    let centerChar = "";
    let leftPart = "";

    // 홀수 빈도의 알파벳 개수 계산
    for (let char in freq) {
      if (freq[char] % 2 !== 0) {
        oddCount += 1;
        centerChar = char;
      }
    }

    // 홀수 빈도의 알파벳이 2개 이상이면 팰린드롬 불가능
    if (oddCount > 1) {
      console.log("I'm Sorry Hansoo");
    } else {
      // 짝수 빈도의 알파벳으로 좌측 반을 구성
      let chars = Object.keys(freq).sort();
      for (let char of chars) {
        leftPart += char.repeat(Math.floor(freq[char] / 2));
      }

      // 팰린드롬 완성
      const result = leftPart + centerChar + [...leftPart].reverse().join("");
      console.log(result);
    }

    process.exit();
  });
})();
