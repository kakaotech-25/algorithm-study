/**
 *  입력 : 최대 100개
 *  제한사항 : 1초
 *  시간계산 필요 : X
 */

const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim()

// 26길이 딕셔너리 초기화
const result = Array.from({ length: 26 }).fill(0)

// 개수 카운트
for (el of input) {
    const targetIndex = el.charCodeAt() - 'a'.charCodeAt()
    result[targetIndex] += 1;
}

// 공백 포함 출력
console.log(result.join(' '))

