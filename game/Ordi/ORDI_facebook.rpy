screen PC_facebook():
    zorder 100
    add "Images/CG/04-Ordinateur/facebook_profil.png"

    imagebutton:
        xalign 0.4
        yalign 0.65
        idle "Images/Plans/Ordinateur/fb_com.png"
        hover "Images/Plans/Ordinateur/fb_com_hover.png"
        action ShowMenu("PC_cham_user")

    imagebutton:
        xalign 0.85
        yalign 0.8
        idle "Images/Plans/Ordinateur/pub_maria_porn.png"
        hover "Images/Plans/Ordinateur/pub_maria_porn_hover.png"
        action ShowMenu("PC_cham_user")

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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
