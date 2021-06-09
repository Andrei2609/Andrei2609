screen panty_view(panty, nom, link):
    button:
        frame:
            xalign 0.5
            background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
            hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
            has vbox:
                xalign 0.5
                yalign 0.5
            add panty xalign 0.5
            text nom xalign 0.5
        action Jump(link)

screen Menu_collection():
    frame:
        xalign 0.5 ypos 50
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox
        add "Images/Bases/collection.png" xalign 0.5
        grid 3 3:
            spacing 5
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_rita.png"
                hover "Images/Objets/panty/Boutons/BT_rita_hover.png"
                xalign 0.5

                action ShowMenu("mom_panty")
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_lori.png"
                hover "Images/Objets/panty/Boutons/BT_lori_hover.png"
                xalign 0.5

                action ShowMenu("l1_panty")
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_leni.png"
                hover "Images/Objets/panty/Boutons/BT_leni_hover.png"
                xalign 0.5

                action ShowMenu("l2_panty")
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_luna.png"
                hover "Images/Objets/panty/Boutons/BT_luna_hover.png"
                xalign 0.5

                action ShowMenu("l3_panty")
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_luan.png"
                hover "Images/Objets/panty/Boutons/BT_luan_hover.png"
                xalign 0.5

                action ShowMenu("l4_panty")
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_lynn.png"
                hover "Images/Objets/panty/Boutons/BT_lynn_hover.png"
                xalign 0.5

                action ShowMenu("l5_panty")
            null
            imagebutton:
                idle "Images/Objets/panty/Boutons/BT_autres.png"
                hover "Images/Objets/panty/Boutons/BT_autres_hover.png"
                xalign 0.5

                action ShowMenu("autres_panty")
            null
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

label CollectBack:
    hide screen mom_panty
    hide screen l1_panty
    hide screen l2_panty
    hide screen l3_panty
    hide screen l4_panty
    hide screen l5_panty
    hide screen other_panty
    call screen Menu_collection

screen autres_panty():
    frame:
        xalign 0.5 ypos 50
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox
        label _("Autres Filles") xalign 0.5
        grid 4 2:
            if l7_win == True:
                add "Images/Objets/panty/panty_test.png" xalign 0.5
            else:
                null
            if l8_win == True:
                add "Images/Objets/panty/panty_test.png" xalign 0.5
            else:
                null
            if l9_win == True:
                add "Images/Objets/panty/panty_test.png" xalign 0.5
            else:
                null
            if l10_win == True:
                add "Images/Objets/panty/panty_l10.png" xalign 0.5
            else:
                null
            if l11_win == True:
                add "Images/Objets/panty/panty_test.png" xalign 0.5
            else:
                null
            if carol_win == True:
                add "Images/Objets/panty/panty_test.png" xalign 0.5
            else:
                null
            if ronnie_win == True:
                add "Images/Objets/panty/panty_test.png" xalign 0.5
            else:
                null
            null
        text ""
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("CollectBack")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
