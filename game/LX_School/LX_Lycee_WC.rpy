label wc:
    $ checkZone = "school_wc"
    scene BG_lycee_wc
    with fondu
    call screen WC_school

screen WC_school():
    imagebutton:
        xalign 0.009
        yalign 0.6
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("hall")

    imagebutton:
        xalign 0.26
        yalign 0.4
        idle "Images/Plans/Minis/flecheH.png"
        hover "Images/Plans/Minis/flecheH_hover.png"
        action Jump("wc_garcons")

    imagebutton:
        xalign 0.74
        yalign 0.4
        idle "Images/Plans/Minis/flecheH.png"
        hover "Images/Plans/Minis/flecheH_hover.png"
        action Jump("wc_filles")

    imagebutton:
        xalign 0.65
        yalign 0.53
        idle "Images/Plans/Minis/peek.png"
        hover "Images/Plans/Minis/peek_hover.png"
        action Jump("peek_wc_filles")

    if jour == 5 and heure < 11 or jour == 5 and heure >= 15 or heure < 13 and heure >= 10:
        imagebutton:
            xalign 0.5
            yalign 0.65
            idle "Images/Plans/Lycee/EVENT/mollie.png"
            hover "Images/Plans/Lycee/EVENT/mollie_hover.png"
            action Jump("school_mollie")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
