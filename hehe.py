#python program that outlines all functionalities of python

# Printing
print("Hello, World!")

# Variables and data types
number = 10
floating_point = 3.14
string = "Python"
boolean = True

# Arithmetic operations
result = number + floating_point
print(result)

# Conditional statements
if result > 10:
    print("Greater than 10")
elif result == 10:
    print("Equal to 10")
else:
    print("Less than 10")

# Loops
for i in range(5):
    print(i)

while number > 0:
    print(number)
    number -= 1

# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list[0])

# Dictionaries
my_dict = {"name": "John", "age": 25}
print(my_dict["name"])

# Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# File handling
file = open("example.txt", "w")
file.write("Hello, Python!")
file.close()

# Error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# Modules and libraries
import math
print(math.sqrt(16))

# Classes and objects
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())


#---------------- Data Structures and Algos ------------------
# Data Structures

# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Dictionaries
my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# Arrays
import array
my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array)


# Strings
my_string = "Hello, World!"
print("String:", my_string)


# Library-Based Data Structures

# Stacks (using the 'deque' class from the 'collections' module)
from collections import deque

my_stack = deque()
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
print("Stack:", my_stack)

# Queues (using the 'deque' class from the 'collections' module)
my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
print("Queue:", my_queue)

# Heaps (using the 'heapq' module)
import heapq

my_heap = []
heapq.heappush(my_heap, 3)
heapq.heappush(my_heap, 1)
heapq.heappush(my_heap, 2)
print("Heap:", my_heap)

# Linked Lists (using the 'LinkedList' class from the 'linkedlist' module)
from linkedlist import LinkedList

my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print("Linked List:", my_linked_list)

# Trees (using the 'BinaryTree' class from the 'binarytree' module)
from binarytree import BinaryTree

my_tree = BinaryTree(1)
my_tree.left = BinaryTree(2)
my_tree.right = BinaryTree(3)
print("Tree:")
print(my_tree)

# Graphs (using the 'Graph' class from the 'networkx' library)
import networkx as nx

my_graph = nx.Graph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 3)
print("Graph:", my_graph.edges())

# These are just a few examples of data structures available in Python.
# Additional data structures can be found in various libraries and modules.
# Please note that some of the data structures mentioned here may require installation of third-party libraries.


# Algorithms

# Sorting
my_list = [5, 3, 1, 4, 2]
sorted_list = sorted(my_list)
print(sorted_list)

# Searching
target = 4
if target in my_list:
    print("Found")
else:
    print("Not found")

# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Graph traversal (BFS)
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

bfs(graph, 'A')

# Tree traversal (DFS)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

# Usage example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal(root)


# Basic Algorithms

# Linear Search
def linear_search(arr, target):
    """
    Linear search is a simple search algorithm that sequentially checks each element in an array
    until a match is found or the end of the array is reached.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [1, 2, 3, 4, 5]
target = 3
result = linear_search(my_list, target)
print("Linear Search:", result)

# Bubble Sort
def bubble_sort(arr):
    """
    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [5, 3, 1, 4, 2]
bubble_sort(my_list)
print("Bubble Sort:", my_list)


# Advanced Algorithms

# Binary Search (requires a sorted array)
def binary_search(arr, target):
    """
    Binary search is an efficient search algorithm used to find the position of a target value within a sorted array.
    It compares the target value with the middle element of the array and continues narrowing down the search
    by dividing the search range in half until the target value is found or the search range is empty.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

my_list = [1, 2, 3, 4, 5]
target = 3
result = binary_search(my_list, target)
print("Binary Search:", result)

# Quick Sort
def quick_sort(arr):
    """
    Quick sort is an efficient, comparison-based sorting algorithm.
    It uses a divide-and-conquer approach by selecting a pivot element,
    partitioning the array around the pivot, and recursively sorting the sub-arrays.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)

my_list = [5, 3, 1, 4, 2]
sorted_list = quick_sort(my_list)
print("Quick Sort:", sorted_list)


# This program provides explanations for the basic algorithms (linear search and bubble sort)
# and advanced algorithms (binary search and quick sort). Understanding these algorithms
# helps in choosing the appropriate approach for solving specific programming problems.
# Python offers many more algorithms, and you can explore them based on your needs and interests.





