# Reverse Polish Notation (RPN)
def eval_rpn(self, tokens):
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            stack.append(stack.pop() - stack.pop())
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            stack.append(int(stack.pop() / stack.pop()))  # Use int for truncating division
        else:
            stack.append(int(token))

    return stack.pop()


# Valid Parentheses
def is_valid(self, s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in matching_brackets.values():
            stack.append(c)
        elif c in matching_brackets.keys():
            if not stack or stack.pop() != matching_brackets[c]:
                return False
        else:
            return False

    return not stack


# Largest Rectangle in Histogram
def largest_rectangle_area(self, heights):
    if not heights:
        return 0

    stack = []
    max_area = 0
    heights.append(0)  # Add 0 at the end to ensure we empty the stack at the end

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


# Implement Queue using Two Stacks
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Push element to the back of the queue
    def push(self, x):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    # Removes the element from in front of queue and returns that element
    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()

    # Get the front element
    def peek(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2[-1]

    # Returns whether the queue is empty
    def empty(self):
        return not self.stack1 and not self.stack2
