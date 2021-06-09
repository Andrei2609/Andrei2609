screen habit(vet, vetNom):
    if tenue == vet:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 120
            ysize 300
            background None
            add "Images/Personnages/106-Lincoln/Penderie/[vet]_actif.png"
            text vetNom vertical True xalign 0.1 yalign 0.5
    else:
        button:
            xalign 0.5
            yalign 0.5
            frame:
                xsize 120
                ysize 300
                background None
                hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                add "Images/Personnages/106-Lincoln/Penderie/[vet].png"
                text vetNom vertical True xalign 0.1 yalign 0.5
            action SetVariable("tenue", vet), Return(True)

screen penderie():
    zorder 200
    frame:
        xalign 0.5
        ysize 700
        xsize 750
        background Frame("gui/frame_tab.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox:
            xalign 0.5
            yalign 0.5
        add "Images/Bases/penderie.png" xalign 0.5
        grid 5 2:
            spacing 10
            xalign 0.5
            yalign 0.5
            use habit("class", _("Chemise"))
            use habit("classA", _("Costume"))
            use habit("sport", _("Sport"))
            if saison == "hiver":
                use habit("hiver", _("Hiver"))
            else:
                use habit("ete", _("Ete"))
            if saison == "ete":
                use habit("swim", _("M. Bain"))
            else:
                null
            use habit("nu", _("Nu"))
            use habit("slip", _("Slip"))
            use habit("slipA", _("Slip V."))
            use habit("normal", _("Normal"))
            imagebutton:
                xalign 1.0
                yalign 1.0
                idle "Images/Bases/Icones/Faces/face_retour.png"
                hover "Images/Bases/Icones/Faces/face_retour_hover.png"
                action Return(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
