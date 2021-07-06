const nums: number[]  = [];

// write and update - O(1)

nums[0] = 1;
nums[1] = 2;
nums[2] = 3;

nums.push(4);
nums.push(5);

// O(n)
nums.unshift(0);
nums.unshift(-1);

// DELETE - O(n)

nums.splice(2, 1);


console.log(nums);