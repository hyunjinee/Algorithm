const fs = require("fs");
const input = fs.readFileSync("./dev/stdin").toString().trim();
let [NM, ...grid] = input.split('\n').map(e => e.split(' ').map(Number));
const direction = [[-1, 0],[0, -1],[0, 1],[1, 0]];
console.log(solution(NM, grid));

function solution ([N, M], grid) {
  const COLOR_B = -1;
  const COLOR_R = 0;
  const EMPTY = -2;
  let result = 0;

  const check = (y, x) => 0 <= y && y < N && 0 <= x && x < N;

  const bfs = (pos, block, v) => {
    v[pos[0]][pos[1]] = true;
    const visited = JSON.parse(JSON.stringify(v));
    let queue = [pos];

    const result = [];
    let cntR = 0;

    while(queue.length > 0) {
      const size = queue.length;
      const nextQueue = [];
      for(let i = 0; i < size; i++) {
        const [y, x] = queue[i];
        result.push([y, x]);
        for(const [dy, dx] of direction) {
          const ny = dy + y;
          const nx = dx + x;
          if(!check(ny, nx)) continue;
          if(visited[ny][nx]) continue;
          if(grid[ny][nx] === EMPTY) continue;
          if(grid[ny][nx] === COLOR_B) continue;
          visited[ny][nx] = true;
          if(grid[ny][nx] === COLOR_R) {
            nextQueue.push([ny, nx]);
            cntR++;
            continue;
          }
          if(grid[ny][nx] === block) {
            nextQueue.push([ny, nx]);
            v[ny][nx] = true;
          } 
        }
      }
      queue = nextQueue;
    }

    return [result, cntR];
  }

  const drop = (grid) => {
    for(let i = 0; i < N; i++) {
      let btm = N - 1;
      for(let j = N - 1; j >= 0; j--) {
        if(grid[j][i] === EMPTY) continue;
        if(grid[j][i] === COLOR_B) {
          btm = j - 1;
          continue;
        }
        if(j !== btm) {
          const value = grid[j][i];
          grid[j][i] = EMPTY;
          grid[btm][i] = value;
        }
        btm--;
      }
    }
  }
  
  const turn = (grid) => {
    const newGrid = Array.from({length: N}, () => Array(N).fill(EMPTY));
    
    for(let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        newGrid[i][j] = grid[j][N - i - 1];        
      }
    }
    return newGrid;
  }

  while(1){
    let myBlocks = [];
    let myCntR = 0;
    const visited = Array.from({length: N}, () => Array(N).fill(false));

    for(let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if(visited[i][j]) continue;
        if(grid[i][j] < 1) continue;
        const [blocks, cntR] = bfs([i, j], grid[i][j], visited);
        if(myBlocks.length < blocks.length) {
          myBlocks = blocks;
          myCntR = cntR;
          continue;
        }
        if(myBlocks.length === blocks.length && myCntR <= cntR) {
          myBlocks = blocks;
          myCntR = cntR;
        }
      }
    }
    
    if(myBlocks.length < 2) break;
    result += Math.pow(myBlocks.length, 2);
    myBlocks.forEach(([y, x]) => grid[y][x] = EMPTY);
    drop(grid);
    grid = turn(grid);
    drop(grid);
  }

  return result;
}
// const [[n, m], ...board] = require("fs")
//     .readFileSync("./dev/stdin")
//     .toString()
//     .trim()
//     .split("\n")
//     .map((v) => v.split(" ").map(Number)),
//   direction = [
//     [-1, 0],
//     [0, -1],
//     [0, 1],
//     [1, 0],
//   ]

// console.log(solution(n, m, board))

// function solution(n, m, board) {
//   const COLOR_B = -1
//   const COLOR_R = 0
//   const EMPTY = -2
//   let result = 0

//   const check = (y, x) => 0 <= y && y < n && 0 <= x && x < n

//   const bfs = (pos, block, v) => {
//     v[pos[0]][pos[1]] = true
//     const visited = JSON.parse(JSON.stringify(v))

//     let queue = [pos]
//     const result = []
//     let cntR = 0

//     while (queue.length > 0) {
//       const size = queue.length
//       const nextQueue = []
//       for (let i = 0; i < size; i++) {
//         const [y, x] = queue[i]
//         result.push([y, x])

//         for (const [dy, dx] of direction) {
//           const ny = dy + y
//           const nx = dx + x

//           if (!check(ny, nx)) continue
//           if (visited[ny][nx]) continue
//           if (board[ny][nx] === EMPTY) continue
//           if (board[ny][nx] === COLOR_B) continue
//           visited[ny][nx] = true
//           if (board[ny][nx] === COLOR_R) {
//             nextQueue.push([ny, nx])
//             cntR++
//             continue
//           }
//           if (board[ny][nx] === block) {
//             nextQueue.push([ny, nx])
//             v[ny][nx] = true
//           }
//         }
//       }
//       queue = nextQueue
//     }

//     return [result, cntR]
//   }

//   //   const bfs = (pos, block, v) => {
//   //     v[pos[0]][pos[1]] = true
//   //     const visited = JSON.parse(JSON.stringify(v))
//   //     let queue = [pos]

//   //     const result = []
//   //     let cntR = 0

