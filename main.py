x = print("welcome")
while x != 0:
 x = int(input("Enter a number:\n"))
 logic = ['or', 'and', 'not', 'nor', 'nand', '<<', '>>', 'bit-wise AND', 'bit-wise OR', 'bit-wise XOR', 'bit-wise inversion']
 sel = input(f"{logic}\nselect one:\n")
 y = int(input(f"{x} {sel} "))
 if sel == 'or': print(x or y)
 elif sel == 'and': print(x and y)
 elif sel == 'not': print(not x, not y)
 elif sel == '<<': print(x << y)
 elif sel == '>>': print(x >> y)
 elif sel == 'nor': print(x or not y)
 elif sel == 'nand': print(x and not y)
 elif sel == 'bit-wise AND': print(x & y)
 elif sel == 'bit-wise OR': print(x | y)
 elif sel == 'bit-wise XOR': print(x ^ y)
 elif sel == 'bit-wise inversion': print(~ x, ~ y)
 else: print("option invalid or not found");break 




