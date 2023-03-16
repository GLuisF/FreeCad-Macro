colorCode = '#FF0080'
# convert color code to RGB
rgb = tuple(int(colorCode[i:i+2], 16)/255 for i in (1, 3, 5))
print(colorCode, rgb)

def ConvertColorCode(colorCode):
    # convert color code to RGB
    rgb = tuple(int(colorCode[i:i+2], 16)/255 for i in (1, 3, 5))
    return rgb

def GetColorSelected():
    # get selected faces
    sel = Gui.Selection.getSelectionEx()[0]
    obj = sel.Object
    objColors = obj.ViewObject.DiffuseColor
    item = sel.SubElementNames[0]
    if item.startswith('Face'): 
        if len(objColors) == 1:
            return objColors[0]
        else:
            faceIdx = int(item[4:])-1
            return objColors[faceIdx]
    else:
        print('No face selected')
        return

#convert rgb tuple to hex string
def ConvertRGBToHex(rgb):
    return '#%02x%02x%02x' % rgb

#convert r,g,b to hex string
def ConvertRGB(r, g, b, *rest):
    return '#%02X%02X%02X' % (int(r*255), int(g*255), int(b*255))

ConvertRGB(0.5, 0.5, 0.5)