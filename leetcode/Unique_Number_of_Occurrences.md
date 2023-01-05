# 1207. Unique Number of Occurrences

![1207](https://user-images.githubusercontent.com/63354527/107896385-746da200-6f79-11eb-82c5-802c7c681a56.PNG)

## 풀이 1

```javascript
var uniqueOccurrences = function (arr) {
  let count = {};

  for (let i = 0; i < arr.length; i++) {
    if (!count[arr[i]]) {
      count[arr[i]] = 1;
    } else {
      count[arr[i]]++;
    }
  }
  let temp = [];
  for (let k in count) {
    if (temp.includes(count[k])) return false;
    temp.push(count[k]);
  }
  return true;
};
```

## 풀이 2

```javascript
var uniqueOccurrences = function (arr) {
  // Let's make a map to keep track of how many times each number occurs in our array
  let myMap = new Map();

  //For every number in our array using the for-of loop
  for (let num of arr) {
    //If we have the key already, we know the value is a number, so increment it by one
    if (myMap.has(num)) {
      myMap.set(num, myMap.get(num) + 1);
    } else {
      //If we dont have the key in our map...
      myMap.set(num, 1);
    }
  }
  //Make a new set and add the value of each key. If at any point we already saw the value we know the occurrences are NOT unique
  let mySet = new Set();
  //Grab the key and value of each myMap entry
  for (const val of myMap.values()) {
    //If the set already has it, return false
    if (mySet.has(val)) return false;
    //Otherwise add it
    mySet.add(val);
  }
  //If we got though the code above, return true, since the occurrences are all unique
  return true;
};
```
