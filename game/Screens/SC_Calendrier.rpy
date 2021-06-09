label calendrier:
    call screen Calendrier()

screen Calendrier():
    zorder 200
    frame:
        xalign 0.5
        has vbox
        label _("Agenda") xalign 0.5
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            textbutton _("été"):
                action SetVariable("choix_saison", "ete"), Jump("calendrier")
            text "|"
            textbutton _("hiver"):
                action SetVariable("choix_saison", "hiver"), Jump("calendrier")
            text "|"
            textbutton _("vacances"):
                action SetVariable("choix_saison", "vacances"), Jump("calendrier")
        hbox:
            spacing 20
            grid 2 4:
                spacing 10
                xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_retour.png"
                        hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                        if user_room == True:
                            action SetVariable("choix_calendrier", "neutre"), Jump("cham_user")
                        else:
                            action SetVariable("choix_calendrier", "neutre"), Return(True)
                    text _("Retour") xalign 0.5
                vbox:
                    if choix_saison == "vacances":
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            idle "Images/Bases/Icones/Faces/face_user.png"
                            hover "Images/Bases/Icones/Faces/face_user_hover.png"
                            action SetVariable("choix_calendrier", "ecole"), Jump("calendrier")
                        text _("Perso") xalign 0.5
                    else:
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            idle "Images/Bases/Icones/Faces/face_school.png"
                            hover "Images/Bases/Icones/Faces/face_school_hover.png"
                            action SetVariable("choix_calendrier", "ecole"), Jump("calendrier")
                        text _("Scolaire") xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_mom.png"
                        hover "Images/Bases/Icones/Faces/face_mom_hover.png"
                        action SetVariable("choix_calendrier", "mom"), Jump("calendrier")
                    text _("Rita") xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_l1.png"
                        hover "Images/Bases/Icones/Faces/face_l1_hover.png"
                        action SetVariable("choix_calendrier", "l1"), Jump("calendrier")
                    text _("Lori") xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_l2.png"
                        hover "Images/Bases/Icones/Faces/face_l2_hover.png"
                        action SetVariable("choix_calendrier", "l2"), Jump("calendrier")
                    text _("Leni") xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_l3.png"
                        hover "Images/Bases/Icones/Faces/face_l3_hover.png"
                        action SetVariable("choix_calendrier", "l3"), Jump("calendrier")
                    text _("Luna") xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_l4.png"
                        hover "Images/Bases/Icones/Faces/face_l4_hover.png"
                        action SetVariable("choix_calendrier", "l4"), Jump("calendrier")
                    text _("Luan") xalign 0.5
                vbox:
                    imagebutton:
                        xalign 0.5
                        yalign 0.5
                        idle "Images/Bases/Icones/Faces/face_l5.png"
                        hover "Images/Bases/Icones/Faces/face_l5_hover.png"
                        action SetVariable("choix_calendrier", "l5"), Jump("calendrier")
                    text _("Lynn") xalign 0.5
            vbox:
                ysize 400
                spacing 10
                if choix_calendrier <> "neutre":
                    frame:
                        xalign 0.5
                        xpadding 10
                        has hbox
                        if choix_calendrier == "ecole":
                            add "Images/Bases/Icones/Faces/face_user.png" xalign 0.5
                        elif choix_calendrier == "mom":
                            add "Images/Bases/Icones/Faces/face_mom.png" xalign 0.5
                        elif choix_calendrier == "l1":
                            add "Images/Bases/Icones/Faces/face_l1.png" xalign 0.5
                        elif choix_calendrier == "l2":
                            add "Images/Bases/Icones/Faces/face_l2.png" xalign 0.5
                        elif choix_calendrier == "l3":
                            add "Images/Bases/Icones/Faces/face_l3.png" xalign 0.5
                        elif choix_calendrier == "l4":
                            add "Images/Bases/Icones/Faces/face_l4.png" xalign 0.5
                        elif choix_calendrier == "l5":
                            add "Images/Bases/Icones/Faces/face_l5.png" xalign 0.5
                        vbox:
                            hbox:
                                xalign 0.5
                                textbutton _("Lundi"):
                                    xalign 0.5
                                    yalign 0.5
                                    action SetVariable("choix_jour", 1), Jump("calendrier")
                                text "|" yalign 0.5
                                textbutton _("Mardi"):
                                    xalign 0.5
                                    yalign 0.5
                                    action SetVariable("choix_jour", 2), Jump("calendrier")
                                text "|" yalign 0.5
                                textbutton _("Mercredi"):
                                    xalign 0.5
                                    yalign 0.5
                                    action SetVariable("choix_jour", 3), Jump("calendrier")
                                text "|" yalign 0.5
                                textbutton _("Jeudi"):
                                    xalign 0.5
                                    yalign 0.5
                                    action SetVariable("choix_jour", 4), Jump("calendrier")
                            hbox:
                                xalign 0.5
                                textbutton _("Vendredi"):
                                    xalign 0.5
                                    yalign 0.5
                                    action SetVariable("choix_jour", 5), Jump("calendrier")
                                text "|" yalign 0.5
                                if choix_calendrier <> "ecole" or choix_saison == "vacances":
                                    textbutton _("Samedi"):
                                        xalign 0.5
                                        yalign 0.5
                                        action SetVariable("choix_jour", 6), Jump("calendrier")
                                    text "|" yalign 0.5
                                    textbutton _("Dimanche"):
                                        xalign 0.5
                                        yalign 0.5
                                        action SetVariable("choix_jour", 7), Jump("calendrier")
                    hbox:
                        xalign 0.0
                        yalign 0.5
                        xsize 550
                        vbox:
                            textbutton _("Matin"):
                                xalign 0.5
                                action SetVariable("choix_periode", "matin"), Jump("calendrier")
                            textbutton _("Après-Midi"):
                                xalign 0.5
                                action SetVariable("choix_periode", "apresmidi"), Jump("calendrier")
                            if choix_calendrier <> "ecole" or choix_saison == "vacances":
                                textbutton _("Soir"):
                                    xalign 0.5
                                    action SetVariable("choix_periode", "soir"), Jump("calendrier")
                        if choix_calendrier == "ecole":
                            if choix_saison == "ete":
                                use Agenda_Ecole
                            elif choix_saison == "hiver":
                                use Agenda_Noel
                            elif choix_saison == "vacances":
                                use Agenda_Vacances
                        elif choix_calendrier == "mom":
                            if choix_saison == "ete":
                                use planning_mom
                            elif choix_saison == "hiver":
                                use planning_mom_noel
                            elif choix_saison == "vacances":
                                use planning_mom_vacances
                        elif choix_calendrier == "l1":
                            if choix_saison == "ete":
                                use planning_l1
                            elif choix_saison == "hiver":
                                use planning_l1_noel
                            elif choix_saison == "vacances":
                                use planning_l1_vacances
                        elif choix_calendrier == "l2":
                            if choix_saison == "ete":
                                use planning_l2
                            elif choix_saison == "hiver":
                                use planning_l2_noel
                            elif choix_saison == "vacances":
                                use planning_l2_vacances
                        elif choix_calendrier == "l3":
                            if choix_saison == "ete":
                                use planning_l3
                            elif choix_saison == "hiver":
                                use planning_l3_noel
                            elif choix_saison == "vacances":
                                use planning_l3_vacances
                        elif choix_calendrier == "l4":
                            if choix_saison == "ete":
                                use planning_l4
                            elif choix_saison == "hiver":
                                use planning_l4_noel
                            elif choix_saison == "vacances":
                                use planning_l4_vacances
                        elif choix_calendrier == "l5":
                            if choix_saison == "ete":
                                use planning_l5
                            elif choix_saison == "hiver":
                                use planning_l5_noel
                            elif choix_saison == "vacances":
                                use planning_l5_vacances
                else:
                    label _("Choisi") xalign 0.5 yalign 0.5

