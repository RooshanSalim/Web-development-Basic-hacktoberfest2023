import heapq


def heap_sort(array):
  """Sorts an array using the heap sort algorithm.

  Args:
    array: An array to be sorted.

  Returns:
    A sorted array.
  """

  # Convert the array to a max heap.
  heapq.heapify(array)

  # Repeatedly extract the largest element from the heap and append it to the
  # sorted array.
  sorted_array = []
  while array:
    sorted_array.append(heapq.heappop(array))

  return sorted_array


# Example usage:

array = [5, 3, 2, 1, 4]

sorted_array = heap_sort(array)

print(sorted_array)
