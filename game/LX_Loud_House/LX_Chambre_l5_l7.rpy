
image BG_lynn_lucy = "Images/Backgrounds/chambre_lynn_lucy.png"
image l5_lit_back = "Images/Mini-Jeux/Lit/l5/lit_back.png"

screen CH_l5_l7():
    imagebutton:
        xalign 0.5
        yalign 1.0
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("ch_out_l5_l7")

    imagebutton:
        xalign 0.48
        yalign 0.75
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_tiroir_l5_l7")

    if heure < 7 or heure >= 22:
        imagebutton:
            xalign 0.843
            yalign 0.963
            idle "Images/Plans/CH_l5_l7/lit_l5.png"
            hover "Images/Plans/CH_l5_l7/lit_l5_hover.png"
            action Jump("ch_l5_l7_lit_l5")
    elif heure >= 15 or jour == 3 and heure >= 13 or jour >= 6 and heure >= 9:
        imagebutton:
            xalign 0.8
            yalign 0.95
            idle "Images/Plans/CH_l5_l7/l5.png"
            hover "Images/Plans/CH_l5_l7/l5_hover.png"
            action Jump("ch_l5_l7_l5")

    if heure >=15 and heure < 20:
        imagebutton:
            xalign 0.35
            yalign 0.88
            idle "Images/Plans/CH_l5_l7/l7.png"
            hover "Images/Plans/CH_l5_l7/l7_hover.png"
            action Jump("ch_l5_l7_l7")

label cham_l5_l7:
    call screen porte_cham("ch_in_l5_l7", "peek_l5_l7", "couloir")

label ch_out_l5_l7:
    hide screen CH_l3_l4
    with fondu
    jump couloir

label ch_in_l5_l7:
    $ checkZone = "ch_l5_l7"
    scene BG_lynn_lucy
    with fondu
    call screen CH_l5_l7

label ch_l5_l7_l5:
    show screen Actor1("l5", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    l5 "Qu'est-ce que tu veux Puanteur ?"
    show screen Actor1("l5", "normal", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    with fondu
    call screen l5_talk
    hide screen Actor1
    jump ch_in_l5_l7

label ch_l5_l7_l7:
    show Lucy_P at right
    with fondu
    l7 "Bonjour Lincoln... Soupir..."
    hide Lucy_P
    show Lucy at right
    with fondu
    nar "en construction"
    hide Lucy
    jump ch_in_l5_l7

label ch_l5_l7_lit_l5:
    scene l5_lit_back
    with fondu
    $ idFille = "l5"
    call screen sex_sleep

label peek_tiroir_l5_l7:
    call timer (0, 5) from _call_timer_24
    call screen Tiroir("ch_in_l5_l7")

label peek_l5_l7:
    call timer (0, 5) from _call_timer_25
    show screen peekLoud("BG_lynn_lucy")
    user "Rien à voir..."
    hide screen peekLoud
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