screen agendaJour(repasChoix, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5):
    frame:
        xalign 0.5
        xpadding 20
        ypadding 10
        has vbox
        if choix_jour == 1:
            label _("Lundi") xalign 0.5
        elif choix_jour == 2:
            label _("Mardi") xalign 0.5
        elif choix_jour == 3:
            label _("Mercredi") xalign 0.5
        elif choix_jour == 4:
            label _("Jeudi") xalign 0.5
        elif choix_jour == 5:
            label _("Vendredi") xalign 0.5
        elif choix_jour == 6:
            label _("Samedi") xalign 0.5
        elif choix_jour == 7:
            label _("Dimanche") xalign 0.5
        text "---------------------" xalign 0.5
        if choix_periode == "matin":
            vbox:
                if a1 <> "":
                    hbox:
                        label "7h - "
                        text a1
                if a2 <> "":
                    hbox:
                        label "8h - "
                        text a2
                if a3 <> "":
                    hbox:
                        label "9h - "
                        text a3
                if a4 <> "":
                    hbox:
                        label "10h - "
                        text a4
                if a5 <> "":
                    hbox:
                        label "11h - "
                        text a5
                hbox:
                    label "12h - "
                    if repasChoix == 1:
                        text _("Déjeuner à la cantine")
                    elif repasChoix == 2:
                        text _("Déjeuner à la cantine\nou à la maison")
                    else:
                        text _("Déjeuner à la maison")
        elif choix_periode == "apresmidi":
            vbox:
                if b1 <> "":
                    hbox:
                        label "13h - "
                        text b1
                if b2 <> "":
                    hbox:
                        label "14h - "
                        text b2
                if b3 <> "":
                    hbox:
                        label "15h - "
                        text b3
                if b4 <> "":
                    hbox:
                        label "16h - "
                        text b4
                if b5 <> "":
                    hbox:
                        label "17h - "
                        text b5
                if b6 <> "":
                    hbox:
                        label "18h - "
                        text b6
                if choix_calendrier <> "ecole" or choix_saison == "vacances":
                    hbox:
                        label "19h - "
                        text _("Repas en famille")
        elif choix_periode == "soir":
            vbox:
                if c1 <> "":
                    hbox:
                        label "20h - "
                        text c1
                if c2 <> "":
                    hbox:
                        label "21h - "
                        text c2
                if c3 <> "":
                    hbox:
                        label "22h - "
                        text c3
                if c4 <> "":
                    hbox:
                        label "23h - "
                        text c4
                if c5 <> "":
                    hbox:
                        label "01h - "
                        text c5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
