def rgb(r, g, b):
    arr = [r, g, b]
    for x in range(len(arr)):
        if arr[x] > 255: arr[x] = 255 # changes out of range values to closest valid value
        if arr[x] < 0: arr[x] = 0
        arr[x] = hex(arr[x]).replace('0x', '').upper() # converts the numbers to (capitalized) hex values without '0x' prefix
        if len(arr[x]) == 1: arr[x] = '0'+arr[x] # makes sure the output has 6 chars, not the 3 char abbrv.
    return (''.join(arr))