import FreeCAD, FreeCADGui

class PressMockupCommand:
    def GetResources(self):
        return {
            'Pixmap': 'PrintmakersToolbox/Resources/icons/PressMockup.svg',
            'MenuText': "Press Mockup",
            'ToolTip': "Creates a 3D mockup of a printing press."
        }

    def Activated(self):
        FreeCAD.Console.PrintMessage("Press Mockup Command Activated\n")

    def IsActive(self):
        return True

FreeCADGui.addCommand("PressMockupCommand", PressMockupCommand())