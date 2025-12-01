# AAHELI -> 2 and 3
# HEL
# 1 and 5 -> AHELI
# pos, n
char = ['F','O','R','M','U','L','A','Q','S','O','L','U','T','I','O','N','S']
length = len(char)

def character_printing(pos, n):
    new_s =""
    for i in range(pos, pos + n):
        #if i >= length - 1:
        #    i = 0
        new_s = new_s + char[i%16]
        
    return new_s

ans = character_printing(16,5)
print(ans)

# M U L A Q

