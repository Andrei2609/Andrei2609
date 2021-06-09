screen ronnie_panty():
    frame:
        xalign 0.5 ypos 50
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox
        label _("Ronnie Anne") xalign 0.5
        hbox:
            add "Images/Objets/panty/Photos/ronnie_slip.png"
            vbox:
                text _("Culottes Classiques") xalign 0.5
                hbox:
                    if ronnie_win == True:
                        add "Images/Objets/panty/panty_test.png" xalign 0.5
                text ""
                text _("Culottes Spéciales") xalign 0.5
                hbox:
                    if ronnie_win == True:
                        add "Images/Objets/panty/panty_test.png" xalign 0.5
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("CollectBack")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
