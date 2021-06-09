image table = "Images/Plans/Lycee/table.png"

screen cantine():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("school_couloir_1")

    if heure == 12:
        imagebutton:
            xalign 0.8
            yalign 0.55
            idle "Images/Plans/Lycee/EVENT/EAT_stella.png"
            hover "Images/Plans/Lycee/EVENT/EAT_stella_hover.png"
            action Jump("school_eat_stella")

    if heure < 12:
        add "Images/Plans/Bonus/EAT_geek_1.png" xalign 0.5 yalign 0.78

    add "Images/Plans/Lycee/table.png" xalign 0.75 yalign 0.95

    if heure < 12:
        imagebutton:
            xalign 0.5
            yalign 0.45
            idle "Images/Plans/Bonus/EAT_geek.png"
            hover "Images/Plans/Bonus/EAT_geek_hover.png"
            action Jump("school_eat_geek")

    if heure == 12:
        imagebutton:
            xalign 0.55
            yalign 0.6
            idle "Images/Plans/Salle_a_Manger/manger.png"
            hover "Images/Plans/Salle_a_Manger/manger_hover.png"
            action Jump("cantine_miam")

    if heure == 13:
        imagebutton:
            xalign 0.3
            yalign 0.9
            idle "Images/Plans/Lycee/EVENT/EAT_l5.png"
            hover "Images/Plans/Lycee/EVENT/EAT_l5_hover.png"
            action Jump("school_eat_l5")

    if heure >= 12 and heure < 13:
        imagebutton:
            xalign 0.01
            yalign 0.99
            idle "Images/Plans/Lycee/EVENT/EAT_clyde.png"
            hover "Images/Plans/Lycee/EVENT/EAT_clyde_hover.png"
            action Jump("school_eat_clyde")

label cantine:
    $ checkZone = "cantine"
    scene BG_lycee_cantine
    show table:
        xalign 0.75
        yalign 0.95
    with fondu
    call screen cantine

label cantine_miam:
    show eat_user_school
    with fondu
    nar ""
    call timer (1, 0) from _call_timer_5
    $ vie_points = 100
    hide eat_user_school
    jump cantine
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
