screen Grenier():
    if heure >= 20 and heure < 23:
        imagebutton:
            xalign 0.8
            yalign 0.5
            idle "Images/Plans/Grenier/l7.png"
            hover "Images/Plans/Grenier/l7_hover.png"
            action Jump("grenier_l7_shop")

    if coco_jambe_1 == "perdue":
        imagebutton:
            xalign 0.85
            yalign 0.63
            idle "Images/Plans/Grenier/coco_jambe.png"
            hover "Images/Plans/Grenier/coco_jambe_hover.png"
            action Jump("grenier_l4_quest_1")

    imagebutton:
        xalign 0.54
        yalign 0.7
        idle "Images/Plans/Minis/flecheB.png"
        hover "Images/Plans/Minis/flecheB_hover.png"
        action Jump("couloir")

label grenier:
    $ checkZone = "grenier"
    scene BG_grenier
    with fondu
    call screen Grenier

label grenier_l4_quest_1:
    show screen User(tenue, "_P")
    with inL
    user "C'est la jambe de monsieur Coco ! {w}Vite, allons la rendre à Luan."


    $ coco_jambe_1 = "inpoche"

    hide screen User
    with outB
    jump grenier

label grenier_l7_shop:
    show Lucy_voyante_P at right
    with fondu
    l7 "Lincoln... Soupir..."
    hide Lucy_voyante_P
    show Lucy_voyante at right
    with fondu
    call screen Lucy_shop
    nar ""
    hide Lucy_voyante
    jump grenier

screen Lucy_shop():
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        if l2_halloween_2020 == False:
            button:
                frame:
                    hover_background Frame("gui/frame_horror.png", gui.frame_borders, tile=gui.frame_tile)
                    has hbox:
                        spacing 5
                    add "Images/Objets/citrouille.png" xalign 0.5
                    label _("Halloween 2020") xalign 0.5 yalign 0.5
                action Jump("Halloween_2020_Go")
        else:
            text _("En cours de fabrication...")

        text ""
        imagebutton:
            idle "Images/Bases/Icones/Faces/face_retour.png"
            hover "Images/Bases/Icones/Faces/face_retour_hover.png"
            action Jump("grenier")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
