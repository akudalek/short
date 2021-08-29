try:
    r: int = int(input("Red count:"))
    w: int = int(input("White1 count:"))
except ValueError as e:
    print("Run the program again and enter only integer values")

if max(r, w) > min(r, w) * 2:
    print("No solutions ")
    exit(0)

solution: str = "Mm" * min(r, w)

for _ in range(max(r, w) - min(r, w)):
    if solution.find('mMm') != -1:
        solution = solution.replace('mMm', 'mMMm', 1)
    else:
        solution = solution + 'M'

replacements = {
    "M": 'R' if r >= w else "W",
    "m": 'R' if r < w else "W"
}
solution = "".join([replacements.get(c, c) for c in solution])

print(f"Solution: {solution}")
