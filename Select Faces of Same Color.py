def SelectFacesByColor(sel = None):
    obj = sel.Object
    faceIdx = []
    objColors = obj.ViewObject.DiffuseColor
    item = sel.SubElementNames[0]
    faceIdx = int(item[4:])-1
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

def SelectionType():
    sel = Gui.Selection.getSelectionEx()
    if len(sel) == 0:
        print('Nada foi selecionado:', sel)
        return
    elif len(sel) > 1:
        print('Mais de um objeto selecionado:', sel)
        return
    else:
        sel = sel[0]
        obj = sel.Object
        tipo = obj.TypeId
        if 'Part' not in tipo:
            print('Objeto não é Part:', tipo)
            return
        else:
            if not sel.HasSubObjects:
                print('Part inteira foi selecionada:', obj.TypeId)
                return
            else:
                item = sel.SubElementNames
                if len(item) > 1:
                    print('Mais de 1 item foi selecionado:', item)
                    return
                else:
                    sub_obj = sel.SubObjects[0]
                    tipo = sub_obj.ShapeType
                    if tipo != 'Face':
                        print('Objeto não é Face:', tipo)
                        return
                    else:
                        print('Face selecionada')
                        return sel

sel = SelectionType()
if sel != None:
    SelectFacesByColor(sel)