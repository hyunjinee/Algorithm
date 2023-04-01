function solution(a, b, g, s, w, t) {
  //이분탐색의 범위는 걸리는 시간
  let answer = 10e5 * 4 * 10e9
  let start = 0
  //최대로 걸리는 시간
  //편도 최대시간 t = 10^5
  //왕복 최대시간 10 ^ 5 * 2 * 2(금/은) * 10 ^ 9
  let end = 10e5 * 4 * 10e9
  while (start <= end) {
    let mid = Math.floor((start + end) / 2)
    let gold_carry = 0
    let silver_carry = 0
    let all_carry = 0

    for (let i = 0; i < g.length; i++) {
      let now_gold = g[i] //i국 금
      let now_silver = s[i] //i국 은
      let now_w = w[i] //i국에서 한번에 옮길수 있는 최대 양
      let now_t = t[i] //i국에서 한번 옮길때 걸리는 시간
      let move_t = Math.floor(mid / (now_t * 2)) //일정시간동안 왕복가능 횟수
      //편도로한번더 갈 수 있으면 왕복횟수 추가
      if (mid % (now_t * 2) >= now_t) move_t++

      //금만 캤을때 캘수있는양(왕복횟수 * 한번에 옮길 수 잇는양)
      gold_carry += move_t * now_w >= now_gold ? now_gold : move_t * now_w
      //은만 캤을때
      silver_carry += move_t * now_w >= now_silver ? now_silver : move_t * now_w
      //최대로 옮길수 있는 광물의 무게(캘수 잇는 최대 광물 무게가 보유 금은의 합보다 크면 )
      all_carry +=
        move_t * now_w >= now_silver + now_gold
          ? now_silver + now_gold
          : move_t * now_w
    }
    //시간(mid)안에 가능하다
    if (a <= gold_carry && b <= silver_carry && a + b <= all_carry) {
      end = mid - 1
      answer = Math.min(answer, mid)
    } else {
      //이 시간안에 해결 불가하다
      start = mid + 1
    }
  }
  return answer
}
