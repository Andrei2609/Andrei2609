screen Salon():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("entree")

    imagebutton:
        xalign 0.431
        yalign 0.131
        idle "Images/Plans/Salon/ch_mom.png"
        hover "Images/Plans/Salon/ch_mom_hover.png"
        action Jump("cham_mom")

    if jour < 6 and heure == 15 or jour == 6 and heure == 14:
        imagebutton:
            xalign 0.68
            yalign 0.75
            idle "Images/Plans/Salon/l2.png"
            hover "Images/Plans/Salon/l2_hover.png"
            action Jump("salon_l2")

    if lynn_peek_1 == False and heure > 6 and heure < 9:
        imagebutton:
            xalign 0.7
            yalign 0.99
            idle "Images/Plans/Salon/l5_abdo.png"
            hover "Images/Plans/Salon/l5_abdo_hover.png"
            action Jump("l5_sport_matin")

    if mom_party_21 == False and jour == 7 and heure > 14 and heure <= 20:
        imagebutton:
            xalign 0.3
            yalign 0.525
            idle "Images/Plans/Salon/l2_quest.png"
            hover "Images/Plans/Salon/l2_quest_hover.png"
            action Jump("mom_party_2021")

    imagebutton:
        xalign 0.5
        yalign 0.6
        idle "Images/Plans/Salon/TV.png"
        hover "Images/Plans/Salon/TV_hover.png"
        action Jump("TV")

label salon:
    $ checkZone = "salon"
    scene BG_salon
    with fondu
    call screen Salon

label salon_l2:
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "P")
    with fondu
    l2 "Salut Lincoln"
    show screen Actor1("l2", "nue", "normal", "sh_1", "sb_1", "normal", "boucle_1", "lunettes", "", "Neutre", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    jump salon

label TV:
    scene TV_off
    with fondu
    menu:
        "Regarder la TV" if True:
            jump TV_on
        "Regarder un film porno" if heure < 3 or heure > 20:
            jump TV_porn
        "Jouer aux Jeux Vidéos" if True:
            jump TV_jv
        "Se lever" if True:
            jump salon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
