screen MenuPause():
    frame:
        xalign 0.5
        yalign 0.2
        has vbox
        label _("Pause") xalign 0.5
        text ""
        hbox:
            spacing 20
            xalign 0.5
            vbox:
                imagebutton:
                    idle "Images/Bases/Icones/save.png"
                    hover "Images/Bases/Icones/save_hover.png"
                    xalign 0.5
                    action ShowMenu("save")
                text _("Sauvegarder")
            vbox:
                imagebutton:
                    idle "Images/Bases/Icones/home.png"
                    hover "Images/Bases/Icones/home_hover.png"
                    xalign 0.5
                    action MainMenu()
                text _("Menu")
            vbox:
                imagebutton:
                    idle "Images/Bases/Icones/option.png"
                    hover "Images/Bases/Icones/option_hover.png"
                    xalign 0.5
                    action ShowMenu("preferences")
                text _("Préférences")
            vbox:
                imagebutton:
                    idle "Images/Bases/Icones/exit.png"
                    hover "Images/Bases/Icones/exit_hover.png"
                    xalign 0.5
                    action ShowMenu("quit")
                text _("Quitter")
        text ""
        textbutton _("Retour au Jeu"):
            xalign 0.5
            action Return(True)

screen Menu_des_stats():
    frame:
        xalign 0.5 ypos 50
        has hbox:
            spacing 5
        frame:
            yalign 0.5
            xalign 0.5
            has vbox
            label _("Tenue Actuelle") xalign 0.5
            use User(tenue, "")
        vbox:
            spacing 5
            hbox:
                xalign 0.5
                spacing 10
                add "Images/Bases/Avatars/Av_user.png" xalign 0.5 yalign 0.5
                vbox:
                    label "Fiche de Lincoln" xalign 0.5 yalign 0.5
                    text ""
                    hbox:
                        spacing 10
                        xalign 0.5
                        add "Images/Bases/Icones/aime.png" xalign 0.5
                        text ": Ace Savy" yalign 0.5
                    hbox:
                        spacing 10
                        xalign 0.5
                        add "Images/Bases/Icones/not_aime.png" xalign 0.5
                        text _(": Tante Ruth") yalign 0.5
            text "_______________________________"
            vbox:
                spacing 5
                grid 2 2:
                    spacing 3
                    use stat(_("Santé :"), vie_points)
                    use stat(_("Excitation :"), sex_points)
                    use stat(_("Ruse :"), int_points)
                    use stat(_("Force :"), force_points)
                hbox:
                    spacing 10
                    xalign 0.5
                    frame:
                        xalign 0.5
                        ysize 110
                        has vbox:
                            yalign 0.5
                            xalign 0.5
                        text _("{font=FT_Slapstick.ttf}{size=30}{color=#556B2F}Argent{/color}{/size}{/font}") xalign 0.5
                        text _("{font=FT_Slapstick.ttf}[user_coins] {color=#556B2F}${/color}{/font}") xalign 0.5
                    frame:
                        xalign 0.5
                        has hbox:
                            spacing 5
                        add "Images/Bases/Icones/Faces/face_school.png" xalign 0.5 yalign 0.5
                        vbox:
                            yalign 0.5
                            text _("Réputation") xalign 0.5
                            hbox:
                                spacing 5
                                xalign 0.5
                                yalign 0.5
                                add "Images/Bases/Icones/not_aime.png" yalign 0.5 xalign 0.5
                                bar value AnimatedValue(school_points, 100, 0.5) style "slider" xsize 150 yalign 0.5 xalign 0.5
                                add "Images/Bases/Icones/aime.png" yalign 0.5 xalign 0.5
            imagebutton:
                xalign 0.99
                yalign 0.99
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action Return(True)

screen User(tenue, exp):
    zorder 200
    if sex_points >= 50 and tenue == "normal":
        if exp == "_P":
            add "Lincoln_X_P" xalign 0 yalign 1.0
        elif exp == "I":
            add "I_Lincoln_X" xalign 0 yalign 1.0
        else:
            add "Lincoln_X" xalign 0 yalign 1.0
    elif sex_points >= 50:
        if exp == "_P":
            add "Lincoln_[tenue]_X_P" xalign 0 yalign 1.0
        elif exp == "I":
            add "I_Lincoln_[tenue]_X" xalign 0 yalign 1.0
        else:
            add "Lincoln_[tenue]_X" xalign 0 yalign 1.0
    elif tenue == "normal":
        if exp == "_P":
            add "Lincoln_P" xalign 0 yalign 1.0
        elif exp == "I":
            add "I_Lincoln" xalign 0 yalign 1.0
        else:
            add "Lincoln[exp]" xalign 0 yalign 1.0
    else:
        if exp == "_P":
            add "Lincoln_[tenue]_P" xalign 0 yalign 1.0
        elif exp == "I":
            add "I_Lincoln_[tenue]" xalign 0 yalign 1.0
        else:
            add "Lincoln_[tenue][exp]" xalign 0 yalign 1.0

screen NewUser(bras, cheveux, slip, tenue, acc1, acc2, acc3, exp, position):
    add "Images/Personnages/nouveau/user/corps.png" xalign 0.0 yalign 1.0
    if cheveux <> "":
        add "Images/Personnages/nouveau/user/Cheveux/[cheveux].png" xalign 0.0 yalign 1.0
    add "Images/Personnages/nouveau/user/Bras/[bras]_G.png" xalign 0.0 yalign 1.0
    if slip <> "" and sex_points >= 50:
        add "Images/Personnages/nouveau/user/Slip/[slip]_X.png" xalign 0.0 yalign 1.0
    elif slip <> "":
        add "Images/Personnages/nouveau/user/Slip/[slip].png" xalign 0.0 yalign 1.0
    if tenue <> "" and sex_points >= 50:
        add "Images/Personnages/nouveau/user/Tenue/[tenue]_X.png" xalign 0.0 yalign 1.0
    elif tenue <> "":
        add "Images/Personnages/nouveau/user/Tenue/[tenue].png" xalign 0.0 yalign 1.0
    add "Images/Personnages/nouveau/user/Bras/[bras]_D.png" xalign 0.0 yalign 1.0
    if position == "P" or position == "p":
        add "user_[exp]_talk" xalign 0.0 yalign 1.0
    elif position == "EX":
        add "Images/Personnages/nouveau/user/Expression/[exp]/2.png" xalign 0.0 yalign 1.0
    else:
        add "Images/Personnages/nouveau/user/Expression/[exp]/0.png" xalign 0.0 yalign 1.0
    if acc1 <> "":
        add "Images/Personnages/nouveau/user/Accessoire/[acc1].png" xalign 0.0 yalign 1.0
    if acc2 <> "":
        add "Images/Personnages/nouveau/user/Accessoire/[acc2].png" xalign 0.0 yalign 1.0
    if acc3 <> "":
        add "Images/Personnages/nouveau/user/Accessoire/[acc3].png" xalign 0.0 yalign 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
