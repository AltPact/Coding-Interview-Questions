struct ListNode {
    val: i32,
    next: Option<Box<ListNode>>,
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

fn reverse_linked_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut prev = None;
    let mut current = head;
    while let Some(mut boxed_node) = current.take() {
        let next_node = boxed_node.next.take();
        boxed_node.next = prev.take();
        prev = Some(boxed_node);
        current = next_node;
    }
    prev
}