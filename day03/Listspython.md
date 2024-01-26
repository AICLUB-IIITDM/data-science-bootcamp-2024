# Lists in Python

## (a) Lists
Lists are used to store multiple items in a single variable. List literals are written within square brackets `[ ]`. Lists work similarly to strings -- use the `len()` function and square brackets `[ ]` to access data, with the first element at index 0. List items can be of any data type.

### Example: Create a list
```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0])
print(len(thislist))
```
List items are **ordered, changeable, and allow duplicate values**.
- **Ordered:** When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.
- **Changeable:** The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
- **Allow Duplicates:** Since lists are indexed, lists can have items with the same value.
### Example:
```python
thislist = ["apple", "banana", "cherry", "apple", "banana"]
print(thislist)
```
Assignment with an `=` on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.
```python
b = thislist   ## Does not copy the list
```
The "empty list" is just an empty pair of brackets [ ]. The '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4] (this is just like + with strings).
**(b). FOR AND IN :** The `for` construct -- `for var in list` -- is an easy way to look at each element in a list (or other collection).
**Example:**
```python
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
    print(sum)  ## 30
```
The `in` construct on its own is an easy way to test if an element appears in a list (or other collection) -- `value in collection` -- tests if the value is in the collection, returning True/False.
**Example:**
```python
list = ['apple', 'grapes', 'banana']
if 'grapes' in list:
    print('present') ## present
```
**(c). RANGE:** The `range(n)` function yields the numbers 0, 1, ..., n-1, and `range(a, b)` returns a, a+1, ..., b-1 --> up to but not including the last number.

**Example:**
```python
## print the numbers from 0 through 99
for i in range(100):
    print(i)
```
**(d). WHILE LOOP:** The above `for/in` loops solve the common case of iterating over every element in a list, but the `while` loop gives you total control over the index numbers.

**Example:**
```python
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
```
**(e). LIST METHODS:** Here are a few common list methods:
1. `list.append(elem)` -- adds a single element to the end of the list.
2. `list.insert(index, elem)` -- inserts the element at the given index, shifting elements to the right.
3. `list.extend(list2)` -- adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
4. `list.index(elem)` -- searches for the given element from the start of the list and returns its index.
5. `list.remove(elem)` -- searches for the first instance of the given element and removes it.
6. `list.sort()` -- sorts the list in place (does not return it).
7. `list.reverse()` -- reverses the list in place (does not return it).
8. `list.pop(index)` -- removes and returns the element at the given index.

**Example:**
```python
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add a list of elems at the end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))    ## 2
list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
```
**(f). LIST SLICES:** Slices work on lists just as with strings and can also be used to change sub-parts of the list.

**Example:**
```python
list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']
```