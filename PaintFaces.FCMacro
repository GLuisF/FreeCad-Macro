# App.ActiveDocument = App.getDocument('Document_Name') 
# Get object by name
obj = App.ActiveDocument.getObject('Part__Feature')

# Get object by label
obj = App.ActiveDocument.getObjectsByLabel('ObjectLabel')[0]

# Get All Objects in active document
obj = App.ActiveDocument.findObjects("Part::Feature")

# Get selected objects
obj = Gui.Selection.getSelection()

# Get selected faces
sel = Gui.Selection.getSelectionEx()[0]

def SelectFacesCodePilot(obj):
  # não funciona
  for i in range(len(obj.Shape.Faces)):
    obj.ViewObject.ElementNames.append('Face'+str(i+1))
  print('[*] Selected %d faces'%(len(obj.Shape.Faces),))

# https://forum.freecadweb.org/viewtopic.php?f=22&t=23686&start=10#p185119
shapes=App.ActiveDocument.findObjects("Part::Feature")
for sh in shapes:
  for i in range(len(sh.Shape.Faces)):
    face = "Face%d" % (i+1)
    Gui.Selection.addSelection(sh, face)

# https://forum.freecadweb.org/viewtopic.php?t=7125
def setObjColor(obj, color):
  # set color for all faces of selected object
  colorlist=[]
  for i in range(len(obj.Shape.Faces)):
    colorlist.append(color)
  print('[*] Object contains %d faces'%(len(colorlist),))
  obj.ViewObject.DiffuseColor = colorlist

def setColorOfSelectedFaces(sel, colorSelected, colorBase):
    # faces can be selected with mouse
    obj = sel.Object
    # got all faces indexes
    faceIdx = []
    for item in sel.SubElementNames:
        if item.startswith('Face'):
            faceIdx.append(int(item[4:])-1)
    print('[*] Object %s contains %d faces'%(obj.Name, len(faceIdx)))
    # Loop over whole object faces, make list of colors
    setColor = []
    for idx in range(len(obj.Shape.Faces)):
        if idx in faceIdx:
            setColor.append(colorSelected)
        else:
            setColor.append(colorBase)
    obj.ViewObject.DiffuseColor = setColor
    print('[*] ... colored %d faces'%(len(setColor),))