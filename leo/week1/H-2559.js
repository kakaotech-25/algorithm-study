/**
 *  제목 : 수열
 *  사용 알고리즘 : 슬라이딩 윈도우
 *  입력 : 100000
 *  제한사항 :
 *      n ~ m 까지 전부 더하고 한칸 이동하고 전부 더하면(2중 for문) 100000^2 100초 가량 시간을 소요하게 된다. O(n2)
 *      한칸 이동한뒤 이동한 인덱스 값을 더하고, 없어진 인덱스 값을 빼면 회차당 2번 연산으로 충분하다. O(n)
 *  시간계산 필요 : O
 */

// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let input = [];
  for await (const line of rl) {
    input.push(line);
  }
  rl.close;

  const [N, K] = input.shift().split(" ").map(Number);
  const arr = input.shift().split(" ").map(Number);

  //초기 윈도우 생성
  let max = 0,
    sum = 0;
  for (let i = 0; i < K; ++i) {
    sum += arr[i];
  }

  max = sum;
  const slideWindow = (left, right, sum) => {
    sum -= arr[left];
    sum += arr[right];
    return sum;
  };

  for (let i = 0; i < N - K; ++i) {
    // 슬라이딩
    sum = slideWindow(i, i + K, sum);

    //최댓값 갱신
    if (sum > max) {
      max = sum;
    }
  }
  console.log(max);

  process.exit();
})();
