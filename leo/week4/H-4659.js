/**
 *  제목 : 비밀번호 발음하기
 *  입력 : 여러 줄에 걸쳐 비밀번호가 주어짐. 마지막 줄은 'end'
 *  제한사항 : 비밀번호는 한 글자 이상 20 글자 이하의 소문자로 구성. 대문자는 포함되지 않음
 *  시간계산 필요 : 시간 복잡도는 O(n)으로 각 비밀번호를 검사 (n은 비밀번호 길이)
 */

// Run by Node.js
const readline = require("readline");

const vowels = new Set(["a", "e", "i", "o", "u"]);

function isAcceptable(password) {
  let hasVowel = false;
  let consecutiveVowelCount = 0;
  let consecutiveConsonantCount = 0;

  for (let i = 0; i < password.length; i++) {
    const char = password[i];
    const isVowel = vowels.has(char);

    if (isVowel) hasVowel = true;

    if (isVowel) {
      consecutiveVowelCount++;
      consecutiveConsonantCount = 0;
    } else {
      consecutiveConsonantCount++;
      consecutiveVowelCount = 0;
    }

    if (consecutiveVowelCount === 3 || consecutiveConsonantCount === 3) {
      return false;
    }

    if (i > 0 && char === password[i - 1] && char !== "e" && char !== "o") {
      return false;
    }
  }

  return hasVowel;
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    if (line === "end") break;
    const result = isAcceptable(line) ? "is acceptable." : "is not acceptable.";
    console.log(`<${line}> ${result}`);
  }

  rl.close();
  process.exit();
})();
