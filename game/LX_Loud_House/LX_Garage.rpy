label garage:
    $ checkZone = "garage"
    scene BG_garage
    with fondu
    call screen Garage

screen Garage():
    imagebutton:
        xalign 0.3
        yalign 0.65
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("allee")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
