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

        ch = char[index]
        index = index + 1
        # To restart the list
        if index == len(char):
            index = 0
        if num_chars == 1:
            line = spaces + ch 
        else:
            if index % 2 == 0:
                line = spaces + ch + "-"* (num_chars -2) +ch
            else:
                line = spaces + (ch*num_chars)
          
        lines.append(line)

    return "\n".join(lines)

print(generate_diamond(21))


