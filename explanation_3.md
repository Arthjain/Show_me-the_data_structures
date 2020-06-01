In this implementation of Huffman coding, i have used heapq and Counter 
    Dictionary. Counter easily gives us keys as the strings and values with their 
    frequency in the data. Heapq is efficient as i need to insert the new node formed 
    everytime when the two with least nodes are combined and sort it again. Encoding function() we use a while loop inside of which we 
    call heappop. This makes its complexity O(nlogn) where n is the number of
    elements. 
    In decoding function, the complexity is O(k) where k is the number of items 
    in the dictionary.
