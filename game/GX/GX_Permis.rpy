init:
    $ pos_car = 1
    $ pos_bad_car = 0
    $ time_car = 0
    $ cpt_car = 0

screen conduite(dest):
    if pos_bad_car == pos_car:
        $ warn_ville_points += 1
        button:
            add "Images/Mini-Jeux/Voiture/KO.png"
            action Jump("allee")
    elif time_car > 0:
        timer 1.0 repeat True action SetVariable("time_car", time_car - 1)
        if dest == "ville":
            add "Images/Mini-Jeux/Voiture/ville.png"
        else:
            add "Images/Mini-Jeux/Voiture/ciel.png"
        add "Images/Mini-Jeux/Voiture/route.png"

        if cpt_car == 1:
            if time_car == 25:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 24:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 23:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 22:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 21:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 20:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 19:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.35
            elif time_car == 18:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 17:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.45
            elif time_car == 16:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 15:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 14:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 13:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 12:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 11:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 10:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 9:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 8:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 7:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 6:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 5:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 4:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 3:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 2:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            else:
                $ pos_bad_car = 0
        elif cpt_car == 2:
            if time_car == 29:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.45
            elif time_car == 28:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 27:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 26:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 25:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.4 yalign 0.45
            elif time_car == 24:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.1 yalign 0.99
            elif time_car == 23:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 22:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 21:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 20:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 19:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 18:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 17:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 16:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 15:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 14:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 13:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.35
            elif time_car == 12:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 11:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.45
            elif time_car == 10:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 9:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 8:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 7:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 6:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 5:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.35
            elif time_car == 4:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 3:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.45
            elif time_car == 2:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            else:
                $ pos_bad_car = 0
        else:
            $ cpt_car = 0
            if time_car == 29:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 28:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 27:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 26:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 25:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.4 yalign 0.45
            elif time_car == 24:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.1 yalign 0.99
            elif time_car == 23:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.6 yalign 0.35
            elif time_car == 22:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.9 yalign 0.99
            elif time_car == 21:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 20:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 19:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.35
            elif time_car == 18:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            elif time_car == 17:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.45
            elif time_car == 16:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 15:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 14:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 13:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.4 yalign 0.45
            elif time_car == 12:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.1 yalign 0.99
            elif time_car == 11:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.6 yalign 0.35
            elif time_car == 10:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.9 yalign 0.99
            elif time_car == 9:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 8:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 7:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_3_2.png" xalign 0.6 yalign 0.35
            elif time_car == 6:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_3_1.png" xalign 0.9 yalign 0.99
            elif time_car == 4:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_2_2.png" xalign 0.6 yalign 0.35
            elif time_car == 3:
                $ pos_bad_car = 2
                add "Images/Mini-Jeux/Voiture/car_2_1.png" xalign 0.9 yalign 0.99
            elif time_car == 2:
                $ pos_bad_car = 0
                add "Images/Mini-Jeux/Voiture/car_1_2.png" xalign 0.4 yalign 0.45
            elif time_car == 1:
                $ pos_bad_car = 1
                add "Images/Mini-Jeux/Voiture/car_1_1.png" xalign 0.1 yalign 0.99
            else:
                $ pos_bad_car = 0

        if pos_bad_car == pos_car and pos_car == 1:
            add "Images/Mini-Jeux/Voiture/boom.png" xalign 0.1 yalign 0.99
        elif pos_bad_car == pos_car and pos_car == 2:
            add "Images/Mini-Jeux/Voiture/boom.png" xalign 0.9 yalign 0.99
        elif pos_car == 1:
            add "Images/Mini-Jeux/Voiture/vanzilla.png" xalign 0.1 yalign 0.99
            if renpy.variant("pc"):
                key "K_RIGHT" action SetVariable("pos_car", 2)
            elif renpy.variant("mobile"):
                button:
                    xalign 0.99
                    yalign 0.99
                    add "Images/Plans/Minis/flecheD_hover.png"
                    action SetVariable("pos_car", 2)
        elif pos_car == 2:
            add "Images/Mini-Jeux/Voiture/vanzilla.png" xalign 0.9 yalign 0.99
            if renpy.variant("pc"):
                key "K_LEFT" action SetVariable("pos_car", 1)
            elif renpy.variant("mobile"):
                button:
                    xalign 0.01
                    yalign 0.99
                    add "Images/Plans/Minis/flecheG_hover.png"
                    action SetVariable("pos_car", 1)
    else:
        button:
            add "Images/Mini-Jeux/Voiture/OK.png"
            if checkZone == "dmv_hall":
                action Jump("DMV_2")
            elif checkZone == "casagrande_out":
                action Jump("casagrande_ext")
            else:
                action Jump("map")

label quiz_auto:
    scene BG_back_wait
    with fondu
    $ permis_test_go = False
    $ rep_1 = False
    $ rep_2 = False
    $ rep_3 = False
    $ rep_4 = False

    nar "Ce quizz de 4 questions se base du code de la route en France."
    nar "Une seule bonne réponse à chaque fois"
    jump Q_Auto_1

screen QuizAuto(question, var, r1, f1, r2, f2, r3, f3, r4, f4, next):
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        add "Images/Mini-Jeux/Permis/permis_question.png" xalign 0.5
        label question xalign 0.5
        grid 2 2:
            xalign 0.5
            spacing 10
            frame:
                xalign 0.5
                textbutton r1:
                    action SetVariable(var, f1), Jump(next)
            frame:
                xalign 0.5
                textbutton r2:
                    action SetVariable(var, f2), Jump(next)
            if r3 == "" and f3 == "":
                null
            else:
                frame:
                    xalign 0.5
                    textbutton r3:
                        action SetVariable(var, f3), Jump(next)
            if r4 == "" and f4 == "":
                null
            else:
                frame:
                    xalign 0.5
                    textbutton r4:
                        action SetVariable(var, f4), Jump(next)

label Q_Auto_1:
    call screen QuizAuto(_("A quelle vitesse doit-on rouler en ville ?"),"rep_1",_("50 Km/h"),True,_("30 Km/h"),False,_("70 Km/h"),False,_("40 Km/h"),False,"Q_Auto_2")

label Q_Auto_2:
    call screen QuizAuto(_("A quoi servent les clignotants ?"),"rep_2",_("A signaler qu'on freîne"),False,_("A signaler qu'on tourne"),True,_("A faire \"Tic-Tac\""),False,_("A rien"),False,"Q_Auto_3")

label Q_Auto_3:
    call screen QuizAuto(_("Dans un carrefour giratoire, la priorité est à ..."),"rep_3",_("Droite"),False,_("Gauche"),True,_("Celui qui va le plus vite"),False,_("Toujours à moi !"),False,"Q_Auto_4")

label Q_Auto_4:
    call screen QuizAuto(_("La ceinture est-elle obligatoire ?"),"rep_4",_("Oui"),True,_("Non"),False,"","","","","Q_Auto_R")

label Q_Auto_R:
    if rep_1 == True and rep_2 == True and rep_3 == True and rep_4 == True:
        $ permis = True
        nar "Bravo, tu as le code. \n{w}Reste plus que la pratique !"

        jump pratique_auto
    elif True:
        nar "Dommage... Faut réviser !"
        jump DMV_2

label pratique_auto:
    $ time_car = 10
    $ cpt_car += 1
    call screen conduite("")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
