# Read number of elements
n = int(input())
# Read elements into a set (to keep uniqueness & O(1) lookup)
s = set(map(int, input().split()))

# Read number of commands
m = int(input())

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "pop":
        # Instead of arbitrary pop, we remove the smallest element
        if len(s) == 0:
            raise KeyError("pop from empty set")
        smallest = min(s)       # find smallest
        s = {x for x in s if x != smallest}   # rebuild set without that element

    elif cmd[0] == "remove":
        x = int(cmd[1])
        if x not in s:
            raise KeyError(x)   # mimic Python's remove() behavior
        s = {v for v in s if v != x}  # remove manually

    elif cmd[0] == "discard":
        x = int(cmd[1])
        if x in s:
            s = {v for v in s if v != x}  # safely remove

# Finally, compute sum manually without sum()
total = 0
for value in s:
    total += value

print(total)
