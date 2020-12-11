#Binary search for a number
#before writing a code for a binary search, the given list must be in sorted format
pos = 0
def search(list, n):

    lb = 0
    ub = len(list)-1

    while lb <= ub:
       
        mid = (lb + ub) // 2
        globals()['pos'] = mid

        if list[mid] == n:
            #globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lb = mid+1
            else:
                ub = mid-1
    return False


list = [4, 7, 8, 12, 45, 99, 1024, 2345, 89765, 234567]
n = 234567

if search(list, n):
    print(n, ' is at index ', pos )
else:
    print('Not found')