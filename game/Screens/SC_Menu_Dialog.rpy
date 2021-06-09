screen bouton_nue():
    vbox:
        spacing 2
        label _("Imaginer") yalign 1.0
        hbox:
            spacing 1
            if slipGO == False:
                button:
                    yalign 0.5
                    frame:
                        xsize 200
                        ysize 50
                        hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                        text _("en slip") xalign 0.5 yalign 0.5
                    action SetVariable("slipGO", True)
            elif slipGO == True:
                button:
                    yalign 0.5
                    frame:
                        xsize 200
                        ysize 50
                        hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                        text _("Arrêter") xalign 0.5 yalign 0.5
                    action SetVariable("slipGO", False), SetVariable("nakedGO", False)
            if nakedGO == False and slipGO == True:
                button:
                    yalign 0.5
                    frame:
                        xsize 200
                        ysize 50
                        hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                        text _("nue") xalign 0.5 yalign 0.5
                    action SetVariable("nakedGO", True)
            elif nakedGO == True:
                button:
                    yalign 0.5
                    frame:
                        xsize 200
                        ysize 50
                        hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                        text _("Arrêter") xalign 0.5 yalign 0.5
                    action SetVariable("nakedGO", False)

screen menu_shop_talk(nom, love, sex, discut, shop, retour):
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        label _("Actions") xalign 0.5
        hbox:
            xalign 0.5
            yalign 0.5
            use talkButton("courses", nom, love, sex, "", _("Acheter"), shop)
            use talkButton("talk", nom, love, sex, "", _("Discuter"), discut)
            if tissu_leni_1 == "vide" and nom == fiona:
                use talkButton("tissu", nom, love, sex, _("Voir pour"), _("du tissu"), "tissu_quete_shop")
        hbox:
            spacing 50
            imagebutton:
                xalign 0.01
                yalign 0.99
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action SetVariable("nakedGO", False), SetVariable("slipGO", False), Jump(retour)
            use bouton_nue

screen menu_talk(nom, love, sex, stat):
    frame:
        xalign 0.1
        yalign 0.5
        has vbox
        label _("Discution") xalign 0.5
        if nom <> mom and nom <> l1 and nom <> l2 and nom <> l3 and nom <> l4 and nom <> l5:
            label _("Non disponible")
        else:
            grid 5 2:
                xalign 0.5
                yalign 0.5
                use talkButton("talk", nom, love, sex, "", _("Discuter"), "talk_1")
                if love >= 20:
                    if nom == mom:
                        use talkButton("livre", nom, love, sex, _("Discuter de"), _("son livre"), "talk_2")
                    elif nom == l1:
                        use talkButton("bobby", nom, love, sex, _("Discuter de"), _("Bobby"), "talk_2")
                    elif nom == l2:
                        use talkButton("mode", nom, love, sex, _("Discuter de"), _("Mode"), "talk_2")
                    elif nom == l3:
                        use talkButton("talk", nom, love, sex, _("Discuter de"), _("musique"), "talk_2")
                    elif nom == l4:
                        use talkButton("talk", nom, love, sex, _("Faire une"), _("blague"), "talk_2")
                    elif nom == l5:
                        use talkButton("sport", nom, love, sex, _("Discuter de"), _("sport"), "talk_2")
                    elif nom == ronnie:
                        use talkButton("jeux", nom, love, sex, _("Discuter de"), _("jeux vidéos"), "talk_2")
                else:
                    use talkButtonOFF
                if love >= 50:
                    use talkButton("flirt", nom, love, sex, "", _("Flirter"), "talk_3")
                else:
                    use talkButtonOFF
                if nom == l2:
                    use talkButton("gift", nom, love, sex, _("Offrir"), _("cadeau"), "gift")
                else:
                    use talkButtonOFF
                if love >= 80:
                    use talkButton("sexe", nom, love, sex, _("Discuter de"), _("sexe"), "talk_4")
                else:
                    use talkButtonOFF
                if nom == mom:
                    use talkButton("talk", nom, love, sex, _("Demander"), _("conseil"), "talk_5")
                    use talkButton("argent", nom, love, sex, _("Argent"), _("de poche"), "talk_6")
                    use talkButton("service", nom, love, sex, "", _("Service"), "talk_7")
                elif nom == ronnie and ronnie_tel == False:
                    use talkButton("tel", nom, love, sex, _("Demander"), _("son tel"), "talk_TEL")
                    use talkButtonOFF
                    use talkButtonOFF
                else:
                    use talkButtonOFF
                    use talkButtonOFF
                    use talkButtonOFF
                use actionButton("service", nom, love, sex, "", _("Activité"), "menu_act")
                if love >= 80 and nom <> l2:
                    use actionButton("rdv", nom, love, sex, "", _("RDV"), "menu_rdv")
                else:
                    use talkButtonOFF
        hbox:
            spacing 50
            imagebutton:
                xalign 0.01
                yalign 0.99
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action SetVariable("nakedGO", False), SetVariable("slipGO", False), Return(True)
            use bouton_nue
            button:
                yalign 0.5
                frame:
                    xsize 250
                    ysize 50
                    hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                    text _("Informations") xalign 0.5 yalign 0.5
                action ShowMenu(stat)