//   //     while (queue.length > 0) {
//   //       const size = queue.length
//   //       const nextQueue = []
//   //       for (let i = 0; i < size; i++) {
//   //         const [y, x] = queue[i]
//   //         result.push([y, x])
//   //         for (const [dy, dx] of direction) {
//   //           const ny = dy + y
//   //           const nx = dx + x
//   //           if (!check(ny, nx)) continue
//   //           if (visited[ny][nx]) continue
//   //           if (grid[ny][nx] === EMPTY) continue
//   //           if (grid[ny][nx] === COLOR_B) continue
//   //           visited[ny][nx] = true
//   //           if (grid[ny][nx] === COLOR_R) {
//   //             nextQueue.push([ny, nx])
//   //             cntR++
//   //             continue
//   //           }
//   //           if (grid[ny][nx] === block) {
//   //             nextQueue.push([ny, nx])
//   //             v[ny][nx] = true
//   //           }
//   //         }
//   //       }
//   //       queue = nextQueue
//   //     }

//   //     return [result, cntR]
//   //   }

//   const drop = (board) => {
//     for (let i = 0; i < n; i++) {
//       let btm = n - 1
//       for (let j = n - 1; j >= 0; j--) {
//         if (board[j][i] === EMPTY) continue

//         if (board[j][i] === COLOR_B) {
//           btm = j - 1
//           continue
//         }

//         if (j !== btm) {
//           const value = board[j][i]
//           board[j][i] = EMPTY
//           board[btm][i] = value
//         }
//         btm--
//       }
//     }
//   }

//   const turn = (grid) => {
//     const newGrid = Array.from({ length: n }, () => Array(n).fill(EMPTY))

//     for (let i = 0; i < n; i++) {
//       for (let j = 0; j < n; j++) {
//         newGrid[i][j] = grid[j][n - i - 1]
//       }
//     }
//     return newGrid
//   }

//   while (1) {
//     let myBlocks = []
//     let myCntR = 0

//     const visited = Array.from({ length: n }, () => Array(n).fill(false))

//     for (let i = 0; i < n; i++) {
//       for (let j = 0; j < n; j++) {
//         if (visited[i][j]) continue
//         if (board[i][j] < 1) continue

//         const [blocks, cntR] = bfs([i, j], board[i][j], visited)

//         if (myBlocks.length < blocks.length) {
//           myBlocks = blocks
//           myCntR = cntR
//           continue
//         }
//         if (myBlocks.length === blocks.length && myCntR <= cntR) {
//           myBlocks = blocks
//           myCntR = cntR
//         }
//       }
//     }

//     if (myBlocks.length < 2) break
//     result += Math.pow(myBlocks.length, 2)
//     myBlocks.forEach(([y, x]) => (board[y][x] = EMPTY))
//     drop(board)
//     board = turn(board)
//     drop(board)
//   }

//   //   while (1) {
//   //     let myBlocks = []
//   //     let myCntR = 0
//   //     const visited = Array.from({ length: N }, () => Array(N).fill(false))

//   //     for (let i = 0; i < N; i++) {
//   //       for (let j = 0; j < N; j++) {
//   //         if (visited[i][j]) continue
//   //         if (grid[i][j] < 1) continue
//   //         const [blocks, cntR] = bfs([i, j], grid[i][j], visited)
//   //         if (myBlocks.length < blocks.length) {
//   //           myBlocks = blocks
//   //           myCntR = cntR
//   //           continue
//   //         }
//   //         if (myBlocks.length === blocks.length && myCntR <= cntR) {
//   //           myBlocks = blocks
//   //           myCntR = cntR
//   //         }
//   //       }
//   //     }

//   //     if (myBlocks.length < 2) break
//   //     result += Math.pow(myBlocks.length, 2)
//   //     myBlocks.forEach(([y, x]) => (grid[y][x] = EMPTY))
//   //     drop(grid)
//   //     grid = turn(grid)
//   //     drop(grid)
//   //   }
// }

// // function solution([N, M], grid) {

// //   const bfs = (pos, block, v) => {
// //     v[pos[0]][pos[1]] = true
// //     const visited = JSON.parse(JSON.stringify(v))
// //     let queue = [pos]

// //     const result = []
// //     let cntR = 0

// //     while (queue.length > 0) {
// //       const size = queue.length
// //       const nextQueue = []
// //       for (let i = 0; i < size; i++) {
// //         const [y, x] = queue[i]
// //         result.push([y, x])
// //         for (const [dy, dx] of direction) {
// //           const ny = dy + y
// //           const nx = dx + x
// //           if (!check(ny, nx)) continue
// //           if (visited[ny][nx]) continue
// //           if (grid[ny][nx] === EMPTY) continue
// //           if (grid[ny][nx] === COLOR_B) continue
// //           visited[ny][nx] = true
// //           if (grid[ny][nx] === COLOR_R) {
// //             nextQueue.push([ny, nx])
// //             cntR++
// //             continue
// //           }
// //           if (grid[ny][nx] === block) {
// //             nextQueue.push([ny, nx])
// //             v[ny][nx] = true
// //           }
// //         }
// //       }
// //       queue = nextQueue
// //     }

// //     return [result, cntR]
// //   }

// //   return result
// // }
