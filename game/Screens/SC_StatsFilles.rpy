screen boy_stats(id_num, nom, surnom, love, hate, age, love_pts, sex_pts):
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        hbox:
            xalign 0.5
            label "Fiche de" xalign 0.5 yalign 0.5
            label " [nom]" xalign 0.5 yalign 0.5
        hbox:
            spacing 5
            add "Images/Bases/Avatars/Av_[id_num].png" xalign 0.5 yalign 0
            vbox:
                hbox:
                    text "Alias "
                    text surnom
                text _("Il a [age] ans.")
                text "______________"
                hbox:
                    spacing 10
                    xalign 0.5
                    add "Images/Bases/Icones/aime.png" xalign 0.5
                    text ": " yalign 0.5
                    text love yalign 0.5
                hbox:
                    spacing 10
                    xalign 0.5
                    add "Images/Bases/Icones/not_aime.png" xalign 0.5
                    text ": " yalign 0.5
                    text hate yalign 0.5
        text ""
        text _("Affinité") xalign 0.0
        use girl_bar(_("Images/Bases/Icones/love.png"), love_pts, 250)
        text _("Excitation") xalign 0.0
        use girl_bar(_("Images/Bases/Icones/sex.png"), sex_pts, 250)
        text ""
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen girl_stats(id_num, win, nom, surnom, love, hate, age, love_pts, sex_pts, cum_pts):
    if cum_pts == "":
        $ cum_pts = 0
    frame:
        xalign 0.5
        yalign 0.5
        has hbox
        vbox:
            hbox:
                xalign 0.5
                label "Fiche de" xalign 0.5 yalign 0.5
                label " [nom]" xalign 0.5 yalign 0.5
            hbox:
                spacing 5
                if win == True:
                    add "Images/Bases/Avatars/Av_[id_num]_nue.png" xalign 0.5 yalign 0
                elif love_pts >= 90:
                    add "Images/Bases/Avatars/Av_[id_num]_4.png" xalign 0.5 yalign 0
                elif love_pts >= 70:
                    add "Images/Bases/Avatars/Av_[id_num]_3.png" xalign 0.5 yalign 0
                elif love_pts >= 50:
                    add "Images/Bases/Avatars/Av_[id_num]_2.png" xalign 0.5 yalign 0
                elif love_pts >= 40:
                    add "Images/Bases/Avatars/Av_[id_num]_1.png" xalign 0.5 yalign 0
                elif love_pts <= 0:
                    add "Images/Bases/Avatars/Av_[id_num]_KO.png" xalign 0.5 yalign 0
                else:
                    add "Images/Bases/Avatars/Av_[id_num].png" xalign 0.5 yalign 0
                vbox:
                    hbox:
                        text "Alias "
                        text surnom
                    text _("Elle a [age] ans.")
                    text "______________"
                    hbox:
                        spacing 10
                        xalign 0.5
                        add "Images/Bases/Icones/aime.png" xalign 0.5
                        text ": " yalign 0.5
                        text love yalign 0.5
                    hbox:
                        spacing 10
                        xalign 0.5
                        add "Images/Bases/Icones/not_aime.png" xalign 0.5
                        text ": " yalign 0.5
                        text hate yalign 0.5
                    hbox:
                        spacing 2
                        xalign 0.5
                        if cum_pts >= 5:
                            add "Images/Bases/i_love_cum.png" xalign 0.5
                        if win >= True:
                            add "Images/Bases/win_panty.png" xalign 0.5
                    if id_num <> "l2":
                        label _("Personnage en attente de mise à jour")
        vbox:
            spacing 1
            xalign 0.5
            frame:
                xalign 0.5
                has vbox:
                    spacing 1
                    xalign 0.5
                label _("Statistiques") xalign 0.5
                text _("Affinité") xalign 0.0
                use girl_bar(_("Images/Bases/Icones/love.png"), love_pts, 250)
                text _("Excitation") xalign 0.0
                use girl_bar(_("Images/Bases/Icones/sex.png"), sex_pts, 250)
            imagebutton:
                xalign 0.99
                yalign 0.99
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action Return(True)

