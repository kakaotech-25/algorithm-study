/**
 *  제목 : NBA 농구 경기를 통한 리드 시간 계산
 *  입력 : 첫 줄에 득점 횟수 N이 주어지고, 이후 각 득점에 대한 팀 번호와 시간 정보가 주어진다.
 *  제한사항 : 1 ≤ N ≤ 100, 시간은 MM:SS 형식으로 주어진다.
 *  시간계산 필요 : 각 득점 시점마다 리드 시간을 계산하는 O(N) 복잡도
 */

// Run by Node.js
const readline = require("readline");

const toSeconds = (time) => {
  const [minutes, seconds] = time.split(":").map(Number);
  return minutes * 60 + seconds;
};

const toMMSS = (seconds) => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${String(minutes).padStart(2, "0")}:${String(
    remainingSeconds
  ).padStart(2, "0")}`;
};

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let input = [];
  rl.on("line", (line) => {
    input.push(line);
  });

  rl.on("close", () => {
    const N = parseInt(input[0], 10);
    const events = input.slice(1).map((line) => {
      const [team, time] = line.split(" ");
      return { team: parseInt(team, 10), time: toSeconds(time) };
    });

    const totalTime = 48 * 60;
    let team1Time = 0;
    let team2Time = 0;
    let currentLeader = 0; // 0: no leader, 1: team1 leading, 2: team2 leading
    let lastTime = 0;

    for (const event of events) {
      const elapsedTime = event.time - lastTime;
      if (currentLeader === 1) {
        team1Time += elapsedTime;
      } else if (currentLeader === 2) {
        team2Time += elapsedTime;
      }
      currentLeader = event.team;
      lastTime = event.time;
    }

    // 마지막 득점 이후 남은 시간 처리
    const remainingTime = totalTime - lastTime;
    if (currentLeader === 1) {
      team1Time += remainingTime;
    } else if (currentLeader === 2) {
      team2Time += remainingTime;
    }

    console.log(toMMSS(team1Time));
    console.log(toMMSS(team2Time));
  });
})();
