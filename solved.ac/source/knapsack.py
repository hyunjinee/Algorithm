"""
the fractional kanpsack problem
- concerns a thief breaking into a jewelery store carrying a knapsack
- in this case, the thief does not have to steal all of an item, buy rather can take any fraction of the item.
- we can think of the items as being bags of gold or silver dust.

the 0-1 knapsack problem
- in this case ,the thief can not take some fraction of the item
- we can think of the items as being gold or silver ingots.
suppose there are n items, and let
- S = {item, item2, item3, ...}
- w = weight of itemi
- pi = profit of item
- W = maximum weight the knapsack can hold,
- where wi, pi and w are postive integers

our greedy strategy is to choose the items with the largest profit per unit weight first.
that is order the items in nonincreasing order by the profilt/unit weigth, and select them in sequence.
an item is put in the knapsack 
if its weight does not bring the total weight above w.
note that this strategy can waste some capacities of an item.
therefore, greedy algorithm does not solve the 0-1 kanpsack problem.

"""