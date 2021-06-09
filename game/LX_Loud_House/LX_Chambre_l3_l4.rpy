
image BG_luna_luan = "Images/Backgrounds/chambre_luna_luan.png"
image PEEK_luna_luan = "Images/Backgrounds/chambre_luna_luan_peek.png"
image l3_lit_back = "Images/Mini-Jeux/Lit/l3/lit_back.png"
image l4_lit_back = "Images/Mini-Jeux/Lit/l4/lit_back.png"

screen CH_l3_l4(actor1, actor2):
    imagebutton:
        xalign 0.6
        yalign 1.0
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("ch_out_l3_l4")

    imagebutton:
        xalign 0.89
        yalign 0.6
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_tiroir_l3_l4")

    if actor1 == "l3" or actor2 == "l3":
        if heure < 7 or heure >= 22:
            imagebutton:
                xalign 0.0
                yalign 0.27
                idle "Images/Plans/CH_l3_l4/lit_l3.png"
                hover "Images/Plans/CH_l3_l4/lit_l3_hover.png"
                action Jump("ch_l3_l4_lit_l3")
        else:
            imagebutton:
                xalign 0.2
                yalign 0.9
                idle "Images/Plans/CH_l3_l4/l3.png"
                hover "Images/Plans/CH_l3_l4/l3_hover.png"
                if coco_jambe_1 == "inpoche":
                    action Jump("l4_quest_1_fin")
                else:
                    action Jump("ch_l3_l4_l3")

    if actor1 == "l4" or actor2 == "l4":
        if heure < 7 or heure >= 22:
            imagebutton:
                xalign 0.0
                yalign 0.905
                idle "Images/Plans/CH_l3_l4/lit_l4.png"
                hover "Images/Plans/CH_l3_l4/lit_l4_hover.png"
                action Jump("ch_l3_l4_lit_l4")
        else:
            imagebutton:
                xalign 0.75
                yalign 0.7
                idle "Images/Plans/CH_l3_l4/l4.png"
                hover "Images/Plans/CH_l3_l4/l4_hover.png"
                action Jump("ch_l3_l4_l4")

label cham_l3_l4:
    call screen porte_cham("ch_in_l3_l4", "peek_l3_l4", "couloir")

label ch_out_l3_l4:
    hide screen CH_l3_l4
    with fondu
    jump couloir

label ch_in_l3_l4:
    $ checkZone = "ch_l3_l4"
    scene BG_luna_luan
    with fondu
    if heure < 8 and luna_peek_1 == False:
        jump l3_surprise_nue_cham_1
    elif heure < 9:
        call screen CH_l3_l4("l3","")
    elif True:
        call screen CH_l3_l4("","")

label ch_l3_l4_l3:
    show screen Actor1("l3", "nue", "normal", "sh_0", "sb_1", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "P")
    with fondu
    l3 "Hello Brother !"
    show screen Actor1("l3", "nue", "normal", "sh_0", "sb_1", "normal", "boucle_1", "bracelet_1", "collier_1", "Neutre", "")
    with fondu
    call screen l3_talk
    hide screen Actor1
    jump ch_in_l3_l4

label ch_l3_l4_l4:
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "P")
    with fondu
    l4 "Salut Lincoln, alors ça gaze ?"
    show screen Actor1("l4", "nue", "normal", "sh_1", "sb_1", "normal", "", "", "", "Neutre", "")
    call screen l4_talk
    hide screen Actor1
    jump ch_in_l3_l4

label ch_l3_l4_lit_l3:
    scene l3_lit_back
    with fondu
    $ idFille = "l3"
    call screen sex_sleep

label ch_l3_l4_lit_l4:
    scene l4_lit_back
    with fondu
    $ idFille = "l4"
    call screen sex_sleep

label peek_tiroir_l3_l4:
    call timer (0, 5) from _call_timer_36
    call screen Tiroir("ch_in_l3_l4")

label peek_l3_l4:
    call timer (0, 5) from _call_timer_37
    if luna_peek_1 == False:
        show screen peekLoud("FULL_luna_dos_3")
        pause
        $ sex_points += 5
        hide screen peekLoud
    elif True:
        show screen peekLoud("PEEK_luna_luan")
        user "Rien à voir..."
        hide screen peekLoud
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
