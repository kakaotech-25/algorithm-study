/**
 *  농구경기
 *  입력 : 150줄, 줄당 30글자
 *  제한사항 : 1초
 *  시간계산 필요 : X
 */

// Run by Node.js

const readline = require('readline');
(async () => {
    //입력을 배열형태로 저장
	let rl = readline.createInterface({ input: process.stdin });	
    let input = []
	for await (const line of rl) {
        input.push(line);
	}	
    rl.close();

    // 알파벳 사전 
    const dict = Array.from({length: 26}, () => 0)

    //첫 줄 필요없음
    input.shift();

    //첫 알파벳 검사 후 카운트 
    input.map((el) => {
        const targetIndex = el[0].charCodeAt() - 'a'.charCodeAt();
        dict[targetIndex] += 1;
    })

    //선발 가능여부 체크
    const result = [];
    let flag = false;
    for (let i = 0; i < dict.length; ++i) {
        if (dict[i] >= 5) {
            result.push(String.fromCharCode(i + 'a'.charCodeAt()));
            flag = true;
        }
    }

    if (flag) {
        console.log(result.join(''));
    } else {
        console.log('PREDAJA');
    }

	process.exit();
})();
