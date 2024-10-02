/**
 *  제목 : 재귀함수가 뭔가요?
 *  입력 : 첫째 줄에 N(1 ≤ N ≤ 50)이 주어진다.
 *  제한사항 : N은 1 이상 50 이하의 정수
 *  시간계산 필요 : 재귀 깊이가 최대 50이므로, 시간 제한 내에 문제 해결 가능
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  for await (const line of rl) {
    let N = parseInt(line);

    console.log("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");

    function recursiveConversation(currentLevel, totalLevels) {
      let indent = "____".repeat(currentLevel);
      console.log(`${indent}"재귀함수가 뭔가요?"`);
      if (currentLevel === totalLevels) {
        console.log(`${indent}"재귀함수는 자기 자신을 호출하는 함수라네"`);
      } else {
        console.log(
          `${indent}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.`
        );
        console.log(
          `${indent}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.`
        );
        console.log(
          `${indent}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."`
        );
        recursiveConversation(currentLevel + 1, totalLevels);
      }
      console.log(`${indent}라고 답변하였지.`);
    }

    recursiveConversation(0, N);

    rl.close();
  }

  process.exit();
})();
