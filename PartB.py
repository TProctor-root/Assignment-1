import sys

# O(n): Linear Time
# When the file opens, a loop is started that takes all the text from the
# file and stores the text into a data type that runs in O(1) time.
def storing(filename):
    text = ''
    with open(filename, 'r', encoding = 'utf-8') as fOpen:
        for line in fOpen:
            text += line
            
    return text

# O(n): Linear Time
# A loop that forms the maximum tokens from the file size in for N times and
# uses if and else conditions to check the certain character to be consider
# tokens in O(1) time.
def collecting(amount):
    temp = ''
    storage = []

    
    for x in range(len(amount)):
    # Code: "for x in range(len(amount)):"
    # Source: https://www.pitt.edu/~naraehan/python3/more_on_for_loops.html
        if 47 < ord(amount[x]) < 58:
            temp = temp + amount[x]  
        elif 64 < ord(amount[x]) < 91:
            temp = temp + amount[x].lower()
        elif 96 < ord(amount[x]) < 123:
            temp = temp + amount[x]
        else:
            if temp:
                storage.append(temp)
                # Code: "storage.append(temp)"
                # Source: https://www.tutorialspoint.com/python/list_append.htm
                temp = ''
                
    return storage

# O(n): Linear Time
# A loop that runs for N times depending on the number of tokens to find the
# maximum frequency using if and else statements in O(1) time. Also, the
# worst-case depending on the number of tokens in the data type is O(n).
def counting(wLeft):
    times = {}
    
    for y in wLeft:
        if y in times:
            times[y] = times[y] + 1
        else:
            times[y] = 1
            
    return times

# O(n): Linear Time
# A loop that will go through every token in the first argument in O(1)
# times then compare it with tokens in the second argument in O(1) times.
# After incrementing all the numbers of common tokens in the first and
# second argument, it will print the total number of common tokens found
# in both arguments running in O(1).
def results(first, second):
    compare = 0

    for z in first.keys():
    # Code: "for z in first.keys():"
    # Source: https://www.freecodecamp.org/news/python-dictionary-guide/
    # Source: https://realpython.com/iterate-through-dictionary-python/
        if z in second:
            compare = compare + 1
    print(compare)

if __name__ == "__main__":   
    a = storing(sys.argv[1])
    b = storing(sys.argv[2])
    
    a2 = collecting(a)
    b2 = collecting(b)

    a3 = counting(a2)
    b3 = counting(b2)

    results(a3, b3)          

