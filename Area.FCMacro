def MedirArea():
    area = 0.0
    for sel in Gui.Selection.getSelectionEx():
        obj = sel.Object
        tipo = obj.TypeId
        if 'Part' not in tipo:
            print('Objeto não é Part:', tipo)
            return
        else:
            if not sel.HasSubObjects:
                area += obj.Shape.Area
            else:
                for item in sel.SubObjects:
                    if item.ShapeType == 'Face':
                        area += item.Area
    print('area total: %fmm²' % area)

MedirArea()