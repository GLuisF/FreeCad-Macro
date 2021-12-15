def SelectFacesByColor(sel = None):
    "SelectFacesByColor()"
    if sel == None: sel = Gui.Selection.getSelectionEx()
    if type(sel) == list:
        if len(sel) == 0:
            print('No object selected')
            return
        elif len(sel) >= 1:
            sel = sel[0]
    # faces can be selected with mouse
    obj = sel.Object
    # got all faces indexes
    faceIdx = []
    # get old colors of object
    objColors = obj.ViewObject.DiffuseColor
    item = sel.SubElementNames[0]
    if item.startswith('Face'): 
        faceIdx = int(item[4:])-1
    else:
        print('No face selected')
        return
    n = 0
    for idx in range(len(obj.Shape.Faces)):
        if len(objColors) == 1:
            face = "Face%d" % (idx+1)
            Gui.Selection.addSelection(obj, face)
            n += 1
        elif objColors[idx] == objColors[faceIdx]:
            face = "Face%d" % (idx+1)
            Gui.Selection.addSelection(obj, face)
            n += 1
            
    print('%d face%s selected' % (n,'s' if n>1 else ''))

