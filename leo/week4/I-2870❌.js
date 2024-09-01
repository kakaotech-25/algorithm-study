/**
 *  제목 : 수학숙제
 *  입력 : 첫째 줄에 줄의 개수 N이 주어지고, 이어서 N개의 줄에 문자열이 주어진다.
 *  제한사항 : 각 줄은 알파벳 소문자와 숫자로만 이루어져 있다.
 */

// Run by Node.js
const readline = require("readline");

function extractNumbers(s) {
  const numbers = [];
  let currentNumber = "";

  for (let i = 0; i < s.length; i++) {
    if (/\d/.test(s[i])) {
      currentNumber += s[i]; // 숫자일 경우 currentNumber에 추가
    } else {
      if (currentNumber.length > 0) {
        numbers.push(parseInt(currentNumber, 10)); // 숫자 스트링을 정수로 변환 후 추가
        currentNumber = ""; // currentNumber 초기화
      }
    }
  }
  if (currentNumber.length > 0) {
    numbers.push(parseInt(currentNumber, 10)); // 마지막 숫자 처리
  }

  return numbers;
}

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  const lines = [];

  for await (const line of rl) {
    lines.push(line.trim());
  }

  const N = parseInt(lines.shift(), 10); // 첫 줄에서 줄의 개수 N 읽기
  let allNumbers = [];

  for (let i = 0; i < N; i++) {
    allNumbers = allNumbers.concat(extractNumbers(lines[i])); // 각 줄에서 숫자 추출하여 추가
  }

  allNumbers.sort((a, b) => a - b); // 비내림차순으로 정렬

  for (const number of allNumbers) {
    console.log(number); // 각 숫자를 한 줄에 하나씩 출력
  }

  rl.close();
  process.exit();
})();
