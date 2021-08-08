
from typing import Type
from copy import deepcopy
mod = 10**9 + 7
class TreeNode:
    def __init__(self, 
            minimum:int, 
            count_minimum:int, 
            minimum_prod:int,
            minimum_prod_count:int, 
            left: 'TreeNode', 
            right: 'TreeNode'
            ):
        self.minimum = minimum
        self.count_minimum = count_minimum
        self.minimum_prod = minimum_prod
        self.minimum_prod_count = minimum_prod_count
        self.left = left
        self.right = right

def left_right_setup(left: 'TreeNode', right: 'TreeNode', mod = mod):

    """
    TODO: Naming convention is a bit poor in this function. Correct That
    """
    if not left:
        return deepcopy(right)
    if not right:
        return deepcopy(left)


    min_left, min_right = left.minimum, right.minimum
    """
    Setting up the product part first and it's count
    """
    ans_count = left.count_minimum * right.count_minimum
    ans_prod = min_left * min_right
    
    if left.minimum_prod:
        if ans_prod > left.minimum_prod:
            ans_count = left.minimum_prod_count
            ans_prod = left.minimum_prod
        elif ans_prod == left.minimum_prod:
            ans_count = (ans_count + left.minimum_prod_count) % mod

    
    if right.minimum_prod:
        if ans_prod > right.minimum_prod:
            ans_count = right.minimum_prod_count
            ans_prod = right.minimum_prod
        elif ans_prod == right.minimum_prod:
            ans_count = (ans_count + right.minimum_prod_count) % mod

    """
    Setting up this nodes minima and it's count
    """
    if min_left < min_right:
        minima, minima_count = min_left, left.count_minimum
    elif min_right < min_left:
        minima, minima_count = min_right, right.count_minimum
    else:
        minima, minima_count = min_left, (left.count_minimum + right.count_minimum) % mod
    
    return TreeNode(minima, minima_count, ans_prod, ans_count, left, right)


def is_overlap(s1:int, 
               e1:int, 
               s2:int, 
               e2:int) -> bool:
    arr = sorted([(s1, e1), (s2, e2)])
    [(s1, e1), (s2, e2)] = arr    
    if s2 <= e1:
        return True
    return False

def find_query(l_index:int, r_index:int, cur_l:int, cur_r:int, node: 'TreeNode') -> 'TreeNode':
    if cur_l <= l_index <= r_index <= cur_r:
        """
        Complete Overlap
        """
        return node
    
    mid = (l_index + r_index)//2
    if is_overlap(l_index, mid, cur_l, cur_r):
        left = find_query(l_index, mid, cur_l, cur_r, node.left)
    else:
        left = None

    if is_overlap(mid + 1, r_index, cur_l, cur_r):
        right = find_query(mid + 1, r_index, cur_l, cur_r, node.right)
    else:
        right = None

    return left_right_setup(left, right)


        
def create_tree(l_index, r_index, arr):
    if l_index == r_index:
        return TreeNode(arr[l_index], 1, None, 0, None, None)
    mid = (l_index + r_index)//2
    left = create_tree(l_index, mid, arr)
    right = create_tree(mid + 1, r_index, arr)

    return left_right_setup(left, right)


def update_tree(l_index, r_index, index, value, node:'TreeNode'):
    if l_index == r_index:
        return TreeNode(value, 1, None, 0, None, None)
    mid = (l_index + r_index) // 2
    left, right = node.left, node.right
    if l_index <= index <= mid:
        left = update_tree(l_index, mid, index, value, node.left)
    else:
        right = update_tree(mid+1, r_index, index, value, node.right)
    
    return left_right_setup(left, right)


def one_epoch() -> int:
    N, Q = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    tree = create_tree(0, len(arr) - 1, arr)
    ans = 0
    for _ in range(Q):
        type_query, p1, p2 = map(int, input().split(" "))
        if type_query == 2:
            res = find_query(0, len(arr) - 1, p1 - 1, p2 - 1, tree)
            ans = (ans + res.minimum_prod_count) % mod
        elif type_query == 1:
            tree = update_tree(0, len(arr) - 1, p1- 1, p2, tree)
            
    return ans

    


def main():
    t = int(input())
    ans = []
    for _ in range(t):
        ans.append(one_epoch())
    for x in ans:
        print(ans)

if __name__ == "__main__":
    main()
