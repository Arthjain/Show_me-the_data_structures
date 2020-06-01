This algorithm uses the linked list data structure to implement a Blockchain. Inside the 
linked list implementation, an append function was created to add elements to the list.

Time complexity: The overall time complexity is O(1). Since we keep track of the tail, it takes constant time to add a new block. The space complexity is O(n) depending on how many block input we want to chain up.

Space complexity: The space complexity is linear O(n) where n is the input size because 
the size of the block storage scales proportionally to the size of the input.