screen girl_menu(nom, talk, stats):
    zorder 100
    frame:
        xalign 0.3
        yalign 0.4
        has vbox
        hbox:
            if vie_points > 0:
                vbox:
                    imagebutton:
                        xalign 0.5
                        idle "Images/Bases/Icones/talk.png"
                        hover "Images/Bases/Icones/talk_hover.png"
                        action ShowMenu(talk)
                    label _("Discuter") xalign 0.5
            vbox:
                imagebutton:
                    xalign 0.5
                    idle "Images/Bases/Icones/profil.png"
                    hover "Images/Bases/Icones/profil_hover.png"
                    action ShowMenu(stats)
                label nom xalign 0.5

screen mini_girl_stat(nom, girlmenu, love, sex):
    button:
        frame:
            hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
            has hbox:
                spacing 5
            add "Images/Bases/Icones/Faces/face_[nom].png" xalign 0.5
            vbox:
                if nom == "mom":
                    label "rita"
                elif nom == "l1":
                    label "lori"
                elif nom == "l2":
                    label "leni"
                elif nom == "l3":
                    label "luna"
                elif nom == "l4":
                    label "luan"
                elif nom == "l5":
                    label "lynn jr"
                elif nom == "ronnie":
                    label "ronnie ann"
                elif nom == "prof1":
                    label "madame johnson"
                elif nom == "prof2":
                    label "madame dimartino"
                elif nom == "prof3":
                    label "madame shrinivas"
                elif nom == "nurse":
                    label "l'infirmière patty"
                elif nom == "shop_girl_1":
                    label "la caissière"
                elif nom == "electro_girl":
                    label "vera"
                elif nom == "BD_girl":
                    label "wendy"
                elif nom == "candy_girl":
                    label "candice"
                else:
                    label "[nom]"
                use girl_bar(_("Images/Bases/Icones/love.png"), love, 150)
                use girl_bar(_("Images/Bases/Icones/sex.png"), sex, 150)
        action ShowMenu(girlmenu)

screen Filles_Loud():
    frame:
        xalign 0.5 ypos 50 xsize 1000
        has vbox:
            xalign 0.5
        label _("Statistique des Filles Loud") xalign 0.5
        grid 3 2:
            spacing 5

            use mini_girl_stat("mom", "mom_menu_stats", love_mom_points, sex_mom_points)

            use mini_girl_stat("l1", "l1_menu_stats", love_l1_points, sex_l1_points)

            use mini_girl_stat("l2", "l2_menu_stats", love_l2_points, sex_l2_points)

            use mini_girl_stat("l3", "l3_menu_stats", love_l3_points, sex_l3_points)

            use mini_girl_stat("l4", "l4_menu_stats", love_l4_points, sex_l4_points)

            use mini_girl_stat("l5", "l5_menu_stats", love_l5_points, sex_l5_points)
        hbox:
            xalign 0.5
            xsize 800
            vbox:
                xalign 0.0
                text _("Méfiance") xalign 0.0
                use girl_bar(_("Images/Bases/Icones/warn.png"), warn_loud_points, 250)
            imagebutton:
                xalign 1.0
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action Return(True)

screen Filles_School():
    frame:
        xalign 0.5 ypos 50 xsize 600
        has vbox:
            xalign 0.5
        label _("Statistique des Filles du Lycée") xalign 0.5
        hbox:
            xalign 0.5
            spacing 30
            vbox:
                imagebutton:
                    xalign 0.5
                    idle "Images/Bases/Icones/fille_school.png"
                    hover "Images/Bases/Icones/fille_school_hover.png"
                    action ShowMenu("Filles_School_Prof")
                text _("Professeures") xalign 0.5
            vbox:
                imagebutton:
                    xalign 0.5
                    idle "Images/Bases/Icones/fille_school.png"
                    hover "Images/Bases/Icones/fille_school_hover.png"

                    action ShowMenu("Filles_School_Ado")
                text _("Lycéennes") xalign 0.5
        hbox:
            xalign 0.5
            xsize 500
            vbox:
                xalign 0.0
                text _("Méfiance") xalign 0.0
                use girl_bar(_("Images/Bases/Icones/warn.png"), warn_school_points, 250)
            imagebutton:
                xalign 1.0
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action Return(True)

