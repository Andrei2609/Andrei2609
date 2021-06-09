screen couloir():
    imagemap:
        idle "Images/Plans/couloir.png"
        hover "Images/Plans/couloir_hover.png"

        if heure >= 15 and INTRO_Actif == 4:
            hotspot (600,295,87,200) action Jump("prime_quest_bedroom_user")
        else:
            hotspot (600,295,87,200) action Jump("cham_user")
        hotspot (1110,0,170,720) action Jump("cham_l1_l2")
        hotspot (0,0,130,720) action Jump("cham_l3_l4")
        hotspot (280,65,110,580) action Jump("cham_l5_l7")
        hotspot (490,235,43,300) action Jump("cham_l8_l9")
        hotspot (747,238,41,307) action Jump("cham_l10_l11")
        hotspot (609,612,89,105) action Jump("shower")
        hotspot (824,9,106,640) action Jump("entree")
        hotspot (570,170,150,60) action Jump("grenier")

label couloir:
    $ checkZone = "couloir"
    scene BG_couloir
    with fondu
    call screen couloir


screen porte_cham(ch, peek, retour):
    frame:
        xalign 0.5
        yalign 0.5
        xsize 300
        ysize 400
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            label "Que faire ?" xalign 0.5 yalign 0.5
            add "Images/Plans/porte.png" xalign 0.5 yalign 0.5
            textbutton "Retour":
                xalign 0.5
                action Jump(retour)
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            vbox:
                spacing 3
                imagebutton xalign 0.5 yalign 0.5:
                    idle "Images/Bases/Icones/peek.png"
                    hover "Images/Bases/Icones/peek_hover.png"

                    if loud_peek_count == 5 and heure > 15:
                        action SetVariable("loud_peek_count", 0), Jump("Mastu_Course")
                    else:
                        action SetVariable("loud_peek_count", loud_peek_count +1), Jump(peek)
                text "Espionner" xalign 0.5 yalign 0.5
            vbox:
                spacing 3
                imagebutton xalign 0.5 yalign 0.5:
                    idle "Images/Bases/Icones/entre.png"
                    hover "Images/Bases/Icones/entre_hover.png"

                    action Jump(ch)
                text "Entrer" xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
