// var sortList = function (head) {
//   let temp = head
//   let arr = []
//   let i = 0
//   while (temp) {
//     arr.push(temp.val)
//     temp = temp.next
//   }
//   arr.sort((a, b) => a - b)
//   temp = head
//   while (temp) {
//     temp.val = arr[i++]
//     temp = temp.next
//   }
//   return head
// }

// var sortList = function(head) {
//     const result =[];

//     while(head){
//         result.push(head.val);
//         head = head.next;
//     }

//     result.sort((a,b)=> a-b)
//     return helper(result)

// };

// // function helper(array){
// //     return array.reduceRight((next,val)=> ({val,next}),null)
// // }
