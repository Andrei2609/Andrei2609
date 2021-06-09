
image BG_plage = "Images/Backgrounds/plage.png"

image user_swimming = "Images/CG/05-User/user_swim.png"
image user_bronze = "Images/CG/05-User/user_bronze.png"

image girl_1 = "Images/CG/02-Lieux/Plage/girl_1.png"
image girl_2 = "Images/CG/02-Lieux/Plage/girl_2.png"
image girl_3 = "Images/CG/02-Lieux/Plage/girl_3.png"
image girl_4 = "Images/CG/02-Lieux/Plage/girl_4.png"
image girl_4A = "Images/CG/02-Lieux/Plage/girl_4A.png"

screen plage():
    if jour == 7 and heure >= 15 and heure < 17:
        imagebutton:
            xalign 0.2
            yalign 0.6
            idle "Images/Plans/Plage/l2.png"
            hover "Images/Plans/Plage/l2_hover.png"
            action Jump("plage_l2")

    if jour == 6 and heure >= 10 and heure < 12 or jour == 7 and heure >= 13 and heure < 16:
        imagebutton:
            xalign 0.95
            yalign 0.8
            idle "Images/Plans/Plage/girl_1.png"
            hover "Images/Plans/Plage/girl_1_hover.png"
            action Jump("plage_g1")

    if jour == 6 and heure >= 12 and heure < 17 or jour == 7 and heure >= 9 and heure < 11:
        imagebutton:
            xalign 0.6
            yalign 0.95
            idle "Images/Plans/Plage/girl_3.png"
            hover "Images/Plans/Plage/girl_3_hover.png"
            action Jump("plage_g3")

    if jour == 6 and heure >= 12 and heure < 15 or jour == 7 and heure >= 14 and heure < 15:
        imagebutton:
            xalign 0.15
            yalign 0.95
            idle "Images/Plans/Plage/girl_4.png"
            hover "Images/Plans/Plage/girl_4_hover.png"
            action Jump("plage_g4")

    if jour == 6 and heure >= 13 and heure < 15 or jour == 7 and heure >= 9 and heure < 11:
        imagebutton:
            xalign 0.3
            yalign 0.98
            idle "Images/Plans/Plage/girl_2.png"
            hover "Images/Plans/Plage/girl_2_hover.png"
            action Jump("plage_g2")

    imagebutton:
        xalign 0.7
        yalign 0.65
        idle "Images/Plans/Minis/strength.png"
        hover "Images/Plans/Minis/strength_hover.png"
        action Jump("exo_plage")

    imagebutton:
        xalign 0.009
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("map")

label plage:
    call timer (1, 0) from _call_timer_33
    scene BG_plage
    with fondu
    jump plage_2

label plage_2:
    $ checkZone = "plage"
    scene BG_plage
    with fondu
    call screen plage

label plage_g1:
    show girl_1
    with fondu
    nar ""
    hide girl_1
    call screen plage

label plage_g2:
    show girl_2
    with fondu
    nar ""
    hide girl_2
    call screen plage

label plage_g3:
    show girl_3
    with fondu
    nar ""
    hide girl_3
    call screen plage

label plage_g4:
    if plage_g4_compt < 2:
        $ plage_g4_compt += 1
        show girl_4
        with fondu
        nar ""
        hide girl_4
    elif True:
        $ plage_g4_compt = 0
        show girl_4A
        with trembleV
        nar ""
        hide girl_4A
    call screen plage

label exo_plage:
    if vie_points >= 10:
        if tenue == "swim":
            $ vie_points -= 10
            $ force_points += 1
            user "Un peu d'exercice pour me mettre en forme !"
            show user_swimming
            with fondu
            nar ""
            hide user_swimming
            show user_bronze
            with fondu
            nar ""
            hide user_bronze
            call timer (0, 30) from _call_timer_34
        elif True:
            user "Je ne peux pas nagé habiller comme ça !"
    elif True:
        user "Trop fatigué pour ça..."
    jump plage_2

label plage_l2:
    show screen Actor1("l2", "nue", "normal", "", "", "swim", "swim", "boucle_1", "", "Neutre", "P")
    with fondu
    l2 "Salut Lincoln"
    show screen Actor1("l2", "nue", "normal", "", "", "swim", "swim", "boucle_1", "", "Neutre", "")
    call screen l2_talk
    hide screen Actor1
    jump plage_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
