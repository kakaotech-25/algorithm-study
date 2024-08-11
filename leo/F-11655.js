/**
 *  ROT13
 *  입력 : 1줄 100글자
 *  제한사항 : 1초
 *  시간계산 필요 : X
 */

// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
    let input;
	for await (const line of rl) {
        input = line;
	    rl.close();
	}

    const convertAscii = (char) => char.charCodeAt(0);
    const [a, z, A, Z] = ['a', 'z', 'A', 'Z'].map(convertAscii);

    //앞으로 13자 미는 함수
    const push13Alpha = (charcode, selector) => {
        charcode = charcode - convertAscii(selector);
        charcode = (charcode + 13) % 26;
        charcode = charcode + convertAscii(selector);
        return String.fromCharCode(charcode);
    }

    let result = ''
    for (char of input) {
        const num = convertAscii(char);
        if (a <= num && num <= z) {
            result += push13Alpha(convertAscii(char), 'a')
        } else if (A <= num && num <= Z) {
            result += push13Alpha(convertAscii(char), 'A')
        } else {
            result += char;
        }
    }

    console.log(result)

	process.exit();
})();
