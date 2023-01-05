const strStr = (haystack, needle) => {
    // Checking to prevent unecessary verification
    if (needle === '') return 0;
    if (haystack.length < needle.length) return -1;
    
    // Do the checking
    for (let i = 0; i < haystack.length - needle.length + 1; i+= 1) {
        // In case the character matches with the first in the needle
        if (haystack.charAt(i) === needle.charAt(0)) {
            // Check all the other characters
            let matches = true;
            for (let j = 1; j < needle.length; j++) {
                if (haystack.charAt(i + j) !== needle.charAt(j)) matches = false;
            }
            // Matches
            if (matches) return i;
        }
    }
    
    // Did not find
    return -1;
};