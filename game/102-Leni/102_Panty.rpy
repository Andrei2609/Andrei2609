
init:
    $ l2_panty_win = "Images/Objets/panty/102-Leni/panty_l2.png"
    $ l2_panty_job = "Images/Objets/panty/panty_test.png"
    $ l2_panty_playa = "Images/Objets/panty/panty_test.png"
    $ l2_panty_shower = "Images/Objets/panty/panty_test.png"
    $ l2_panty_sleep = "Images/Objets/panty/panty_test.png"

    $ l2_panty_horror_2020 = "Images/Objets/panty/102-Leni/panty_l2_spider.png"
    $ l2_panty_fiesta = "Images/Objets/panty/panty_soiree.png"
    $ l2_panty_mom_party = "Images/Objets/panty/panty_quest_2.png"

screen l2_panty():
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
            label _("Culottes de Leni") xalign 0.5
        hbox:
            add "Images/Objets/panty/Photos/leni_slip.png"
            vbox:
                ysize 300
                imagebutton:
                    idle "Images/Objets/panty/Boutons/BT_classic_panties.png"
                    hover "Images/Objets/panty/Boutons/BT_classic_panties_hover.png"
                    xalign 0.5
                    yalign 0.5
                    action ShowMenu("l2_panty_classic")
                imagebutton:
                    idle "Images/Objets/panty/Boutons/BT_special_panties.png"
                    hover "Images/Objets/panty/Boutons/BT_special_panties_hover.png"
                    xalign 0.5
                    yalign 0.6
                    action ShowMenu("l2_panty_special")
                imagebutton:
                    xalign 0.01
                    yalign 0.99
                    idle "Images/Bases/Icones/Faces/face_retour.png"
                    hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                    action Jump("CollectBack")

screen l2_panty_classic():
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
                    if l2_win == True:
                        use panty_view(l2_panty_win, _("Ordinaire"), "")
                    else:
                        null
                    if l2_win_job == True:
                        use panty_view(l2_panty_job, _("Travaille"), "")
                    else:
                        null
                    if l2_win_plage == True:
                        use panty_view(l2_panty_playa, _("Plage"), "")
                    else:
                        null
                    imagebutton:
                        idle "Images/Bases/Icones/Faces/face_retour.png"
                        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                        action Jump("CollectBack")
                    if l2_win_shower == True:
                        use panty_view(l2_panty_shower, _("Douche"), "")
                    else:
                        null
                    if l2_win_sleep == True:
                        use panty_view(l2_panty_sleep, _("Lit"), "")
                    else:
                        null

screen l2_panty_special():
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
                grid 2 2:
                    spacing 5
                    xalign 0.5
                    if l2_halloween_2020 == True:
                        use panty_view(l2_panty_horror_2020, _("Halloween 2020"), "Halloween_2020_Review")
                    else:
                        null
                    if l2_fiesta == True:
                        use panty_view(l2_panty_fiesta, _("Fête dans la cave"), "l2_fiesta_Review")
                    else:
                        null
                    if mom_party_21 == True:
                        use panty_view(l2_panty_mom_party, _("Fête des mères"), "mom_party_2021_Review")
                    else:
                        null
                    null
                imagebutton:
                    idle "Images/Bases/Icones/Faces/face_retour.png"
                    hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                    action Jump("CollectBack")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
