# Minimize Product
Here is the [question](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/minimize-product-265ce7a0/)

minimize_product_segment_tree.py: 
1) This gave me a score of 20. 
2) Segment Trees are not the best approach as it has a lot of memory requirements plus I am also being quite generous in using up memory.
3) Next approach try fenwick trees.


## Knowledge on Fenwick Tree

1. If we update the fenwick tree at index i 
   
   ```python
   _update(tree, i, val):
     i = i + 1
     while i < len(tree):
         tree[i] += val
         i += ( i & (-i)) # -i in two's compliment anding with i gives the right most bit that is set
         # Go down

   ```
1. If we want to query the fenwick tree
   ```python
   _query(tree, i):
       i = i + 1
       ans = 0
       while i > 0: # 0 is never used 
           ans += tree[i]
           i -= (i & (-i)) # Go Up as child has already updated parent
        return ans
   ```
   If you see, the queries can be from [0, i] only. Now [l, r] types of queries are not supported so we cannot use fenwick tree

1. Optimize the previous code in that case