
def split_string(source, splitlist):
    output = []
    atsplit = True #At a split point
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                #Add char to last word
                output[-1] = output[-1] + char
    return output

out = split_string("After  the flood  ... all the colors came out.", " .")
print(out)
  
