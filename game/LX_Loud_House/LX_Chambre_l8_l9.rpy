
image BG_lana_lola = "Images/Backgrounds/chambre_lana_lola.png"
image BG_lana = "Images/Backgrounds/chambre_lana.png"
image BG_lola = "Images/Backgrounds/chambre_lola.png"

screen CH_l8_l9():
    imagebutton:
        xalign 0.35
        yalign 1.0
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("ch_out_l1_l2")

    imagebutton:
        xalign 0.01
        yalign 0.96
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("ch_lana")


label cham_l8_l9:
    call screen porte_cham("ch_in_l8_l9", "peek_l8_l9", "couloir")

label ch_out_l8_l8:
    hide screen CH_l8_l9
    with fondu
    jump couloir

label ch_in_l8_l9:
    $ checkZone = "ch_l8_l9"
    scene BG_lola
    with fondu
    call screen CH_l8_l9

label peek_l8_l9:
    call timer (0, 5) from _call_timer_19
    show screen peekLoud("BG_lana_lola")
    user "Rien à voir..."
    hide screen peekLoud
    jump couloir

label ch_lana:
    scene BG_lana
    with fondu
    user "Le bazare de Lana..."
    user "Mieux vaut ne rien touché..."
    jump ch_in_l8_l9
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
