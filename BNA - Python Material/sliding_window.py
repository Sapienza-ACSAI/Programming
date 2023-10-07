'''Simply put, the concept of a sliding window is:'''
# pick some oil, 
# apply onto a section of chain, 
# then again pick some oil
# then apply it to the next section where oil is not applied yet
# and so on till the complete chain is oiled.

'''------------------------------------------'''
# maximum sum of a sublist of size k
    
def maxSum(mylist, k):
    n = len(mylist) # length of the array

    if k > n: # k must be less than n
        print("Invalid")
        return -1
  
    window_sum = sum(mylist[:k]) # Compute sum of first window of size k
    # sums 1 + 4 + 2 + 10
    
    max_sum = window_sum # first sum available
    
    # Compute the sums of remaining windows by removing first element of previous
    # window and adding last element of the current window.
    for i in range(n - k):
        window_sum = window_sum - mylist[i] + mylist[i + k]
        # meaning: sum = current sum - first item + next item on queue
        max_sum = max(window_sum, max_sum)
    return max_sum
  
print(maxSum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
# sum of 3, 1, 0, 20 → 24