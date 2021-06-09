
image BG_lori_leni = "Images/Backgrounds/chambre_lori_leni.png"
image l1_lit_back = "Images/Mini-Jeux/Lit/l1/lit_back.png"
image l2_lit_back = "Images/Mini-Jeux/Lit/l2/lit_back.png"

screen CH_l1_l2(actor1, actor2):
    imagebutton:
        xalign 0.35
        yalign 1.0
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("ch_out_l1_l2")

    imagebutton:
        xalign 0.2
        yalign 0.75
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_tiroir_l1_l2")

    imagebutton:
        xalign 0.26
        yalign 0.51
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_placard_l1_l2")

    if actor1 == "l1" or actor2 == "l1":
        if heure < 7 or heure >= 22 and jour >= 5:
            imagebutton:
                xalign 0.888
                yalign 0.796
                idle "Images/Plans/CH_l1_l2/lit_l1.png"
                hover "Images/Plans/CH_l1_l2/lit_l1_hover.png"
                action Jump("ch_l1_l2_lit_l1")
        elif heure >= 20 and jour >= 5:
            imagebutton:
                xalign 0.8
                yalign 0.63
                idle "Images/Plans/CH_l1_l2/l1_lit.png"
                hover "Images/Plans/CH_l1_l2/l1_lit_hover.png"
                action Jump("ch_l1_l2_l1")
        else:
            imagebutton:
                xalign 0.03
                yalign 0.9
                idle "Images/Plans/CH_l1_l2/l1.png"
                hover "Images/Plans/CH_l1_l2/l1_hover.png"
                action Jump("ch_l1_l2_l1")

    if actor1 == "l2" or actor2 == "l2":
        if tissu_leni_1 <> "win" and heure > 14 and heure < 19:
            imagebutton:
                xalign 0.55
                yalign 0.9
                idle "Images/Plans/CH_l1_l2/l2_q1.png"
                hover "Images/Plans/CH_l1_l2/l2_q1_hover.png"
                action Jump("l2_quest_1")
        elif heure >= 20 and heure < 23:
            imagebutton:
                xalign 1.0
                yalign 0.67
                idle "Images/Plans/CH_l1_l2/l2_lit.png"
                hover "Images/Plans/CH_l1_l2/l2_lit_hover.png"
                action Jump("ch_l1_l2_l2")
        elif heure <= 6 and jour < 6 or heure >= 23 or jour >= 6 and heure < 9:
            imagebutton:
                xalign 1.0
                yalign 1.0
                idle "Images/Plans/CH_l1_l2/lit_l2.png"
                hover "Images/Plans/CH_l1_l2/lit_l2_hover.png"
                action Jump("ch_l1_l2_lit_l2")
        else:
            imagebutton:
                xalign 0.55
                yalign 0.7
                idle "Images/Plans/CH_l1_l2/l2.png"
                hover "Images/Plans/CH_l1_l2/l2_hover.png"
                action Jump("ch_l1_l2_l2")

label cham_l1_l2:
    call screen porte_cham("ch_in_l1_l2", "peek_l1_l2", "couloir")

label ch_out_l1_l2:
    hide screen CH_l1_l2
    with fondu
    jump couloir

label ch_in_l1_l2:
    $ checkZone = "ch_l1_l2"
    scene BG_lori_leni
    with fondu
    if jour == 3:
        if heure < 7 or heure == 8 or heure == 13 or heure > 20:
            call screen CH_l1_l2("l2","")
        elif True:
            call screen CH_l1_l2("","")
    elif jour < 6:
        if heure < 7 or heure == 8 or heure == 16 or heure == 18 or heure > 19:
            call screen CH_l1_l2("l2","")
        elif True:
            call screen CH_l1_l2("","")
    elif jour == 6:
        if heure < 10 or heure == 13 or heure > 22:
            call screen CH_l1_l2("l2","")
        elif True:
            call screen CH_l1_l2("","")
    elif jour == 7:
        if heure >= 1 and heure < 10 or heure == 13 or heure == 18 or heure > 19:
            call screen CH_l1_l2("l2","")
        elif True:
            call screen CH_l1_l2("","")
    elif True:
        call screen CH_l1_l2("","")

label ch_l1_l2_l1:
    show screen Actor1("l1", "nue", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    l1 "Oui Lincoln ?"
    show screen Actor1("l1", "nue", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen l1_talk
    hide screen Actor1
    jump ch_in_l1_l2

label ch_l1_l2_l2:
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "P")
    with fondu
    l2 "Salut Lincoln"
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    jump ch_in_l1_l2

label ch_l1_l2_lit_l1:
    scene l1_lit_back
    with fondu
    $ idFille = "l1"
    call screen sex_sleep

label ch_l1_l2_lit_l2:
    scene l2_lit_back
    with fondu
    $ idFille = "l2"
    call screen sex_sleep

label peek_tiroir_l1_l2:
    call timer (0, 5) from _call_timer_29
    call screen Tiroir("ch_in_l1_l2")

label peek_placard_l1_l2:
    call timer (0, 5) from _call_timer_30
    $ int_points += 2
    show screen peekPlacard("Images/Backgrounds/chambre_lori_leni.png")
    user "Rien à voir..."
    hide screen peekPlacard
    jump ch_in_l1_l2

label peek_l1_l2:
    call timer (0, 5) from _call_timer_31
    show screen peekLoud("BG_lori_leni")
    user "Rien à voir..."
    hide screen peekLoud
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
