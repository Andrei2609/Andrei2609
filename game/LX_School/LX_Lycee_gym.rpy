
image user_school_sport_1 = "Images/CG/05-User/user_sport_1.png"

screen Gym():
    imagebutton:
        xalign 0.99
        yalign 0.5
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("hall")

    imagebutton:
        xalign 0.14
        yalign 0.5
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        action Jump("gym_vestiaire")

    imagebutton:
        xalign 0.51
        yalign 0.5
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        action Jump("gym_bureau_coach")

    imagebutton:
        xalign 0.3
        yalign 0.9
        idle "Images/Plans/Minis/strength.png"
        hover "Images/Plans/Minis/strength_hover.png"
        action Jump("gym")

label gym_in:
    $ checkZone = "gym"
    scene BG_lycee_gym_hall
    with fondu
    call screen Gym

label gym_vestiaire:
    menu:
        "Changer de tenue" if True:
            jump gym_user_tenue
        "Espionner les filles" if True:
            jump gym_girl_vestiaire

label gym_girl_vestiaire:
    if min >= 55:
        $ heure += 1
        $ min = 0
    elif True:
        $ min += 5
    $ sex_points += 10
    show screen peekGym("BG_standby")
    nar ""
    hide screen peekGym
    jump gym_in

label gym_user_tenue:
    call screen penderie
    jump user_tenue_verif_gym

label user_tenue_verif_gym:
    if tenue <> "sport":
        show screen User(tenue, "_P")
        user "Je peux pas faire sport comme ça !"
        hide screen User
        jump gym_user_tenue
    elif True:
        call screen Gym

label gym_bureau_coach:
    user "C'est fermé !"
    jump gym_in

label gym:
    scene BG_lycee_gym
    if heure < 15:
        if heure == 12:
            show screen User(tenue, "_P")
            with fondu
            user "C'est l'heure de manger, {w}\nPas étonnant qu'il n'y ait personne !"

            hide screen User
            with fondu
            jump gym_in
        elif jour == 2 and heure > 12 or jour == 4 and heure < 12:
            show coach_P at right
            with fondu
            if tenue <> "sport":
                coach "Lincoln, va te changer, tu vas pas faire sport comme ça !"
                jump gym_in
            coach "Lincoln, à ta place, le cours va commencer !"
            hide coach_P
            show user_school_sport_1
            with fondu
            nar ""
            if heure < 12:
                $ heure = 12
                $ min = 0
            elif heure == 13:
                $ heure = 15
                $ min = 0
            hide user_school_sport_1
            show screen User(tenue, "_P")
            with fondu
            if heure == 12:
                user "Pouah... J'ai trop faim ! {w}\nAllez, direction la cantine."
            elif True:

                user "Aaah... Une journée de cours finie ! {w}\nAllez, retour à la maison !"

            hide screen User
            with fondu
            jump gym_in
        elif True:
            show coach_P at right
            with fondu
            coach "Tu n'as pas cours ici !"
            hide coach_P
            jump gym_in
    elif True:
        show screen User(tenue, "_P")
        with fondu
        user "C'est fini la journée, faut rentrer !"
        hide screen User
        with fondu
        jump gym_in
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
