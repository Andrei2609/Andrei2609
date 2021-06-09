image PC_front = "Images/CG/04-Ordinateur/ordinateur_ecran.png"

init:
    $ PC_back = "Images/CG/04-Ordinateur/ordinateur_back_1.png"

label PC_cham_user:
    call screen Ordi_User

screen Ordi_User():
    zorder 100
    add PC_back

    vbox:
        xalign 0.8
        yalign 0.2
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Ordinateur/icone_dossier.png"
            hover "Images/Plans/Ordinateur/icone_dossier_hover.png"
            action ShowMenu("PC_dossier_perso")
        text _("Perso") xalign 0.5

    vbox:
        xalign 0.1
        yalign 0.2
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Ordinateur/icone_web.png"
            hover "Images/Plans/Ordinateur/icone_web_hover.png"
            action ShowMenu("PC_web")
        text _("Navigateur") xalign 0.5

    vbox:
        xalign 0.25
        yalign 0.2
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Ordinateur/icone_facebook.png"
            hover "Images/Plans/Ordinateur/icone_facebook_hover.png"
            action ShowMenu("PC_facebook")
        text _("Facebook") xalign 0.5

    vbox:
        xalign 0.1
        yalign 0.36
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Ordinateur/icone_dossier.png"
            hover "Images/Plans/Ordinateur/icone_dossier_hover.png"
            action ShowMenu("PC_fond")
        text _("Fonds d'écran") xalign 0.5

    vbox:
        xalign 0.85
        yalign 0.85
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Ordinateur/icone_poubelle.png"
            hover "Images/Plans/Ordinateur/icone_poubelle_hover.png"
            action ShowMenu("PC_corbeille")
        text _("Corbeille") xalign 0.5

    add "Images/CG/04-Ordinateur/ordinateur_ecran.png"

    textbutton _("Retour"):
        xalign 0.1
        yalign 0.93
        action Jump("cham_user_2")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
