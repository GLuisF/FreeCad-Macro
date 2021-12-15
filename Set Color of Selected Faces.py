def setColorFaces(colorSelected, colorBase=None):
    sel = Gui.Selection.getSelectionEx()[0]
    # faces can be selected with mouse
    obj = sel.Object
    # got all faces indexes
    faceIdx = []

    # get old colors of object
    objColors = obj.ViewObject.DiffuseColor 
        
    for item in sel.SubElementNames:
        if item.startswith('Face'):
            faceIdx.append(int(item[4:])-1)
    print('%d faces selected of object %s '%(len(faceIdx), obj.Label))
    # Loop over whole object faces, make list of colors
    setColor = []
    count = 0
    for idx in range(len(obj.Shape.Faces)):
        if idx in faceIdx:
            setColor.append(colorSelected)
            count += 1
        elif colorBase == None:
            if len(objColors) == 1:
                setColor.append(objColors[0])
            else:
                setColor.append(objColors[idx])
        else:
            setColor.append(colorBase)

    obj.ViewObject.DiffuseColor = setColor
    print('%d selected faces colored' % count)
    print('%d total faces' % len(setColor))