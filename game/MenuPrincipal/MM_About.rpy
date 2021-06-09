init:
    $ message = _("D'après une idée original de {color=#6d071a}Kinou{/color}.")
    $ message += "\n"
    $ message += _("Illustré par {color=#9FE855}D-P{/color} et {color=#6d071a}Kinou{/color}.")
    $ message += "\n"
    $ message += _("Conçu avec {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
    $ message += "\n\n"
    $ message += _("Bienvenue chez les Loud est une oeuvre tous droits réservés de {color=#FF5733}Nickelodéon{/color}.")

screen about():
    tag menu

    add "gui/Main_menu/background.png"
    vbox:
        spacing 5
        yalign 0.2
        xalign 0.3
        ysize 720
        hbox:
            xsize 1200
            ysize 100
            vbox:
                label "[config.name!t]"
                text _("Version [config.version!t]")
            text _("À propos"):
                font "FT_name.ttf"
                size 50
                xalign 1.0
                yalign 0.5
        frame:
            xysize (1200,410)
            yalign 0.5
            xalign 0.5
            has hbox:
                spacing 10
            add "gui/Side_menu/version.png" yalign 0.99
            vbox:
                label _("Informations sur la mise à jour :")
                text _("Correction de bugs")
                text _("Ajout de plusieurs Quêtes")
                text _("Ajout de plusieurs CG")
                text _("Ajout de plusieurs Minis Jeux")
                text _("Ajout de plusieurs Zones Cliquables")
                text _("Amélioration des graphismes")
                text ""
                text _("Ce jeux est en cours de développement") xalign 0.5
                text _("est certaines fonctionnalités ne sont pas achevées.") xalign 0.5
        label _("Jeux développé par the Lionesses of Sins.") xalign 0.5
        hbox:
            spacing 10
            vbox:
                spacing 10
                xalign 0.5
                yalign 1.0
                frame:
                    textbutton _("Menu"):
                        action MainMenu()
                imagebutton:
                    idle "gui/Side_menu/retour.png"
                    hover "gui/Side_menu/retour_hover.png"

                    action Return()
            frame:
                xysize (600,150)
                use ZoneText(message)
            frame:
                xysize (500,150)
                has vbox
                label _("Remerciements Spéciaux à :")
                text _("BatmanCxnt pour le {a=https://discord.gg/Zu7J7dZsQY/}Discord{/a}")
                text _("Rath98 pour la traduction Anglaise")
                text _("Betoso114 pour la traduction Espagnole")

screen ZoneText(blabla):
    viewport:
        scrollbars "vertical"
        draggable True
        mousewheel True
        arrowkeys True

        xinitial 0.0
        yinitial 0.0

        text blabla
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
