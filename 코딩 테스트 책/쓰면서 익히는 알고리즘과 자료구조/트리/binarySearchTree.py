from collections import deque


class BinarySearchTree:
    def find(self, data):
        return self._find_data(self.__root, data)



    def _find_data(self, node , data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif node.data > data:
            return self._find_data(node.left, data)
        else:
            return self._find_data(node.right, data)

        

    def inorder_iter(self):
        result = []
        stack = []

        node= self.__root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            if stack:
                node = stack.pop()
                result.append(node)
                node = node.right

        return result

    def find_min_node(self,node):
        while node.left:
            node = node.left
        return node


    def breadth_first_search(self):
        queue = deque()
        res = []

        queue.append(self.__root)

        while len(queue) != 0:
            qsize = len(queue)

            for _ in range(qsize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.data)

                

    def delete(self, data):
        self._delete_data(self.__root, data)

    def _delete_data(self, node, data):
        parent = None

        curr = node

        while curr and curr.data != data:
            parent = curr
            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

            if  curr is None:
                return node
            
            if curr.left is None and curr.right is None:
                if curr != node:
                    if parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    node = None

            elif curr.left and curr.right:
                min_node = self.find_min_node(curr.right)


                min_data = min_node.data

                self._delete_data(node, min_data)
                curr.data = min_data



            else:
                if curr.left:
                    child = curr.left
                else:
                    chile = curr.right

                if curr != node:
                    if curr == parent.left:
                        parent.left = child
                    else:
                        parent.right = child

                        