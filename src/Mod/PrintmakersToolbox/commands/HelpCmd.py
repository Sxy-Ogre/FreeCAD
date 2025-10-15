import FreeCAD, FreeCADGui

class HelpCommand:
    def GetResources(self):
        return {
            'Pixmap': 'PrintmakersToolbox/Resources/icons/Help.svg',
            'MenuText': "Help",
            'ToolTip': "Open the Printmakers Toolbox documentation."
        }

    def Activated(self):
        FreeCAD.Console.PrintMessage("Block Layout Command Activated\n")

    def IsActive(self):
        return True

FreeCADGui.addCommand("HelpCommand", HelpCommand())