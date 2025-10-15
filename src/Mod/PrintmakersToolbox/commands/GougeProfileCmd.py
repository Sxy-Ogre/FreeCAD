import FreeCAD, FreeCADGui

class GougeProfileCommand:
    def GetResources(self):
        return {
            'Pixmap': 'PrintmakersToolbox/Resources/icons/GougeProfile.svg',
            'MenuText': "V-Gouge Profile",
            'ToolTip': "Creates a cross-section of a V-gouge."
        }

    def Activated(self):
        FreeCAD.Console.PrintMessage("V-Gouge Profile Activated\n")

    def IsActive(self):
        return True

FreeCADGui.addCommand("GougeProfileCommand", GougeProfileCommand())
