screen IMGshow(img):
    modal True
    zorder 100
    imagebutton:
        idle img
        xalign 0.5
        yalign 0.5
        action Return(True)

screen Menu_galerie():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        background Frame("gui/frame_tirroir.png", gui.frame_borders, tile=gui.frame_tile)
        has hbox:
            spacing 10
            xalign 0.5
            yalign 0.1
        imagebutton:
            idle "Images/Bases/Galerie/LoudBook.png"
            hover "Images/Bases/Galerie/LoudBook_hover.png"
            xalign 0.5
            action Jump("Souvenirs_Loud")
        imagebutton:
            idle "Images/Bases/Galerie/OtherBook.png"
            hover "Images/Bases/Galerie/OtherBook_hover.png"
            xalign 0.5
            action Jump("Souvenirs_Autres")
    imagebutton:
        xalign 0.2
        yalign 0.9
        idle "Images/Bases/Icones/Faces/face_retour.png"
        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
        action Return(True)

screen Galerie_loud():
    add "Images/Bases/Galerie/LoudBook_open.png" xalign 0.5 ypos 50
    vbox:
        xalign 0.42
        ypos 60
        spacing 10
        label _("Galerie des Loud") xalign 0.5
        add "Images/Bases/Galerie/OP_Loud.png" xalign 0.5
        text _("en cours de fabrication")
        grid 2 3:
            spacing 10
            xalign 0.5
            hbox:
                add "Images/Bases/Galerie/face-mom.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-lori.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-leni.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-luna.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-luan.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-lynn.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen Galerie_other():
    add "Images/Bases/Galerie/OtherBook_open.png" xalign 0.5 ypos 50
    vbox:
        xalign 0.42
        ypos 60
        spacing 10
        label _("Galerie des autres") xalign 0.5
        add "Images/Bases/Galerie/OP_Other.png" xalign 0.5
        text _("en cours de fabrication")
        grid 2 2:
            spacing 10
            xalign 0.5
            hbox:
                add "Images/Bases/Galerie/face-maria.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-ronnie.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            hbox:
                add "Images/Bases/Galerie/face-christina.png"
                imagebutton:
                    idle "Images/Bases/Galerie/replay.png"
                    hover "Images/Bases/Galerie/replay_hover.png"
                    xalign 0.5
                    action Return(True)
            null
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

label Souvenirs_Loud:
    hide screen Menu_galerie
    call screen Galerie_loud
    hide screen Galerie_loud
    return

label Souvenirs_Autres:
    hide screen Menu_galerie
    call screen Galerie_other
    hide screen Galerie_other
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
