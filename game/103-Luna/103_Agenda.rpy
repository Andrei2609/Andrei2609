
screen planning_l3():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(0, "", "", "Travaille", "", "", "Travaille", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(0, "", "", "Travaille", "", "", "Travaille", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(0, "", "", "Travaille", "", "", "Travaille", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(0, "", "", "Travaille", "", "", "Travaille", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(0, "", "", "Travaille", "", "", "Travaille", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 6:
            use agendaJour(0, "", "", "Travaille", "", "", "Travaille", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 7:
            use agendaJour(0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        text _("...") xalign 0.5 text_align 0.5


screen planning_l3_noel():
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


screen planning_l3_vacances():
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
