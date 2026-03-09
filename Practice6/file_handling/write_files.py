with open("input.txt", "a") as f:
    f.write("Now this is the new content :)\n")

with open("input.txt") as f:
    print(f.read())


# with open("input.txt", "w") as f:
#   f.write("This is the new content :)")

# with open("input.txt") as f:
#    print(f.read())
