
screen Agenda_Ecole():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(1, "", "", _("Langue"), "", "", _("Maths"), "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(1, "", "", _("Biologie"), "", "", _("Sport"), "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(2, "", "", _("Maths"), "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(1, "", "", _("Sport"), "", "", _("Langue"), "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(1, "", "", _("Langue"), "", "", _("Biologie"), "", "", "", "", "", "", "", "", "", "")
        text _("Samedi et dimanche pas d'école.") xalign 0.5


screen Agenda_Noel():
    vbox:
        yalign 0.0
        ysize 280
        if choix_jour == 1:
            use agendaJour(1, _("9h - Langue"), "", "", "", "", _("13h - Maths"), "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 2:
            use agendaJour(1, _("9h - Biologie"), "", "", "", "", _("13h - Sport"), "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 3:
            use agendaJour(2, _("9h - Maths"), "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 4:
            use agendaJour(1, _("9h - Sport"), "", "", "", "", _("13h - Langue"), "", "", "", "", "", "", "", "", "", "")
        elif choix_jour == 5:
            use agendaJour(1, _("9h - Langue"), "", "", "", "", _("13h - Biologie"), "", "", "", "", "", "", "", "", "", "")
        text _("Bientôt Noël") xalign 0.5


screen Agenda_Vacances():
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
