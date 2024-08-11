/**
 *  펠린드롬
 *  입력 : 1줄, 100개
 *  제한사항 : 1초
 *  시간계산 필요 : X
 */

const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim();

let start = 0, end = input.length - 1;
while(start < end) {
    if (input[start] !== input[end]) {
        console.log(0);
        return;
    }
    ++start;
    --end;
}
console.log(1);