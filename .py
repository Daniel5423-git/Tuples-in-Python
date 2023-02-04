# Tuples-in-Python


Tuples
In Python, there are different data types: string, integer and float. These data types can all be contained in a tuple as follows:

Image
Now, let us create your first tuple with string, integer and float.

# Create your first tuple
​
tuple1 = ("disco",10,1.2 )
tuple1
('disco', 10, 1.2)
The type of variable is a tuple.

# Print the type of the tuple you created
​
type(tuple1)
tuple
Indexing
Each element of a tuple can be accessed via an index. The following table represents the relationship between the index and the items in the tuple. Each element can be obtained by the name of the tuple followed by a square bracket with the index number:

Image
We can print out each value in the tuple:

# Print the variable on each index
​
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
disco
10
1.2
We can print out the type of each value in the tuple:

# Print the type of value on each index
​
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
<class 'str'>
<class 'int'>
<class 'float'>
We can also use negative indexing. We use the same table above with corresponding negative values:

Image
We can obtain the last element as follows (this time we will not use the print statement to display the values):

1
# Use negative index to get the value of the last element
​
tuple1[-1]
1.2
We can display the next two elements as follows:

# Use negative index to get the value of the second last element
​
tuple1[-2]
10
# Use negative index to get the value of the third last element
​
tuple1[-3]
'disco'
Concatenate Tuples
We can concatenate or combine tuples by using the + sign:

# Concatenate two tuples
​
tuple2 = tuple1 + ("hard rock", 10)
tuple2
('disco', 10, 1.2, 'hard rock', 10)
We can slice tuples obtaining multiple values as demonstrated by the figure below:

Image
Slicing
We can slice tuples, obtaining new tuples with the corresponding elements:

# Slice from index 0 to index 2
​
tuple2[0:3]
('disco', 10, 1.2)
We can obtain the last two elements of the tuple:

# Slice from index 3 to index 4
​
tuple2[3:5]
('hard rock', 10)
We can obtain the length of a tuple using the length command:

# Get the length of tuple
​
len(tuple2)
5
This figure shows the number of elements:

Image
Sorting
Consider the following tuple:

# A sample tuple
​
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
We can sort the values in a tuple and save it to a new tuple:

# Sort the tuple
​
RatingsSorted = sorted(Ratings)
RatingsSorted
[0, 2, 5, 6, 6, 8, 9, 9, 10]
Nested Tuple
A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. Consider the following tuple with several elements:

# Create a nest tuple
​
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
Each element in the tuple including other tuples can be obtained via an index as shown in the figure:

Image
# Print element on each index
​
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])
Element 0 of Tuple:  1
Element 1 of Tuple:  2
Element 2 of Tuple:  ('pop', 'rock')
Element 3 of Tuple:  (3, 4)
Element 4 of Tuple:  ('disco', (1, 2))
We can use the second index to access other tuples as demonstrated in the figure:

Image
We can access the nested tuples :

# Print element on each index, including nest indexes
​
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])
Element 2, 0 of Tuple:  pop
Element 2, 1 of Tuple:  rock
Element 3, 0 of Tuple:  3
Element 3, 1 of Tuple:  4
Element 4, 0 of Tuple:  disco
Element 4, 1 of Tuple:  (1, 2)
We can access strings in the second nested tuples using a third index:

# Print the first element in the second nested tuples
​
NestedT[2][1][0]
'r'
# Print the second element in the second nested tuples
​
NestedT[2][1][1]
'o'
We can use a tree to visualise the process. Each new index corresponds to a deeper level in the tree:

Image
Similarly, we can access elements nested deeper in the tree with a fourth index:

# Print the first element in the second nested tuples
​
NestedT[4][1][0]
1
# Print the second element in the second nested tuples
​
NestedT[4][1][1]
2
The following figure shows the relationship of the tree and the element NestedT[4][1][1]:

Image
Quiz on Tuples
Consider the following tuple:

# sample tuple
​
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple
('pop',
 'rock',
 'soul',
 'hard rock',
 'soft rock',
 'R&B',
 'progressive rock',
 'disco')
Find the length of the tuple, genres_tuple:

# Write your code below and press Shift+Enter to execute
len(genres_tuple)
8
Image
Double-click __here__ for the solution.
​
<!-- Your answer is below:
len(genres_tuple)
-->
Access the element, with respect to index 3:

[3]
# Write your code below and press Shift+Enter to execute
genres_tuple[3]
'hard rock'
Double-click __here__ for the solution.
​
<!-- Your answer is below:
genres_tuple[3]
-->
Use slicing to obtain indexes 3, 4 and 5:

:6]
# Write your code below and press Shift+Enter to execute
genres_tuple[3:6]
('hard rock', 'soft rock', 'R&B')
Double-click __here__ for the solution.
​
<!-- Your answer is below:
genres_tuple[3:6]
-->
Find the first two elements of the tuple genres_tuple:

0
# Write your code below and press Shift+Enter to execute
genres_tuple[0:2]
('pop', 'rock')
Double-click __here__ for the solution.
​
<!-- Your answer is below:
genres_tuple[0:2]
-->
Find the first index of "disco":

')
# Write your code below and press Shift+Enter to execute
genres_tuple.index('disco')
7
Double-click __here__ for the solution.
​
<!-- Your answer is below:
genres_tuple.index("disco")
-->
Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):

s
# Write your code below and press Shift+Enter to execute
C_tuple = ( -5, 1, -3)
sorted(C_tuple)
[-5, -3, 1]
Double-click __here__ for the solution.
​
<!-- Your answer is below:
C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
C_list
-->
