screen church():
    imagebutton:
        xalign 0.5
        yalign 0.99
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("map")

    if jour == 7 and heure < 12:
        imagebutton:
            xalign 0.8
            yalign 0.6
            idle "Images/Plans/Minis/bureau.png"
            hover "Images/Plans/Minis/bureau_hover.png"
            action Jump("priere")

label eglise:
    $ checkZone = "eglise"
    scene BG_eglise
    with fondu
    if heure >= 6 and heure < 19:
        call timer (0, 10) from _call_timer_16
        jump eglise_2

label eglise_2:
    call screen church

label priere:
    $ heure += 1
    nar "Vous écouter la messe avec attention...{w}Où presque !"
    jump eglise_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
