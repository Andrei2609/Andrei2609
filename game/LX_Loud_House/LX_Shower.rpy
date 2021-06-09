screen salleDeBain(actor1):
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "Images/Plans/Salle_de_Bain/porte.png"
        hover "Images/Plans/Salle_de_Bain/porte_hover.png"
        action Jump("exit_shower")

    imagebutton:
        xalign 0.31
        yalign 0.0
        idle "Images/Plans/Salle_de_Bain/bain.png"
        hover "Images/Plans/Salle_de_Bain/bain_hover.png"
        action Jump("baignoire")

    imagebutton:
        xalign 0.794
        yalign 0.468
        idle "Images/Plans/Salle_de_Bain/WC.png"
        hover "Images/Plans/Salle_de_Bain/WC_hover.png"
        action Jump("wc_use")

    if actor1 == "l2":
        imagebutton:
            xalign 0.2
            yalign 0.6
            idle "Images/Plans/Salle_de_Bain/l2.png"
            hover "Images/Plans/Salle_de_Bain/l2_hover.png"
            action Jump("shower_l2")

label shower:
    call screen porte_cham("shower_in", "peek_shower", "couloir")

label exit_shower:
    scene BG_couloir
    with fondu
    call screen couloir

label shower_l2:
    show screen Actor1("l2", "nue", "normal", "sh_0", "", "tower", "", "", "", "Rougir", "P")
    with fondu
    l2 "Salut Lincoln"
    show screen Actor1("l2", "nue", "normal", "sh_0", "", "tower", "", "", "", "Rougir", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    jump shower_in

label wc_use:
    call timer (0, 5) from _call_timer_20
    user "ça fait du bien de pisser un coup !"
    jump salleDeBain

label baignoire:
    if heure >= 9 and heure < 15 and jour < 6:
        scene BG_bain_in
        show screen User(tenue, "_P")
        with fondu
        user "Je dois aller à l'école !"
        hide screen User
        with outR
        jump salleDeBain
    elif True:
        scene BG_bain_in
        menu:
            "Prendre une douche" if True:
                call timer (0, 30) from _call_timer_21
                show Lincoln_nu
                with fondu
                user "Une bonne douche me fera du bien !"
                hide Lincoln_nu
                with fondu
            "Se masturber" if sex_points >= 50:
                call timer (0, 10) from _call_timer_22
                $ sex_points = 0
                nar "en construction..."
            "Rien" if True:
                jump salleDeBain

label shower_in:
    $ checkZone = "shower"
    if jour < 6 and heure < 9 and mastu_dream_leni == False:
        jump salle_de_bain_leni_1
    elif True:
        jump salleDeBain

label salleDeBain:
    scene BG_bain
    with fondu
    if jour == 3:
        if heure == 7 or heure == 20:
            call screen salleDeBain("l2")
        elif True:
            call screen salleDeBain("")
    elif jour < 6:
        if heure == 7 or heure == 17:
            call screen salleDeBain("l2")
        elif True:
            call screen salleDeBain("")
    elif jour == 6:
        if heure == 11 or heure == 21:
            call screen salleDeBain("l2")
        elif True:
            call screen salleDeBain("")
    elif jour == 7:
        if heure == 11 or heure == 17:
            call screen salleDeBain("l2")
        elif True:
            call screen salleDeBain("")
    elif True:
        call screen salleDeBain("")

label peek_shower:
    call timer (0, 5) from _call_timer_23
    if jour < 6 and heure < 9 and mastu_dream_leni == False:
        show screen peekLoud("leni_douche")
        $ sex_points += 5
        pause
        hide screen peekLoud
    elif True:
        show screen peekLoud("BG_bain")
        nar ""
        hide screen peekLoud
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
