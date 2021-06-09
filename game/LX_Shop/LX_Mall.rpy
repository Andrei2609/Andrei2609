
image BG_mall_ext = "Images/Backgrounds/mall_exterieur.png"
image BG_mall_in = "Images/Backgrounds/mall_interieur.png"

screen mall():
    imagemap:
        idle "Images/Plans/mall_interieur.png"
        hover "Images/Plans/mall_interieur_hover.png"

        hotspot (536,279,173,133) action Jump("exit_mall")
        hotspot (41,184,194,295) action Jump("BD_shop")
        hotspot (279,265,121,173) action Jump("Electro_shop")
        hotspot (434,316,71,98) action Jump("Bar_shop")
        hotspot (870,325,141,195) action Jump("Bonbon_shop")
        hotspot (1039,232,241,262) action Jump("Vet_shop")
        hotspot (838,174,122,130) action Jump("General_shop")

screen mall_ext():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/flecheBD.png"
        hover "Images/Plans/Minis/flecheBD_hover.png"
        action Jump("map")

    if heure > 8 and heure < 22 and jour < 7:
        imagebutton:
            xalign 0.555
            yalign 0.294
            idle "Images/Plans/Centre_Commercial/porte.png"
            hover "Images/Plans/Centre_Commercial/porte_hover.png"
            action Jump("mall_in")

    vbox:
        xalign 0.17
        yalign 0.63
        text _("Ouvert de") xalign 0.5
        text _("9h à 21h") xalign 0.5

label mall_in:
    $ checkZone = "mall_hall"
    scene BG_mall_in
    with fondu
    $ mall_in = True
    call screen mall

label mall:
    $ checkZone = "mall_out"
    call timer (0, 10) from _call_timer_40
    jump exit_mall

label exit_mall:
    scene BG_mall_ext
    with fondu
    $ mall_in = False
    call screen mall_ext
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
