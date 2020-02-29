start = int(input("How many slices of pizza did the pizza have?: ").strip())
end = int(input("How many slices of pizza did you eat?: ").strip())
left = start - end
print('You have {0} slices remaining. Enjoy :)'.format(left))
