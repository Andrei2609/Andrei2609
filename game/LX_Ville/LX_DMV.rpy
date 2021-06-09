
image BG_office_permis = "Images/Backgrounds/office_permis.png"
image BG_office_permis_in = "Images/Backgrounds/office_permis_in.png"

screen DMV():
    imagebutton:
        xalign 0.009
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("map")

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        action Jump("DMV_in")

screen DMV_int():
    imagebutton:
        xalign 0.064
        yalign 0.87
        idle "Images/Plans/DMV/porte.png"
        hover "Images/Plans/DMV/porte_hover.png"
        action Jump("DMV_2")

    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "Images/Plans/DMV/bureau.png"
        hover "Images/Plans/DMV/bureau_hover.png"
        action Jump("caisse_auto")

    if permis_test_go == True:
        imagebutton:
            xalign 0.703
            yalign 0.5
            idle "Images/Plans/DMV/porte_test.png"
            hover "Images/Plans/DMV/porte_test_hover.png"
            action Jump("quiz_auto")

label DMV:
    call timer (0, 10) from _call_timer_52
    jump DMV_2

label DMV_2:
    $ checkZone = "dmv_out"
    scene BG_office_permis
    with fondu
    call screen DMV

label DMV_in:
    $ checkZone = "dmv_hall"
    scene BG_office_permis_in
    with fondu
    call screen DMV_int

label caisse_auto:
    menu:
        nar "Bonjour, c'est 500 $ pour passer le permis."
        "Je veux le faire" if user_coins >= 500:
            $ permis_test_go = True
            $ user_coins -= 500
            nar "Parfait, c'est dans la salle 1 !"
            jump DMV_in
        "Une prochaine fois..." if True:
            jump DMV_in
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
