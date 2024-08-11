/**
 *  주차장 요금 계산
 *  입력 : 최대 3줄
 *  제한사항 : 1초
 *  시간계산 필요 : X
 */

const fs = require('fs');
const input = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split('\n').map(el => el.split(' ').map(Number))
const [A, B, C] = input.shift();

const time = new Array(101).fill(0);
let cost = 0;
input.forEach(el => {
    const [start, end] = el;
    for (let i = start; i < end; ++i) {
        time[i]++;
    }
})

time.forEach(el => {
    switch (el) {
        case 1:
            cost += A; 
            break;
        case 2:
            cost += B * 2;
            break;
        case 3:
            cost += C * 3;
            break;
    }
})

console.log(cost)
