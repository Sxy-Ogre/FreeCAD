import FreeCAD, FreeCADGui

class BlockLayoutCommand:
    def GetResources(self):
        return {
            'Pixmap': 'PrintmakersToolbox/Resources/icons/BlockLayout.svg',
            'MenuText': "Block Layout",
            'ToolTip': "Creates a layout for carving blocks."
        }

    def Activated(self):
        FreeCAD.Console.PrintMessage("Block Layout Command Activated\n")

    def IsActive(self):
        return True

FreeCADGui.addCommand("BlockLayoutCommand", BlockLayoutCommand())