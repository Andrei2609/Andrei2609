screen quit():

    add "gui/Side_menu/quit_back.png"
    label _("Êtes-vous sûr de vouloir nous quitter ?") xalign 0.5 yalign 0.1 text_size 40 text_font "FT_name.ttf"

    vbox:
        xalign 0.48
        yalign 0.6
        spacing 10
        frame:
            xalign 0.5
            textbutton _("Oui"):
                text_size 50
                action Quit(confirm=False)
        frame:
            xalign 0.5
            textbutton _("Non"):
                text_size 50
                action Return()

screen soutien():
    tag menu

    add "gui/Side_menu/soutien_back.png"
    hbox:
        xsize 1200
        ysize 100
        xalign 0.5
        yalign 0.0
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]")
        text _("Support"):
            font "FT_name.ttf"
            size 50
            xalign 1.0
            yalign 0.5

    frame:
        background None
        xalign 0.6
        yalign 0.75
        xsize 800
        ysize 300
        has vbox:
            xalign 0.5
            yalign 0.2
        label _("Vous aimez le jeu ?") xalign 0.5
        text _("Soutenez-nous sur l'une des plateformes suivantes,") xalign 0.5
        text _("afin que cette aventure continue et devienne encore meilleure !") xalign 0.5

        hbox:
            spacing 50
            xalign 0.5
            vbox:
                imagebutton:
                    xalign 0.5
                    idle "gui/Side_menu/Patreon.png"
                    hover "gui/Side_menu/Patreon_hover.png"

                    action OpenURL("https://www.patreon.com/thelionessesofsins")
                label "Patreon" xalign 0.5

            vbox:
                imagebutton:
                    xalign 0.5
                    idle "gui/Side_menu/SubscribeStar.png"
                    hover "gui/Side_menu/SubscribeStar_hover.png"

                    action OpenURL("https://www.subscribestar.com/the-lionesses-of-sins")
                label "SubscribeStar" xalign 0.5

            vbox:
                imagebutton:
                    xalign 0.5
                    idle "gui/Side_menu/PayPal.png"
                    hover "gui/Side_menu/PayPal_hover.png"

                    action OpenURL("https://paypal.me/KinouPriol?locale.x=fr_FR")
                label "PayPal" xalign 0.5
    vbox:
        xalign 0.95
        yalign 0.98
        label _("Des questions ? Besoin d'aide ?") xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/Side_menu/f95zone.png"
            hover "gui/Side_menu/f95zone_hover.png"

            action OpenURL("https://f95zone.to/threads/the-loud-house-lost-panties-v0-01-lioness-entertainment.52165/")

    vbox:
        spacing 10
        xalign 0.009
        yalign 0.99
        frame:
            textbutton _("Menu"):
                action MainMenu()
        imagebutton:
            idle "gui/Side_menu/retour.png"
            hover "gui/Side_menu/retour_hover.png"

            action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
