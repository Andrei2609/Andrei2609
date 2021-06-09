label cham_user_2:
    scene BG_lincoln_2
    with fondu
    call screen bureau_user

screen bureau_user():
    imagebutton:
        xalign 0.066
        yalign 0.0
        idle "Images/Plans/CH_l6/porte.png"
        hover "Images/Plans/CH_l6/porte_hover.png"
        action Jump("exit_room")

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("cham_user")

    imagebutton:
        xalign 0.741
        yalign 0.0
        idle "Images/Plans/CH_l6/penderie.png"
        hover "Images/Plans/CH_l6/penderie_hover.png"
        action ShowMenu("penderie")

    imagebutton:
        xalign 0.714
        yalign 0.7389
        hover_xalign 0.723
        hover_yalign 0.7675
        idle "Images/Plans/CH_l6/tiroirs_1.png"
        hover "Images/Plans/CH_l6/tiroirs_1_hover.png"
        action ShowMenu("Menu_galerie")

    imagebutton:
        xalign 0.714
        yalign 0.895
        hover_xalign 0.723
        hover_yalign 0.93
        idle "Images/Plans/CH_l6/tiroirs_2.png"
        hover "Images/Plans/CH_l6/tiroirs_2_hover.png"
        action ShowMenu("Menu_collection")

    imagebutton:
        xalign 0.45
        yalign 0.905
        hover_xalign 0.45
        hover_yalign 0.91
        idle "Images/Plans/CH_l6/placard.png"
        hover "Images/Plans/CH_l6/placard_hover.png"
        action ShowMenu("Placard")

    if ordiUser == 1:
        imagebutton:
            xalign 0.5
            yalign 0.47
            idle "Images/Plans/CH_l6/ordinateur.png"
            hover "Images/Plans/CH_l6/ordinateur_hover.png"
            action Jump("PC_cham_user")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
