def MedirComprimento():
    comprimento = 0.0
    for sel in Gui.Selection.getSelectionEx():
        obj = sel.Object
        tipo = obj.TypeId
        if 'Part' not in tipo:
            print('Objeto não é Part:', tipo)
            return
        else:
            if not sel.HasSubObjects:
                comprimento += obj.Shape.Length
            else:
                for item in sel.SubObjects:
                    if item.ShapeType in ['Edge','Face']:
                        comprimento += item.Length
    print('comprimento total: %f ' % comprimento)

MedirComprimento()