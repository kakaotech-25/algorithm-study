/**
 *  입력 : 최대 9개
 *  제한사항 : 2초 (2억번 연산)
 *  시간계산 필요 : X
 */

const fs = require('fs');

const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split('\n')

// 전체 합
let sum = 0;
input.map((el) => sum += +el);

// 범인찾기
let first, second;
for (let i = 0; i < input.length; ++i) {
    for (let j = i + 1; j < input.length; ++j) {
        if (sum - input[i] - input[j] === 100)  {
            first = input[i];
            second = input[j];
            break;
        }
    }
}

//결과 정렬 후 출력
input.sort((x, y) => x - y).map(el => {
    if (el !== first && el !== second) {
        console.log(el)
    }
})