screen menu_act():
    modal True
    frame:
        xalign 0.2
        yalign 0.4
        has vbox
        label _("Activités") xalign 0.5
        grid 2 2:
            use talkButton("jeux", talkCible, loveCible, sexCible, "", _("Jeu Vidéo"), "JV")
            use talkButton("talk", talkCible, loveCible, sexCible, _("Boite"), _("Mystère"), "BM")
            if talkCible == l2:
                use talkButton("mode", talkCible, loveCible, sexCible, _("Essayer des"), _("vêtements"), "l2_vetHome")
            else:
                use talkButtonOFF
            use talkButton("flirt", talkCible, loveCible, sexCible, "", _("Baiser"), "fucktime")
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen menu_rdv():
    modal True
    frame:
        xalign 0.2
        yalign 0.4
        has vbox
        label _("Rendez-vous") xalign 0.5
        grid 4 1:
            use talkButton("talk", talkCible, loveCible, sexCible, _("Allez à"), _("la plage"), "rdv_plage")
            use talkButton("talk", talkCible, loveCible, sexCible, _("Allez au"), _("parc"), "rdv_parc")
            use talkButton("talk", talkCible, loveCible, sexCible, _("Allez au"), _("magasin"), "rdv_mall")
            use talkButton("talk", talkCible, loveCible, sexCible, _("Allez au"), _("cinéma"), "rdv_cinema")
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Return(True)

screen talkButton(img, nom, love, sex, t1, t2, url):
    button:
        xalign 0.5
        yalign 0.5
        frame:
            xsize 150
            ysize 150
            hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
            has vbox:
                xalign 0.5
                yalign 0.5
            if t1 <> "":
                text t1 xalign 0.5
            add "Images/Bases/Icones/Discutions/[img].png" xalign 0.5
            if t2 <> "":
                text t2 xalign 0.5
        action SetVariable("talkCible", nom), SetVariable("loveCible", love), SetVariable("sexCible", sex), Jump(url)

screen actionButton(img, nom, love, sex, t1, t2, url):
    button:
        xalign 0.5
        yalign 0.5
        frame:
            xsize 150
            ysize 150
            hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
            has vbox:
                xalign 0.5
                yalign 0.5
            if t1 <> "":
                text t1 xalign 0.5
            add "Images/Bases/Icones/Discutions/[img].png" xalign 0.5
            if t2 <> "":
                text t2 xalign 0.5
        action SetVariable("talkCible", nom), SetVariable("loveCible", love), SetVariable("sexCible", sex), ShowMenu(url)

screen talkButtonOFF():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 150
        ysize 150
        background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
