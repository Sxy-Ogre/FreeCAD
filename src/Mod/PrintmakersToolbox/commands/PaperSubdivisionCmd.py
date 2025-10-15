import FreeCAD, FreeCADGui

class PaperSubdivisionCommand:
    def GetResources(self):
        return {
            'Pixmap': 'PrintmakersToolbox/Resources/icons/PaperSubdivision.svg',
            'MenuText': "Paper Subdivision",
            'ToolTip': "Divides a paper sheet into sections for printmaking."
        }

    def Activated(self):
        FreeCAD.Console.PrintMessage("Paper Subdivision Command Activated\n")

    def IsActive(self):
        return True

FreeCADGui.addCommand("PaperSubdivisionCommand", PaperSubdivisionCommand())