
image BG_mcbride = "Images/Backgrounds/maison_mcbride.png"
image BG_mcbride_in = "Images/Backgrounds/maison_mcbride_in.png"
image BG_mcbride_shower = "Images/Backgrounds/salle_de_bain_2.png"

screen McBride_ext():
    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("map")

    frame:
        xalign 0.5
        yalign 0.7
        imagebutton:
            idle "Images/Plans/Minis/porte.png"
            hover "Images/Plans/Minis/porte_hover.png"
            action Jump("mcbride_in")

label mcbride:
    call timer (0, 10) from _call_timer_4
    jump mcbride_2

label mcbride_2:
    $ checkZone = "mcbride_out"
    scene BG_mcbride
    with fondu
    call screen McBride_ext

label mcbride_in:
    $ checkZone = "mcbride_hall"
    scene BG_mcbride_in
    with fondu
    call screen mcbride_couloir

screen mcbride_couloir():
    imagemap:
        idle "Images/Plans/maison_mcbride_in.png"
        hover "Images/Plans/maison_mcbride_in_hover.png"

        hotspot (0,0,152,720) action Jump("cham_clyde_dad")
        hotspot (303,10,155,601) action Jump("cham_clyde")
        hotspot (784,10,155,601) action Jump("mcbride_shower")
        hotspot (578,642,68,73) action Jump("mcbride_2")

label cham_clyde_dad:
    $ checkZone = "mcbride_ch_dad"
    scene BG_standby
    with fondu
    nar "en cours de fabrication..."
    jump mcbride_in

label cham_clyde:
    $ checkZone = "mcbride_ch_clyde"
    scene BG_standby
    with fondu
    nar "en cours de fabrication..."
    jump mcbride_in

label mcbride_shower:
    $ checkZone = "mcbride_shower"
    scene BG_mcbride_shower
    with fondu
    nar "en cours de fabrication..."
    jump mcbride_in
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
