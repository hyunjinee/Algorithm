
# 1310. XOR Queries of a Subarray
[문제 보러가기](https://leetcode.com/problems/xor-queries-of-a-subarray/)

## 🅰 설계

arr가 주어지고, queries[i] = [Li, Ri], 각각의 쿼리는 두원소의 Li Ri 사이의 모든 arr에대한 원소의XOR연산이다. 즉 다시말해서, XOR 연산을 하는 기능을 하는 함수를 하나 만들고, output arr 에 push 하는 식으로 진행해봅시당.    

일단 한 한시간? 을 생각했다. 솔직히xor 연산에대해 아직 정확히 감이 안온다. 하지만 아래 두 규칙은 이 문제를 푸는데 알고 있어야한다.

> A xor B xor B = A
> xor[0,i] ^ xor[i, j] = xor[0,j]

이를 기반으로 풀면 아래와같다.
```ts
function xorQuexries(arr: number[], queries: number[][]): number[] {
    // result array
    const res: number[] = [];

    // generate prefix array
    for (let i = 1; i < arr.length; i++) {
        arr[i] ^= arr[i - 1];
    }

    // iterate thru queries
    for (let i = 0; i < queries.length; i++) {
        // get query values
        const [x, y] = queries[i];
        // get prefix of first, xor'd with prefix of second
        // unless it's 0, then just return prefix of second
        res.push(x > 0 ? arr[x - 1] ^ arr[y] : arr[y]);
    }

    return res;
}
```
## ✅ 후기
// 새롭게 알게되거나 공유해서 알게된 점
같은걸 xor 해서 없애는거.. 신기했다.

// 고생한 점

진짜 개고생했다. 비트연산 공부할게염.. 디질거같아..
