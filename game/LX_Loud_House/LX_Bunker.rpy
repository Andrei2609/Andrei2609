
image BG_bunker = "Images/Backgrounds/bunker.png"
image BG_bunker_2 = "Images/Backgrounds/bunker_2.png"

screen Bunker():
    imagebutton:
        xalign 0.42
        yalign 0.2
        idle "Images/Plans/Minis/flecheH.png"
        hover "Images/Plans/Minis/flecheH_hover.png"
        action Jump("VC_exit")

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("bunker_sm")

screen Donjon():
    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("bunker_in")

label bunker:
    call screen VerrouCode

label bunker_in:
    $ checkZone = "bunker"
    scene BG_bunker
    with fondu
    call screen Bunker

label bunker_sm:
    $ checkZone = "donjon"
    scene BG_bunker_2
    with fondu
    call screen Donjon
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
