
screen planning_l5():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(1, "Entrainement", "", "Au Lycée", "", "", "Au Lycée", "", "Dans sa chambre", "", "", "", "Dans sa chambre", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(1, "Entrainement", "", "Au Lycée", "", "", "Au Lycée", "", "Dans sa chambre", "", "", "", "Dans sa chambre", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(2, "Entrainement", "", "Au Lycée", "", "", "Dans sa chambre", "", "", "", "", "", "Dans sa chambre", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(1, "Entrainement", "", "Au Lycée", "", "", "Au Lycée", "", "Dans sa chambre", "", "", "", "Dans sa chambre", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(1, "Entrainement", "", "Au Lycée", "", "", "Au Lycée", "", "Dans sa chambre", "", "", "", "Dans sa chambre", "", "", "", "")
        elif choix_jour == 6:
            use agendaJour(0, "Entrainement", "", "Dans sa chambre", "", "", "", "", "Dans sa chambre", "", "", "", "Dans sa chambre", "", "", "", "")
        elif choix_jour == 7:
            use agendaJour(0, "Entrainement", "", "Dans sa chambre", "", "", "", "", "Dans sa chambre", "", "", "", "Dans sa chambre", "", "", "", "")
        text _("Lynn s'entraine dans le salon tout les matins.") xalign 0.5 text_align 0.5


screen planning_l5_noel():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 6:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 7:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        text _("Noël approche...") xalign 0.5 text_align 0.5


screen planning_l5_vacances():
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
