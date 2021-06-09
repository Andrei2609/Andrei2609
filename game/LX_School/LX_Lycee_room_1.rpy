label room_1:
    $ checkZone = "school_room_1"
    scene BG_classe_tableau
    if heure < 15:
        if heure == 12:
            show screen User(tenue, "_P")
            with fondu
            user "C'est l'heure de manger ! {w}\nPas étonnant qu'il n'y ait personne !"

            hide screen User
            with fondu
            jump hall
        elif jour == 1 and heure < 12 or jour == 4 and heure > 12 or jour == 5 and heure < 12:
            show prof1_P at right
            with fondu
            prof1 "Lincoln, à ta place, le cours va commencer !"
            hide prof1_P
            if heure < 12:
                $ heure = 12
                $ min = 0
            elif heure == 13:
                $ heure = 15
                $ min = 0
            show user_school_time_1
            with fondu
            nar ""
            hide user_school_time_1
            show user_school_time_2
            with trembleV
            pause 0.5
            hide user_school_time_2
            show jordan_chaise_1
            with fondu
            nar ""
            $ sex_points += 5
            hide jordan_chaise_1
            show user_school_time_3
            with fondu
            nar ""
            hide user_school_time_3
            with fondu
            if jour_Num == 0:
                jump prime_quest_go
            elif heure == 12:
                show screen User(tenue, "_P")
                user "Pouah... J'ai trop faim ! {w}\nAllez, direction la cantine."
            elif True:

                show screen User(tenue, "_P")
                user "Aaah... Une journée de cours finie ! {w}\nAllez, retour à la maison !"

            hide screen User
            with fondu
            jump hall
        elif jour == 2 and heure < 12 or jour == 5 and heure > 12:
            show prof2_P at right
            with fondu
            prof2 "Lincoln, à ta place, le cours va commencer !"
            hide prof2_P
            if heure < 12:
                $ heure = 12
                $ min = 0
            elif heure == 13:
                $ heure = 15
                $ min = 0
            show EF_school_cloche
            with fondu
            nar ""
            hide EF_school_cloche
            show screen User(tenue, "_P")
            with fondu
            if heure == 12:
                user "Pouah... J'ai trop faim ! {w}\nAllez, direction la cantine."
            elif True:

                user "Aaah... Une journée de cours finie ! {w}\nAllez, retour à la maison !"

            hide screen User
            with fondu
            jump hall
        elif True:
            show prof1_P at right
            with fondu
            prof1 "Tu n'as pas cours ici !"
            hide prof1_P
            jump hall
    elif True:
        show screen User(tenue, "_P")
        with fondu
        user "C'est fini la journée, faut rentrer !"
        hide screen User
        with fondu
        jump hall
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
