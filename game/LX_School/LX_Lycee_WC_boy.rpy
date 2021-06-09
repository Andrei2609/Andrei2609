screen WC_boy():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("wc")

    imagebutton:
        xalign 0.67
        yalign 0.5
        idle "Images/Plans/Minis/gloryhole.png"
        hover "Images/Plans/Minis/gloryhole_hover.png"
        action Jump("GloryHole")

    imagebutton:
        xalign 0.56
        yalign 0.5
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("wc_boy_use")

label wc_garcons:
    $ checkZone = "school_wc_boy"
    scene BG_lycee_wc_garcon
    with fondu
    call screen WC_boy

label wc_boy_use:
    if heure < 10:
        show screen User (tenue, "_P")
        user "Clyde y est déjà et j'en ai pas besoin."
        hide screen User
        jump wc_garcons
    elif True:
        show screen User (tenue, "_P")
        user "Pas envie."
        hide screen User
        jump wc_garcons
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
