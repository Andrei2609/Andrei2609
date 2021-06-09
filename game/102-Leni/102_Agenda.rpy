
screen planning_l2():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1 or choix_jour == 2 or choix_jour == 4 or choix_jour == 5:
            use agendaJour(0, _("Prend sa douche"), _("Dans sa chambre"), "", "", "", "Travaille", "", _("Regarde son émission"), _("Dans sa chambre"), _("Prend sa douche"), _("Dans sa chambre"), _("Dans sa chambre"), "", "", _("Au lit"), "")
        elif choix_jour == 3:
            use agendaJour(0, _("Prend sa douche"), _("Dans sa chambre"), "", "", "", _("Dans sa chambre"), _("Travaille"), "", "", "", "", _("Prend sa douche"), _("Dans sa chambre"), "", _("Au lit"), "")
        elif choix_jour == 6:
            use agendaJour(0, "", "", _("Se Reveille"), _("Prend son petit dej"), _("Prend sa douche"), _("Dans sa chambre"), _("Regarde son émission"), _("Travaille"), "", "", "", _("Dans le jardin"), _("Prend sa douche"), _("Soirée entre filles"), _("Au lit"), "")
        elif choix_jour == 7:
            use agendaJour(0, "", "", _("Se Reveille"), _("Prend son petit dej"), _("Prend sa douche"), _("Dans sa chambre"), _("S'amuse à la plage"), "", "", _("Prend sa douche"), _("Dans sa chambre"), _("Dans sa chambre"), "", "", _("Au lit"), "")
        text _("Leni prend une douche\n2 fois par jour.") xalign 0.5 text_align 0.5


screen planning_l2_noel():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 6:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 7:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        text _("Noël approche...") xalign 0.5 text_align 0.5


screen planning_l2_vacances():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 6:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 7:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        text _("C'est les vacances") xalign 0.5 text_align 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
