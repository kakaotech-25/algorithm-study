/**
 *  제목 : 한국 그리울 서버
 *  입력 : 100 * 100
 *  제한사항 : 1s
 *  시간계산 필요 : X
 */

// Run by Node.js
const readline = require('readline');

(async () => {
    const rl = readline.createInterface({ input: process.stdin });
    
    const input = [];
    for await (const line of rl) {
        input.push(line);
    }
    rl.close();

    const pattern = input.shift();
    const [prefix, suffix] = pattern.split('*');

    input.forEach(el => {
		if (el.length < prefix.length + suffix.length) {
            console.log('NE');
		} else if (el.startsWith(prefix) && el.endsWith(suffix)) {
            console.log('DA');
        } else {
            console.log('NE');
        }
    });

    process.exit();
})();
