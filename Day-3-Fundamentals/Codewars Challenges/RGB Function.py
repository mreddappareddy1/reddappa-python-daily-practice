def rgb(r, g, b):
    # your code here :)
    colors = [r,g,b]
    hexString = "".join([str(hex(color)).upper() for color in colors]).replace("0X","").replace("0","00")
    return hexString

def rgb2(r,g,b):
    colors = [r,g,b]
    hexColor = ""
    for color in colors:
        if color >=0 and color < 16:
            hexColor = hexColor + '0'+ hex(color)
        elif color <0: 
            hexColor = hexColor + "00"
        elif color > 255:
            hexColor = hexColor + "FF"
        else:
            hexColor = hexColor + hex(color)
    print(hexColor.replace("0x","").upper())

print(rgb2(16,407,29))