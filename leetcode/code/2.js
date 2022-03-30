var addTwoNumbers = function(l1, l2) {
    let res = new ListNode(-1),
        dummy = res,
        sum = 0, carry = 0;
    
    while(l1 || l2 || sum > 0) {
        if(l1) {
            sum += l1.val;
            l1 = l1.next;
        }
        
        if(l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        
        if(sum >= 10) {
            sum -= 10;
            carry = 1;
        }
        
        dummy.next = new ListNode(sum);
        dummy = dummy.next;
        sum = carry;
        carry = 0;
    }
    return res.next;
};