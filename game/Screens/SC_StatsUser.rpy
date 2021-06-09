screen user_stats():
    zorder 100
    frame:
        xalign 0.0
        yalign 0.0
        ysize 70
        has hbox:
            spacing 3
            yalign 0.5
        imagebutton:
            idle "Images/Bases/Icones/menu.png"
            hover "Images/Bases/Icones/menu_hover.png"
            action ShowMenu("MenuPause")
        imagebutton:
            idle "Images/Bases/Icones/user.png"
            hover "Images/Bases/Icones/user_hover.png"
            action ShowMenu("Menu_des_stats")
        if home_in == True:
            imagebutton:
                idle "Images/Bases/Icones/fille_loud.png"
                hover "Images/Bases/Icones/fille_loud_hover.png"
                action ShowMenu("Filles_Loud")
        elif city_in == True:
            imagebutton:
                idle "Images/Bases/Icones/fille_ville.png"
                hover "Images/Bases/Icones/fille_ville_hover.png"
                action ShowMenu("Filles_Ville")
        elif ecole_in == True:
            imagebutton:
                idle "Images/Bases/Icones/fille_school.png"
                hover "Images/Bases/Icones/fille_school_hover.png"
                action ShowMenu("Filles_School")
        imagebutton:
            idle "Images/Bases/Icones/inv.png"
            hover "Images/Bases/Icones/inv_hover.png"
            action ShowMenu("Menu_des_objets")
        vbox:
            xalign 0.5
            yalign 1.0
            if jour == 1:
                $ jour_nom = _("Lundi")
            elif jour == 2:
                $ jour_nom = _("Mardi")
            elif jour == 3:
                $ jour_nom = _("Mercredi")
            elif jour == 4:
                $ jour_nom = _("Jeudi")
            elif jour == 5:
                $ jour_nom = _("Vendredi")
            elif jour == 6:
                $ jour_nom = _("Samedi")
            elif jour == 7:
                $ jour_nom = _("Dimanche")

            if saison == "ete":
                add "Images/Bases/Icones/ete.png" xalign 0.5
            elif saison == "hiver":
                add "Images/Bases/Icones/hiver.png" xalign 0.5
            text jour_nom xalign 0.5 font "FT_Open24.ttf" bold True

        vbox:
            xalign 0.5
            yalign 1.0
            add "Images/Bases/Icones/heure.png" xalign 0.5
            if heure < 10 and minute < 10:
                text "0[heure]:0[minute]" xalign 0.5 font "FT_Open24.ttf"
            elif heure < 10 and minute >= 10:
                text "0[heure]:[minute]" xalign 0.5 font "FT_Open24.ttf"
            elif heure >= 10 and minute < 10:
                text "[heure]:0[minute]" xalign 0.5 font "FT_Open24.ttf"
            elif heure >= 10 and minute >= 10:
                text "[heure]:[minute]" xalign 0.5 font "FT_Open24.ttf"

screen stat(name, pts):
    vbox:
        text _(name)
        bar value AnimatedValue(pts, 100, 0.5) style "bar" xsize 250 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
