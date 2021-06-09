screen PC_dossier_perso():
    zorder 100
    use Ordi_User
    add "Images/CG/04-Ordinateur/ordinateur_subwindow.png"
    text _("Perso") xalign 0.25 yalign 0.18
    imagebutton:
        xalign 0.715
        yalign 0.18
        idle "Images/Plans/Ordinateur/exit.png"
        hover "Images/Plans/Ordinateur/exit_hover.png"
        action Return(True)

    grid 2 1:
        xalign 0.377
        yalign 0.26
        spacing 6
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action Jump("PC_perso_img_1")
            text _("Ronnie_1.png") xalign 0.5
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action Jump("PC_perso_img_2")
            text _("Ronnie_2.png") xalign 0.5

label PC_perso_img_1:
    show screen IMGshow("Images/CG/01-Personnages/001-Ronnie_Anne/ronnie-anne_selfi_1.png")
    pause
    return
label PC_perso_img_2:
    show screen IMGshow("Images/CG/01-Personnages/001-Ronnie_Anne/ronnie-anne_selfi_2.png")
    pause
    return

screen PC_fond():
    zorder 100
    use Ordi_User
    add "Images/CG/04-Ordinateur/ordinateur_subwindow.png"
    text _("Fonds d'écran") xalign 0.25 yalign 0.18
    imagebutton:
        xalign 0.715
        yalign 0.18
        idle "Images/Plans/Ordinateur/exit.png"
        hover "Images/Plans/Ordinateur/exit_hover.png"
        action Return(True)

    grid 3 2:
        xalign 0.4
        yalign 0.32
        spacing 6
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action SetVariable("PC_back", "Images/CG/04-Ordinateur/ordinateur_back_1.png")
            text _("parc.png") xalign 0.5
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action SetVariable("PC_back", "Images/CG/04-Ordinateur/ordinateur_back_2.png")
            text _("pn.png") xalign 0.5
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action SetVariable("PC_back", "Images/CG/04-Ordinateur/ordinateur_back_3.png")
            text _("soeurs.png") xalign 0.5
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action SetVariable("PC_back", "Images/CG/04-Ordinateur/ordinateur_back_4.png")
            text _("leni.png") xalign 0.5
        vbox:
            imagebutton:
                xalign 0.5
                idle "Images/Plans/Ordinateur/icone_image.png"
                hover "Images/Plans/Ordinateur/icone_image_hover.png"
                action SetVariable("PC_back", "Images/CG/04-Ordinateur/ordinateur_back_5.png")
            text _("lori.png") xalign 0.5
        null

screen PC_corbeille():
    zorder 100
    use Ordi_User
    add "Images/CG/04-Ordinateur/ordinateur_subwindow.png"
    text _("Corbeille") xalign 0.25 yalign 0.18
    imagebutton:
        xalign 0.715
        yalign 0.18
        idle "Images/Plans/Ordinateur/exit.png"
        hover "Images/Plans/Ordinateur/exit_hover.png"
        action Return(True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
