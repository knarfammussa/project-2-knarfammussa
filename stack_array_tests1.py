import unittest
from stack_array1 import Stack


class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None] * 5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_push(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.num_items, 2)
        self.assertEqual(stack.capacity, 5)
        stack.push(6)
        self.assertEqual(stack, Stack(5, [1, 2, 6]))
        stack.push(1)
        self.assertEqual(stack, Stack(5, [1, 2, 6, 1]))
        stack.push(5)
        self.assertEqual(stack, Stack(5, [1, 2, 6, 1, 5]))
        with self.assertRaises(IndexError):
            stack.push(6)

    def test_pop(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.pop(), 2)
        stack1 = Stack(5, [1, 2])
        stack1.pop()
        self.assertEqual(stack1, Stack(5, [1]))
        self.assertEqual(stack1.num_items, 1)
        stack2 = Stack(5, [])
        with self.assertRaises(IndexError):
            stack2.pop()

    def test_peek(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.peek(), 2)
        stack1 = Stack(5, [5, -23, -6])
        self.assertEqual(stack1.peek(), -6)
        stack2 = Stack(5, [])
        with self.assertRaises(IndexError):
            stack2.peek()

    def test_size(self) -> None:
        stack1 = Stack(5, [1, 2])
        self.assertEqual(stack1.size(), 2)
        stack1.pop()
        self.assertEqual(stack1.size(), 1)


# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc..

if __name__ == '__main__':
    unittest.main()
