label niche:
    $ checkZone = "niche"
    scene BG_niche
    with fondu
    call screen Niche

screen Niche():
    imagebutton:
        xalign 0.9
        yalign 0.5
        idle "Images/Plans/Minis/flecheD.png"
        hover "Images/Plans/Minis/flecheD_hover.png"
        action Jump("jardin")

    if mom_cle == "inpoche":
        textbutton _("les cacher"):
            xalign 0.5
            yalign 0.5
            action SetVariable("mom_cle", "go")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
