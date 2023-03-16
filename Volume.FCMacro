def MedirVolume():
    volume = 0.0
    for sel in Gui.Selection.getSelectionEx():
        obj = sel.Object
        tipo = obj.TypeId
        if 'Part' not in tipo:
            print('Objeto não é Part:', tipo)
            return
        else:
            if not sel.HasSubObjects:
                volume += obj.Shape.Volume
            else:
                for item in sel.SubObjects:
                    if item.ShapeType == 'Face':
                        pass
                        #volume += item.Area
    print('volume total: %fmm³' % volume)

MedirVolume()