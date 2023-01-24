# # beecrowd | 1024
# # Encryption

# import re

# def encription(text):
#     text_new = ''
#     for l in text:
#        if re.match('[a-zA-z]', l):
#            # ord() Return the Unicode code point for a one-character string.  
#            # chr() Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
#            text_new += chr(ord(l)+3)    
#        else:
#            text_new += l
          
#     text_new = text_new[::-1]
#     """In Python, the syntax text_new[::-1] is used to reverse a string. 
#     The [::-1] slice notation is used to step through the string backwards, starting from the last character, 
#     and ending at the first character. This effectively reverses the order of the characters in the string. For example, 
#     if text_new = "hello", then text_new[::-1] would return the string "olleh"."""
    
#     subTex = int((len(text_new)/2))
#     tx1 = text_new[0:subTex]
#     tx2 = text_new[subTex:]
#     tx2_new  = ''
#     for l in tx2:
#         tx2_new += chr(ord(l)-1)
    
#     final_text = tx1 + tx2_new
#     return final_text
       
   
# n = int(input().strip())

# for i in range(0, n):
#     text = input().strip()
#     result = encription(text)
#     print(result)

# beecrowd | 1024
# Encryption

import re

def reverstx(text):
    text_new = ''
    for l in text:
        if re.match("[a-zA-Z]", l):
           text_new += chr(ord(l)+3)
           
        else:
           text_new += l
    
    return text_new

def left_move(tx2):
    tx2_new = ''
    for l in tx2:
        tx2_new += chr(ord(l)-1)
    
    return tx2_new


if __name__ == "__main__":
    n = int(input().strip())
    for i in range(0, n):
        text = input().strip()
        text_new = reverstx(text)
        text_new = text_new[::-1]
        subTex = int((len(text_new)/2))
        tx1 = text_new[0:subTex]
        tx2 = text_new[subTex:]
        tx2_new  = left_move(tx2)
        final_text = tx1 + tx2_new
        
        print(final_text)