data_set = {'John':{'N':3056, 'S':8463,'E':8441, 'W':2451},
            'Tom':{'N':4832, 'S':6786,'E':4737, 'W':2451},
            'Anne':{'N':5239, 'S':4802,'E':5820, 'W':2451},
            'Fiona':{'N':3904, 'S':3645,'E':8821,'W':2451}}


print("\nRegional Sales:")
print("")
for x in data_set:
    print(x,":", data_set[x])

name = input("\nEnter a name from the dictionary to change:").strip().capitalize()

region = input("\nSelect a region (N/S/E/W): ").capitalize().strip()

print([data_set[name][region]])

newdata = int(input("Enter new data:"))
data_set[name][region] = newdata

print(data_set[name])

















# tryagain = True
#
# while tryagain == True:
#     name = input("\nEnter a name from the dictionary to change:").strip().capitalize()
#
#     for name in data_set:
#
#         if name in data_set:
#             region = input("\nSelect a region (N/S/E/W): ").capitalize().strip()
#
#             if region == 'N' or region == 'S' or region == 'E' or region == 'W':
#                     num = int(input("\nEnter a number:").strip())
#                     data_set[name][region] = data_set[num]
#                     tryagain = False
#             else:
#                 print("\nInvalid Entry!")
#
#         else:
#             print("\nName not in dictionary")
#             break
#
#
# print("")
# for x in data_set:
#     print(x,":", data_set[x])
#
#
