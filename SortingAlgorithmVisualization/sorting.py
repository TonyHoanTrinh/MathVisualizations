# We import about libraries

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Our helper function that swaps elements i and j from our list A
def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]

def heapify(A, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and A[i] < A[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and A[largest] < A[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # swap

        # Heapify the root.
        heapify(A, n, largest)

        # The main function to sort an array of given size


def heapsort(A):
    n = len(A)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(A, n, i)
        yield A

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap
        heapify(A, i, 0)
        yield A


# Our Bubble Sort algorithm
def bubblesort(A):

    # Returns back if there is only 1 element in the list
    if len(A) == 1:
        return

    # We initially set our variable swapped as True at the beginning which just checks if swapping did occur or not
    swapped = True
    # We iterate based on the length of the list
    for i in range(len(A) - 1):
        # We break out of our loop if our swapped variable is false and then set it to false immediately after
        if not swapped:
            break
        swapped = False
        # We iterate based on how far we are iterating through the list itself
        for j in range(len(A) - 1 - i):
            # If the value of the current element is less than the element ahead we swapped the values and set swapped as True
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            # We return back the list A to be iterated again
            yield A

# Our Insertion Sort algorithm
def insertionsort(A):

    # We iterate based on the length of the list
    for i in range(1, len(A)):
        # We set a variable to hold our current position in the list
        j = i
        # We loop through based on whether if we are the elements ahead are less than the current element (the area is unsorted)
        while j > 0 and A[j] < A[j - 1]:
            # We swap the elements positions as they are unsorted and we decrement our value of j
            swap(A, j, j - 1)
            j -= 1
            # We return back the list A to be iterated again
            yield A

# Our Merge Sort algorithm
def mergesort(A, start, end):

    # If our end pivot is less than our starting pivot then we know its already sorted so we return it back
    if end <= start:
        return

    # We calculate our mids based on our end and start pivots
    mid = start + ((end - start + 1) // 2) - 1
    # We return back based on calling these functions
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A


# Helper function used with Merge Sort
def merge(A, start, mid, end):

    # We set out left and right pivots with our empty array
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    # We iterate based on if the left pivot is less than our middle pivot and our right pivot is less than our end pivot
    while leftIdx <= mid and rightIdx <= end:
        # If our elements are in the incorrect place then we increment index and append to the merged list accordingly
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    # We iterate based on if our left pivot is less than our mid then we increment and append to the merged list
    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    # We iterate based on if our right pivot is less thna our end then we increment and append to the merged list
    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    # We iterate through our merged list and return back the list A
    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A


# Our quick sort algorithm
def quicksort(A, start, end):

    # If our start pivot is greater than our end pivot then we know its already sorted so we return it back
    if start >= end:
        return

    # We set out start and end pivots based on the list
    pivot = A[end]
    pivotIdx = start

    # We iterate through the list and swapping when the element is greater than the current element
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    # We recursively call the function again for our sub arrays
    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)

# Our Selection Sort algorithm
def selectionsort(A):

    # If our list is of length 1, then its already sorted so we return back
    if len(A) == 1:
        return

    # We iterate based on the length of the list
    for i in range(len(A)):
        # We find our minimum unsorted value and set it to some variables
        minVal = A[i]
        minIdx = i
        # Sub loop to iterate if our minimum value is greater than or less than our current position element
        for j in range(i, len(A)):
            # We change our minimum value if we do find an element that is less than our current minimum value
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A


if __name__ == "__main__":

    # We ask the user for the amount of elements of integers that we will sort and which algorithm they wish to use
    N = int(input("Enter number of integers: "))
    method_msg = "Which Sorting Algorithm would you like to use?:\nBubble Sort\nInsertion Sort\nMerge Sort\
        \nQuick Sort\nHeap Sort\nSelection Sort\n"
    method = input(method_msg)

    # We get a list of random integers based on how many elements they wish to sort and then randomly shuffle the list
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    # Based on the user's selection we will sort the list based on that method and feed into the matplotlib FuncAnimation method
    if method == "Bubble Sort":
        title = "Bubble sort"
        generator = bubblesort(A)
    elif method == "Insertion Sort":
        title = "Insertion sort"
        generator = insertionsort(A)
    elif method == "Merge Sort":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    elif method == "Quick Sort":
        title = "Quick Sort"
        generator = quicksort(A, 0, N - 1)
    elif method == "Heap Sort":
        title = "Heap Sort"
        generator = heapsort(A)
    else:
        title = "Selection sort"
        generator = selectionsort(A)

    # We set our graph with it's axises
    fig, ax = plt.subplots()
    ax.set_title(title)

    # We create our barplot of rectangles which we store as bar_rects
    bar_rects = ax.bar(range(len(A)), A, align="edge", color = "black")

    # We set limits to our axises
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    # Text label at the top to showcase how many operations have been completed
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Iterations is our variable which holds how many operations have been performed and is fed into the FuncAnimation method
    iteration = [0]


    # We update our graph for each operation
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))


    # We call in our FuncAnimation to see the sorting as it occurs
    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=generator, interval=1,
                                   repeat=False)
    # Lastly we show our graph
    plt.show()
