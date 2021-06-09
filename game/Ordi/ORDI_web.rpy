init:
    $ PC_webBack = "Images/CG/04-Ordinateur/ordinateur_webback_1.png"

image PC_webBack_2 = PC_webBack

screen PC_web():
    zorder 100
    add PC_webBack

    vbox:
        xalign 0.48
        yalign 0.4
        spacing 10
        add "Images/Plans/Ordinateur/google_logo.png" xalign 0.5
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Ordinateur/google_bar.png"
            hover "Images/Plans/Ordinateur/google_bar_hover.png"
            action Jump("PC_web_search")

    add "Images/CG/04-Ordinateur/ordinateur_window.png"
    imagebutton:
        xalign 0.883
        yalign 0.15
        idle "Images/Plans/Ordinateur/exit.png"
        hover "Images/Plans/Ordinateur/exit_hover.png"
        action Return(True)
    add "Images/CG/04-Ordinateur/ordinateur_ecran.png"
    textbutton _("Retour"):
        xalign 0.1
        yalign 0.93
        action Jump("PC_cham_user")

label PC_web_search:
    hide screen PC_web
    show PC_webBack_2
    show PC_front
    menu:
        "Faire une recherche pour l'école" if True:
            return
        "Regarder du porno" if True:
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
