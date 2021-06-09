screen Tiroir(retour):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        background Frame("gui/frame_tirroir.png", gui.frame_borders, tile=gui.frame_tile)
    imagebutton:
        xalign 0.2
        yalign 0.9
        idle "Images/Bases/Icones/Faces/face_retour.png"
        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
        action Jump(retour)

screen Placard():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        background Frame("gui/frame_tirroir.png", gui.frame_borders, tile=gui.frame_tile)
        vbox:
            xalign 0.5
            yalign 0.5
            text _("Pour les anciennes sauvegardes") xalign 0.5
            text _("appuyé sur le bouton.") xalign 0.5
            text _("Pour éviter tout bug de compatibilité.") xalign 0.5
        imagebutton:
            xalign 0.9
            yalign 0.1
            idle "Images/Plans/CH_l6/bouton_update.png"
            hover "Images/Plans/CH_l6/bouton_update_hover.png"
            action Jump("debug_variables_update")
    imagebutton:
        xalign 0.2
        yalign 0.9
        idle "Images/Bases/Icones/Faces/face_retour.png"
        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
        action Return(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
