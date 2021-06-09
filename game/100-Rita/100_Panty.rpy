init:
    $ mom_panty_win = "Images/Objets/panty/panty_test.png"
    $ mom_panty_job = "Images/Objets/panty/panty_test.png"
    $ mom_panty_playa = "Images/Objets/panty/panty_test.png"
    $ mom_panty_shower = "Images/Objets/panty/panty_test.png"
    $ mom_panty_sleep = "Images/Objets/panty/panty_test.png"

    $ mom_panty_dog = "Images/Objets/panty/100-Rita/panty_mom_dog.png"

screen mom_panty():
    modal True
    frame:
        xalign 0.5
        yalign 0.1
        xsize 500
        ysize 380
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox:
            xalign 0.5
            yalign 0.93
        frame:
            xalign 0.5
            label _("Culottes de Rita") xalign 0.5
        hbox:
            add "Images/Objets/panty/Photos/Rita_slip.png"
            vbox:
                ysize 300
                imagebutton:
                    idle "Images/Objets/panty/Boutons/BT_classic_panties.png"
                    hover "Images/Objets/panty/Boutons/BT_classic_panties_hover.png"
                    xalign 0.5
                    yalign 0.5
                    action ShowMenu("mom_panty_classic")
                imagebutton:
                    idle "Images/Objets/panty/Boutons/BT_special_panties.png"
                    hover "Images/Objets/panty/Boutons/BT_special_panties_hover.png"
                    xalign 0.5
                    yalign 0.6
                    action ShowMenu("mom_panty_special")
                imagebutton:
                    xalign 0.01
                    yalign 0.99
                    idle "Images/Bases/Icones/Faces/face_retour.png"
                    hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                    action Jump("CollectBack")

screen mom_panty_classic():
    modal True
    frame:
        xalign 0.9
        yalign 0.8
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox:
            xalign 0.5
            yalign 0.93
        add "Images/Objets/panty/Boutons/BT_classic_panties.png" xalign 0.5
        hbox:
            xalign 0.5
            vbox:
                grid 3 2:
                    spacing 5
                    xalign 0.5
                    if mom_win == True:
                        use panty_view(mom_panty_win, _("Ordinaire"), "")
                    else:
                        null
                    if mom_win_job == True:
                        use panty_view(mom_panty_job, _("Travaille"), "")
                    else:
                        null
                    if mom_win_plage == True:
                        use panty_view(mom_panty_playa, _("Plage"), "")
                    else:
                        null
                    imagebutton:
                        idle "Images/Bases/Icones/Faces/face_retour.png"
                        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                        action Jump("CollectBack")
                    if mom_win_shower == True:
                        use panty_view(mom_panty_shower, _("Douche"), "")
                    else:
                        null
                    if mom_win_sleep == True:
                        use panty_view(mom_panty_sleep, _("Lit"), "")
                    else:
                        null

screen mom_panty_special():
    modal True
    frame:
        xalign 0.8
        yalign 0.8
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox:
            xalign 0.5
            yalign 0.93
        add "Images/Objets/panty/Boutons/BT_special_panties.png" xalign 0.5
        hbox:
            xalign 0.5
            vbox:
                hbox:
                    spacing 5
                    xalign 0.5
                    if mom_dog_house == True:
                        use panty_view(mom_panty_dog, _("Coincée dans la niche"), "mom_quest_1_Review")
                imagebutton:
                    idle "Images/Bases/Icones/Faces/face_retour.png"
                    hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                    action Jump("CollectBack")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
