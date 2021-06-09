screen Hopital():
    imagebutton:
        xalign 0.4
        yalign 0.5
        idle "Images/Plans/Minis/flecheH.png"
        hover "Images/Plans/Minis/flecheH_hover.png"
        action Jump("map")

label hopital:
    $ checkZone = "hopital"
    call timer (0, 10) from _call_timer_38
    scene BG_hopital_salle
    with fondu
    call screen Hopital
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
