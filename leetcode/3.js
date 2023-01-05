function lengthOfLongestSubstring(s) {
    const map = {};
    var left = 0;
    
    return s.split('').reduce((max, v, i) => {
        console.log(max, v, i)
        console.log(map[v])
        left = map[v] >= left ? map[v] + 1 : left;
        console.log(left, "left값")
        map[v] = i;
        
        return Math.max(max, i - left + 1);
    }, 0);
}


lengthOfLongestSubstring('abcabcbb')