

'''
     o
    / 
find_unique_tree(n-1)

     o
      \
  find_unique_tree(n-1)

      o
     / \
    o  find_unique_tree(n-2)

                       o
                      / \
 find_unique_tree(n-2)   o

'''




def find_unique_tree(n):
	if n == 0:
		return []
	elif n == 1:
		return ['1']
	else:
		all_unique_trees = []

		tree_minus_one_set = find_unique_tree(n-1)
		for subtree in tree_minus_one_set:
			all_unique_trees += ['L(' + subtree + ')*']
			all_unique_trees += ['*L(' + subtree + ')']

		tree_minus_two_set = find_unique_tree(n-2)
		for subtree in tree_minus_two_set:
			all_unique_trees += ['**L(' + subtree + ')']
			all_unique_trees += ['L(' + subtree + ')**']

		return all_unique_trees

print find_unique_tree(0)
print find_unique_tree(1)
print find_unique_tree(2)
print find_unique_tree(3)




