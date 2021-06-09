screen CH_l10_l11():
    imagebutton:
        xalign 0.15
        yalign 0.5
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("ch_out_l10_l11")

    if heure < 9 or heure >= 15 and heure <= 20:
        imagebutton:
            xalign 0.55
            yalign 0.75
            idle "Images/Plans/CH_l10_l11/l10.png"
            hover "Images/Plans/CH_l10_l11/l10_hover.png"
            action Jump("lisa_shop")

    if boost_secret == False:
        imagebutton:
            xalign 0.75
            yalign 0.58
            idle "Images/Plans/CH_l10_l11/goute.png"
            hover "Images/Plans/CH_l10_l11/goute_hover.png"
            action SetVariable("boost_secret", True)

label cham_l10_l11:
    call screen porte_cham("ch_in_l10_l11", "peek_l10_l11", "couloir")

label ch_in_l10_l11:
    $ checkZone = "ch_l10_l11"
    scene BG_lisa_lily
    with fondu
    call screen CH_l10_l11

label ch_out_l10_l11:
    hide screen CH_l10_l11
    with fondu
    jump couloir

label lisa_shop:
    show Lisa_P at right
    with fondu
    menu:
        l10 "Lincoln, tu as besoin de quelque chose ?"
        "Oui" if True:
            hide Lisa_P
            show I_Lisa at right
            with fondu
            call screen lisa_shop
        "Non, merci Lisa." if True:
            hide Lisa_P
            jump ch_in_l10_l11

screen lisa_shop():
    vbox:
        xalign 0.5
        yalign 0.3
        grid 3 2:
            spacing 10
            xalign 0.5
            yalign 0.5
            use obj_shop("lisa", boost_love, "boost_love", 10)
            use obj_shop("lisa", boost_sex, "boost_sex", 10)
            use obj_shop("lisa", boost_boobs, "boost_boobs", 50)
            use obj_shop("lisa", boost_invisible, "boost_invisible", 100)
            null
            if l10_win == False and user_coins >= 100:
                button:
                    xalign 0.5
                    yalign 0.5
                    frame:
                        xsize 150
                        ysize 150
                        hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                        has vbox:
                            xalign 0.5
                            yalign 0.5
                        add "Images/Objets/panty/panty_l10.png"
                        text "100 $" xalign 0.5
                    action SetVariable("l10_win", True), SetVariable("user_coins", user_coins - 100)
            else:
                frame:
                    xalign 0.5
                    yalign 0.5
                    xsize 150
                    ysize 150
                    background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                    has vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 5
                    if l10_win == True:
                        add "Images/Objets/item_vide.png" xalign 0.5
                        text _("Déjà eu") xalign 0.5
                    else:
                        add "Images/Objets/panty/panty_null.png" xalign 0.5
                        text _("pas possible") xalign 0.5
        text ""
        frame:
            xalign 0.5
            yalign 0.5
            textbutton _("Rien"):
                action Jump("ch_in_l10_l11")

label peek_l10_l11:
    call timer (0, 5) from _call_timer_3
    show screen peekLoud("BG_lisa_lily")
    user "Rien à voir..."
    hide screen peekLoud
    jump couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
