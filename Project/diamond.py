from slicing import character_printing
def generate_diamond(n):
    char = ['F','O','R','M','U','L','A','Q','S','O','L','U','T','I','O','N','S']
    if n % 2 == 0:  #Diamond pattern needs odd number
        n += 1

    mid = n // 2
    lines = []
    index = 0

    for i in range(n):
        row = i if i <= mid else n - i - 1
        num_chars = 2 * row + 1
        spaces = " " * (mid - row)

        ch = char[index%17]
        
        # To restart the list
        # if index == len(char):
        #     index = 0
        if num_chars == 1:
            line = spaces + ch 
        else:
            if index == n//2:
                s = character_printing(index, num_chars)
                # length = len(s)
                middle = len(s)//2
                #line = spaces + ch + "-"* (num_chars -2) + s[-1]
                line = spaces + s[0] + "-"*(middle - 1) + "|" + "-"*(middle - 1) + s[-1]
            else:
                s = character_printing(index, num_chars)
                middle = len(s)//2
                # line = spaces + s[0] + " "*(num_chars - 2) + s[-1]
                line = spaces + s[0] + " "*(middle - 1) + "|" + " "*(middle - 1) + s[-1]
        index = index + 1       
          
        lines.append(line)

    return "\n".join(lines)

print(generate_diamond(21))




