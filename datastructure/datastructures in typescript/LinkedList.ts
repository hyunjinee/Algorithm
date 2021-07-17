import LinkedListNode from "./LinkedListNode";

interface List<T> {
    head: LinkedListNode<T>
    tail: LinkedListNode<T>
    size: number
}

class LinkedList<T> implements Iterable<T> {
    private list: List<T> | undefined

    constructor() {
        this.list = undefined
    }

    size(): number {
        if  (this.list) return this.list.size
        return 0
    }

    isEmpty(): boolean {
        return !this.list
    }

    addFront(val: T) : void {
        const newNode = new LinkedListNode(val)
        if (this.list) {
            this.list.head.prev = newNode
            newNode.next = this.list.head
            this.list.size += 1

        }else {
            this.list = {
                head: newNode,
                tail: newNode,
                size: 1
            }
        }
    }

    addBack(val: T) : void {
        const newNode = new LinkedListNode(val)
        
    }
}