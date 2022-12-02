Input = open("data/dag 1. input.txt", "r").read().split("\n\n")

print(max([sum(getallen) for getallen in [[int(getal) for getal in row.split("\n")] for row in Input]]))
print(sum(sorted([sum(getallen) for getallen in [[int(getal) for getal in row.split("\n")] for row in Input]], reverse=True)[0:3]))