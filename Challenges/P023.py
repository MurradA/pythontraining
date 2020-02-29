first_line = input("Enter the first line of a nursery rhyme: ")
print("\"{0}\" has a length of :".format(first_line)+str(len(first_line)))

start = int(input("Enter a start position: ").strip())
end = int(input("Enter an end position: ").strip())

print(first_line[start:end+1:1])

