a = {1,2,3,4}
target = 5
seen = set()
found = False
for num in a:
    comp = target - num
    if comp in seen:
        print("Pair found:", comp, num)
        found = True
    seen.add(num)

if not found:
    print("No pair sums to", target)
# ...existing code...