class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        for _ in range(len(self.stack1)):
            temp = self.stack1.pop()
            self.stack2.append(temp)
        self.stack1.append(x)

        for _ in range(len(self.stack2)):
            temp = self.stack2.pop()
            self.stack1.append(temp)
        
        return
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) == 0:
            print('Queue empty')
        else:
            return self.stack1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) == 0:
            print('Queue empty')
        else:
            return self.stack1[len(self.stack1) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()