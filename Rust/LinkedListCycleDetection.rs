struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

fn has_cycle(head: Option<Box<ListNode>>) -> bool {
    let mut slow = head.as_ref();
    let mut fast = head.as_ref();

    while let (Some(node1), Some(node2)) = (slow, fast) {
        slow = node1.next.as_ref();
        fast = node2.next.as_ref().and_then(|x| x.next.as_ref());
        if slow == fast {
            return true;
        }
    }

    false
}
