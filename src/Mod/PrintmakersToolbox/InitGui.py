import FreeCADGui

class PrintmakersToolboxWorkbench(FreeCADGui.Workbench):
    MenuText = "Printmakers Toolbox"
    ToolTip = "Tools for printmakers: gravers, layouts, presses, and more."
    Icon = ":/icons/GraverTemplate.svg"

    def Initialize(self):
        import PrintmakersToolbox.commands
        self.appendToolbar("Printmakers Toolbox", [
            "GougeProfileCommand",
            "GraverTemplateCommand",
            "BlockLayoutCommand",
            "PaperSubdivisionCommand",
            "PressMockupCommand",
            "HelpCommand",
        ])
        self.appendMenu("Printmakers Toolbox", [
            "GougeProfileCommand",
            "GraverTemplateCommand",
            "BlockLayoutCommand",
            "PaperSubdivisionCommand",
            "PressMockupCommand",
            "HelpCommand",
        ])

    def GetClassName(self):
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(PrintmakersToolboxWorkbench())