screen Filles_School_Prof():
    modal True
    frame:
        xalign 0.5 ypos 50 xsize 1000
        has vbox:
            xalign 0.5
        label _("Statistique des Professeures du Lycée") xalign 0.5
        grid 3 2:
            spacing 5

            use mini_girl_stat("prof1", "prof1_menu_stats", love_prof1_points, sex_prof1_points)

            use mini_girl_stat("prof2", "prof2_menu_stats", love_prof2_points, sex_prof2_points)

            use mini_girl_stat("prof3", "prof3_menu_stats", love_prof3_points, sex_prof3_points)

            use mini_girl_stat("nurse", "nurse_menu_stats", love_nurse_points, sex_nurse_points)
            null
            null
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen Filles_School_Ado():
    modal True
    frame:
        xalign 0.5 ypos 50 xsize 1000
        has vbox:
            xalign 0.5
        label _("Statistique des Lycéennes") xalign 0.5
        grid 3 2:
            spacing 5

            use mini_girl_stat("cristina", "cristina_menu_stats", love_cristina_points, sex_cristina_points)

            use mini_girl_stat("stella", "stella_menu_stats", love_stella_points, sex_stella_points)

            use mini_girl_stat("jordan", "jordan_menu_stats", love_jordan_points, sex_jordan_points)

            use mini_girl_stat("joy", "joy_menu_stats", love_joy_points, sex_joy_points)

            use mini_girl_stat("mollie", "mollie_menu_stats", love_mollie_points, sex_mollie_points)

            use mini_girl_stat("paige", "paige_menu_stats", love_paige_points, sex_paige_points)
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen Filles_Ville():
    frame:
        xalign 0.5 ypos 50 xsize 600
        has vbox:
            xalign 0.5
        label _("Statistique des Filles de la Ville") xalign 0.5
        hbox:
            xalign 0.5
            spacing 30
            vbox:
                imagebutton:
                    xalign 0.5
                    idle "Images/Bases/Icones/fille_ville.png"
                    hover "Images/Bases/Icones/fille_ville_hover.png"
                    action ShowMenu("Filles_Adulte")
                text _("Femmes Matures") xalign 0.5
            vbox:
                imagebutton:
                    xalign 0.5
                    idle "Images/Bases/Icones/fille_ville.png"
                    hover "Images/Bases/Icones/fille_ville_hover.png"
                    action ShowMenu("Filles_Ado")
                text _("Jeunes Femmes") xalign 0.5
        hbox:
            xalign 0.5
            xsize 500
            vbox:
                xalign 0.0
                text _("Méfiance") xalign 0.0
                use girl_bar(_("Images/Bases/Icones/warn.png"), warn_ville_points, 250)
            imagebutton:
                xalign 1.0
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action Return(True)

screen Filles_Adulte():
    frame:
        xalign 0.5 ypos 50 xsize 1000
        has vbox:
            xalign 0.5
        label _("Statistique des Femmes Matures de Royal Wood") xalign 0.5
        grid 2 1:
            spacing 5

            use mini_girl_stat("maria", "maria_menu_stats", love_maria_points, sex_maria_points)

            use mini_girl_stat("journaliste", "journaliste_menu_stats", love_journaliste_points, sex_journaliste_points)
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen Filles_Ado():
    frame:
        xalign 0.5 ypos 50 xsize 1000
        has vbox:
            xalign 0.5
        label _("Statistique des Jeunes Femmes de Royal Wood") xalign 0.5
        grid 2 1:
            spacing 5

            use mini_girl_stat("carol", "carol_menu_stats", love_carol_points, sex_carol_points)

            use mini_girl_stat("sam", "sam_menu_stats", love_sam_points, sex_sam_points)
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen girl_bar(logo, pts, taille):
    hbox:
        spacing 5
        xalign 0.5
        yalign 0.5
        add logo yalign 0.5
        bar value AnimatedValue(pts, 100, 0.5) style "bar" xsize taille yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
