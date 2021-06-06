def findSum(arr, targetSum):
    for x in arr:
        compliment = targetSum - x
        if(compliment in arr):
            return [compliment, x]
    return None

print(findSum([2,7,11,15],9))
