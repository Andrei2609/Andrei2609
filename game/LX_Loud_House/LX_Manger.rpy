screen SalleAManger():
    imagebutton:
        xalign 0.009
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("entree")

    imagebutton:
        xalign 0.298
        yalign 0.0
        idle "Images/Plans/Salle_a_Manger/cuisine.png"
        hover "Images/Plans/Salle_a_Manger/cuisine_hover.png"
        action Jump("cuisine")

    if heure == 12 or heure == 19 or heure == 10 and jour > 5:
        imagebutton:
            xalign 0.5
            yalign 0.53
            idle "Images/Plans/Salle_a_Manger/manger.png"
            hover "Images/Plans/Salle_a_Manger/manger_hover.png"
            action Jump("diner")

        imagebutton:
            xalign 0.8
            yalign 0.175
            idle "Images/Plans/Salle_a_Manger/l2.png"
            hover "Images/Plans/Salle_a_Manger/l2_hover.png"
            action Jump("diningroom_l2")

    if heure < 8 and luan_peek_1 == False:
        imagebutton:
            xalign 0.5
            yalign 0.55
            idle "Images/Plans/Minis/peek.png"
            hover "Images/Plans/Minis/peek_hover.png"
            action Jump("l4_table_1")

    if heure == 10 and jour >= 6:
        imagebutton:
            xalign 0.8
            yalign 0.175
            idle "Images/Plans/Salle_a_Manger/l2_sleep.png"
            hover "Images/Plans/Salle_a_Manger/l2_sleep_hover.png"
            action Jump("diningroom_l2_matin")

label Diningroom:
    $ checkZone = "manger"
    scene BG_manger
    with fondu
    call screen SalleAManger

label diner:
    call timer (1, 0) from _call_timer_45
    if vie_points >= 50:
        $ vie_points = 100
    elif True:
        $ vie_points += 50
    if school_OK == False and jour < 6:
        show mom_no_school
        with fondu
        mom "Lincoln ! Pourquoi n'es tu pas allé en cours aujourd'hui !?"
        $ love_mom_points -= 5
        hide mom_no_school
        show eat_user_home
        show miam_bol_1
        with fondu
        nar "Après une longue engueulade de votre mère sur votre comportement, vous mangez en famille"
        hide eat_user_home
        hide miam_bol_1
        jump Diningroom
    elif True:
        show eat_user_home
        show miam_bol_1
        with fondu
        nar "Vous mangez en famille"
        hide eat_user_home
        hide miam_bol_1
        jump Diningroom

label diningroom_l2_matin:
    show screen Actor1("l2", "nue", "normal", "sb_1", "sh_0", "sleep", "", "", "", "Neutre", "P")
    with fondu
    l2 "Tu veux manger quelque chose ?"
    show screen Actor1("l2", "nue", "normal", "sb_1", "sh_0", "sleep", "", "", "", "Neutre", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    jump Diningroom

label diningroom_l2:
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "P")
    with fondu
    l2 "Tu veux manger quelque chose ?"
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    jump Diningroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
