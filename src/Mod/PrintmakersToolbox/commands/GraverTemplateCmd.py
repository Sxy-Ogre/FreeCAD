import FreeCAD, FreeCADGui

class GraverTemplateCommand:
    def GetResources(self):
        return {
            'Pixmap': 'PrintmakersToolbox/Resources/icons/GraverTemplate.svg',
            'MenuText': "Graver Template",
            'ToolTip': "Creates a template for graver shapes."
        }

    def Activated(self):
        angle, ok1 = QtWidgets.QInputDialog.getDouble(None, "Tool Angle", "Enter tool angle (degrees):", 45.0, 1.0, 89.0, 1)
        if not ok1:
            return

        extension, ok2 = QtWidgets.QInputDialog.getDouble(None, "Extension Length", "Enter extension length (mm):", 20.0, 1.0, 100.0, 1)
        if not ok2:
            return

        width = 20.0
        slot_width = 3.0
        slot_depth = 1.5

        rad = math.radians(angle)
        height = math.tan(rad) * extension
        length = extension

        wedge = Part.makeBox(length, width, height)
        slot = Part.makeBox(length, slot_width, slot_depth)
        slot.translate(FreeCAD.Vector(0, (width - slot_width)/2, height - slot_depth))

        wedge_with_slot = wedge.cut(slot)

        doc = FreeCAD.ActiveDocument or FreeCAD.newDocument("GraverTemplate")
        obj = doc.addObject("Part::Feature", "GraverTemplate")
        obj.Shape = wedge_with_slot
        doc.recompute()

    def IsActive(self):
        return True

FreeCADGui.addCommand("GraverTemplateCommand", GraverTemplateCommand())