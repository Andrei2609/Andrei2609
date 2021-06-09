screen Grouse_ext():
    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("map")

label m_grouse:
    call timer (0, 10) from _call_timer_11
    $ checkZone = "grouse_out"
    scene BG_grouse
    with fondu
    call screen Grouse_ext
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
