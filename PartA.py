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

# O(n log n): Quasilinear Time
# First uses sorting to sort the frequencies which takes about O(n log n) time
# and prints the frequencies using O(n). In worst case, the function runs
# in O(n log n).
def results(last):
    sorting = sorted(last.items(), key = lambda wn: (-wn[1], wn[0]))
    # Code: "sorted(last.items(), key = lambda wn: (-wn[1], wn[0]))"
    # Source: https://www.simplifiedpython.net/python-sort-dictionary-by-value/
    
    for z in sorting:
        print(z[0] + '\t' + str(z[1]))

if __name__ == "__main__":
    a = storing(sys.argv[1])
    b = collecting(a)
    c = counting(b)
    results(c)
