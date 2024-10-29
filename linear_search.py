def linear_search(list,target):
    #returns the positiom of the target if found, else returns None
    for i in range(0,len(list)):
        if list[i] == target:
            return i+1
    return None
def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else: print("target not found in list")
    
    
num = [1,2,3,4,5,6,7,8,9,11,22]

result = linear_search(num, 8)
verify(result)

result = linear_search(num, 2)
verify(result)

result = linear_search(num, 12)
verify(result)