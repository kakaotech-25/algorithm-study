/**
 *  제목 :
 *  입력 :
 *  제한사항 :
 *  시간계산 필요 :
 */

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const [N, C] = input[0].split(" ").map(Number);
  const sequence = input[1].split(" ").map(Number);

  const frequencyMap = new Map();
  const orderMap = new Map();
  let order = 0;

  // 빈도와 등장 순서 계산
  for (let num of sequence) {
    if (!frequencyMap.has(num)) {
      frequencyMap.set(num, 0);
      orderMap.set(num, order++);
    }
    frequencyMap.set(num, frequencyMap.get(num) + 1);
  }

  // 빈도 및 등장 순서에 따라 정렬
  sequence.sort((a, b) => {
    const freqA = frequencyMap.get(a);
    const freqB = frequencyMap.get(b);

    if (freqA === freqB) {
      return orderMap.get(a) - orderMap.get(b);
    }
    return freqB - freqA;
  });

  console.log(sequence.join(" "));
});
