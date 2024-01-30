import question
import numpy as np

create_test = [[1, 2, 3],
               [1, 2],
               [2, 3, 7]]
convert_test = [[1, 2, 3, 4],
                [1, 2, 3, 4, 5, 6, 7, 8],
                [1, 2, 3, 4, 5, 6]]
common_test_a = [[1, 2, 3, 4, 5],
                 [1, 2, 3],
                 [1, 2, 2, 3, 4]]
common_test_b = [[3, 4, 5, 6, 7],
                 [4, 5, 6],
                 [2, 3, 3, 4, 5]]
match_test_a = [[1,2,3,2,3,4,3,4,5,6],
                [1, 2, 3]]
match_test_b = [[7,2,10,2,7,4,9,4,9,8],
                [0,2,3]]
range_test_a = [[2, 6, 1, 9, 10, 3, 27],
                [1,2,3,2,3,4,3,4,5,5,6]]
swap_test_a1 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
swap_test_a2 = [[1, 3, 2],
                [4, 6, 5],
                [7, 9, 8]]
def test_create():
    arr = np.array([1,4, 5])
    for list in create_test:
        assert type(question.create(list)) == type(arr)
def test_convert():
    for list in convert_test:
        assert question.convert(list).ndim == 2   
def test_common():
    # Test case 1: Common items between common_test_a[0] and common_test_b[0]
    expected_output = np.array([3, 4, 5])
    assert np.array_equal(question.common(common_test_a[0], common_test_b[0]), expected_output)

    # Test case 2: Common items between common_test_a[1] and common_test_b[1]
    expected_output = np.array([])
    assert np.array_equal(question.common(common_test_a[1], common_test_b[1]), expected_output)

    # Test case 3: Common items between common_test_a[2] and common_test_b[2]
    expected_output = np.array([2, 3, 4])
    assert np.array_equal(question.common(common_test_a[2], common_test_b[2]), expected_output)
def test_match():
    # Test case 1: Matching indices between common_test_a[0] and common_test_b[0]
    expected_output = np.array([1, 3, 5, 7])
    assert np.all(question.match(match_test_a[0], match_test_b[0]) == expected_output)

    # Test case 2: Matching indices between common_test_a[1] and common_test_b[1]
    expected_output = np.array([1,2])
    assert np.all(question.match(match_test_a[1], match_test_b[1]) == expected_output)
def test_range():
    # Test case 1: Range of elements between 5 and 10 in range_test_a[0]
    expected_output = np.array([6, 9, 10])
    assert np.all(question.range(range_test_a[0]) == expected_output)

    # Test case 2: Range of elements between 5 and 10 in range_test_a[1]
    expected_output = np.array([5,6])
    assert np.all(question.range(range_test_a[1]) == expected_output)
def test_swap():
    # Test case 1: Swap elements in a 3x3 array
    input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [[2, 1, 3], [5, 4, 6], [8, 7, 9]]
    assert np.all(question.swap(input_array) == expected_output)

    # Test case 2: Swap elements in a 2x2 array
    input_array = [[11, 12], [13, 14]]
    expected_output = [[12, 11], [14, 13]]
    assert np.all(question.swap(input_array) == expected_output)

    # Test case 3: Swap elements in a 1x4 array
    input_array = [[1, 2, 3, 4]]
    expected_output = [[2, 1, 3, 4]]
    assert np.all(question.swap(input_array) == expected_output)
def test_reverse():
    # Test case 1: Reverse a 3x3 array
    input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    assert np.array_equal(question.reverse(input_array), expected_output)

    # Test case 2: Reverse a 2x2 array
    input_array = [[11, 12], [13, 14]]
    expected_output = [[13, 14], [11, 12]]
    assert np.array_equal(question.reverse(input_array), expected_output)

    # Test case 3: Reverse a 1x4 array
    input_array = [[1, 2, 3, 4]]
    expected_output = [[1, 2, 3, 4]]
    assert np.array_equal(question.reverse(input_array), expected_output)
def test_replace():
    # Test case 1: Replace odd numbers in a 3x3 array
    input_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [[-1, 2, -1], [4, -1, 6], [-1, 8, -1]]
    assert np.array_equal(question.replace(input_array), expected_output)

    # Test case 2: Replace odd numbers in a 2x2 array
    input_array = [[11, 12], [13, 14]]
    expected_output = [[-1, 12], [-1, 14]]
    assert np.array_equal(question.replace(input_array), expected_output)

    # Test case 3: Replace odd numbers in a 1x4 array
    input_array = [[1, 2, 3, 4]]
    expected_output = [[-1, 2, -1, 4]]
    assert np.array_equal(question.replace(input_array), expected_output)
def test_extract():
    # Test case 1: Extract odd elements from a 1D array
    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output = [1, 3, 5, 7, 9]
    assert np.array_equal(question.extract(input_array), expected_output)

    # Test case 2: Extract odd elements from a 1D array with negative numbers
    input_array = [-3, -2, -1, 0, 1, 2, 3]
    expected_output = [-3, -1, 1, 3]
    assert np.array_equal(question.extract(input_array), expected_output)

    # Test case 3: Extract odd elements from a 1D array with all even numbers
    input_array = [2, 4, 6, 8, 10]
    expected_output = []
    assert np.array_equal(question.extract(input_array), expected_output)

def test_remove():
    # Test case 1: Remove elements from array a that are in array b
    input_array_a = [1, 2, 3, 4, 5]
    input_array_b = [3, 4, 5, 6, 7]
    expected_output = [1, 2]
    assert np.array_equal(question.remove(input_array_a, input_array_b), expected_output)

    # Test case 2: Remove elements from array a that are in array b
    input_array_a = [10, 20, 30, 40, 50]
    input_array_b = [30, 40, 50, 60, 70]
    expected_output = [10, 20]
    assert np.array_equal(question.remove(input_array_a, input_array_b), expected_output)

    # Test case 3: Remove elements from array a that are in array b
    input_array_a = [5, 10, 15, 20, 25]
    input_array_b = [15, 20, 25, 30, 35]
    expected_output = [5, 10]
    assert np.array_equal(question.remove(input_array_a, input_array_b), expected_output)    