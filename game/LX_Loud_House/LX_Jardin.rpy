screen jardin():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("allee")

    imagebutton:
        xalign 0.5
        yalign 0.99
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        action Jump("cuisine")

    if jour < 6 and heure >= 8 and heure < 12 and mom_cle == "go" and go_school == True:
        imagebutton:
            xalign 0.072
            yalign 0.8
            idle "Images/Plans/Jardin/mom_niche.png"
            hover "Images/Plans/Jardin/mom_niche_hover.png"
            action Jump("mom_quest_1")
    else:
        imagebutton:
            xalign 0.07
            yalign 0.776
            idle "Images/Plans/Jardin/niche.png"
            hover "Images/Plans/Jardin/niche_hover.png"
            action Jump("niche")

    imagebutton:
        xalign 0.753
        yalign 0.687
        idle "Images/Plans/Jardin/bunker.png"
        hover "Images/Plans/Jardin/bunker_hover.png"
        action Jump("bunker")

    if jour == 6 and heure == 20:
        imagebutton:
            xalign 0.3
            yalign 0.6
            idle "Images/Plans/Jardin/l2.png"
            hover "Images/Plans/Jardin/l2_hover.png"
            action Jump("jardin_l2")

label jardin:
    $ checkZone = "jardin"
    scene BG_jardin
    with fondu
    call screen jardin

label jardin_l2:
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "P")
    with fondu
    l2 "Salut Lincoln"
    show screen Actor1("l2", "nue", "normal", "", "", "normal", "boucle_1", "lunettes", "", "Joyeux", "")
    with fondu
    call screen l2_talk
    hide screen Actor1
    jump jardin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
