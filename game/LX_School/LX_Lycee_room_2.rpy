label room_2:
    $ checkZone = "school_room_2"
    scene BG_classe_tableau
    if heure < 15:
        if heure == 12:
            show screen User(tenue, "_P")
            with fondu
            user "C'est l'heure de manger ! {w}\nPas étonnant qu'il n'y ait personne !"

            hide screen User
            with fondu
            jump hall
        elif jour == 1 and heure > 12 or jour == 3 and heure < 12:
            show prof3_P at right
            with fondu
            prof3 "Lincoln, à ta place, le cours va commencer !"
            hide prof3_P
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
            show prof3_P at right
            with fondu
            prof3 "Tu n'as pas cours ici !"
            hide prof3_P
            jump hall
    elif True:
        show screen User(tenue, "_P")
        with fondu
        user "C'est fini la journée, faut rentrer !"
        hide screen User
        with fondu
        jump hall
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
