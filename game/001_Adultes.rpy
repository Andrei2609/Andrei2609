
define journaliste = Character(
    "Katherine Mulligan",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define maria = Character(
    "Maria Santiago",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define nurse = Character(
    _("Infirmière Patty"),
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )


define prof1 = Character(
    _("Madame Johnson"),
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define prof2 = Character(
    _("Madame Dimartino"),
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )
define prof3 = Character(
    _("Madame Shrinivas"),
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_prof1_points = 1
    $ sex_prof1_points = 10
    $ prof1_win = False
    $ prof1_tel = False
    $ prof1_key = False

    $ love_prof2_points = 1
    $ sex_prof2_points = 10
    $ prof2_win = False
    $ prof2_tel = False
    $ prof2_key = False

    $ love_prof3_points = 1
    $ sex_prof3_points = 10
    $ prof3_win = False
    $ prof3_tel = False
    $ prof3_key = False

    $ love_nurse_points = 1
    $ sex_nurse_points = 10
    $ nurse_win = False
    $ nurse_tel = False
    $ nurse_key = False

    $ love_maria_points = 1
    $ sex_maria_points = 10
    $ maria_win = False
    $ maria_tel = False
    $ maria_key = False

    $ love_journaliste_points = 1
    $ sex_journaliste_points = 10
    $ journaliste_win = False
    $ journaliste_tel = False
    $ journaliste_key = False

screen prof1_menu_stats():
    use girl_stats("prof1", prof1_win, "Madame Johnson", _("la prof"), _("???"), _("???"), "40", love_prof1_points, sex_prof1_points, "")

screen prof2_menu_stats():
    use girl_stats("prof2", prof2_win, "Madame Dimartino", _("la prof"), _("???"), _("???"), "40", love_prof2_points, sex_prof2_points, "")

screen prof3_menu_stats():
    use girl_stats("prof3", prof3_win, "Madame Shrinivas", _("la prof"), _("???"), _("???"), "40", love_prof3_points, sex_prof3_points, "")

screen nurse_menu_stats():
    use girl_stats("nurse", nurse_win, "Infirmière Patty", _("l'infirmière"), _("???"), _("???"), "40", love_nurse_points, sex_nurse_points, "")

screen maria_menu_stats():
    use girl_stats("maria", maria_win, "Maria Santiago", _("la maman de Ronnie-Anne"), _("???"), _("???"), "40", love_maria_points, sex_maria_points, "")

screen journaliste_menu_stats():
    use girl_stats("journaliste", journaliste_win, "Katherine Mulligan", _("la journaliste"), _("???"), _("???"), "40", love_journaliste_points, sex_journaliste_points, "")



image nurse = "Images/Personnages/001-Adultes/Actif/nurse_normal.png"
image nurse_P:
    "Images/Personnages/001-Adultes/Actif/nurse_normal_P.png"
    pause .5
    "Images/Personnages/001-Adultes/Actif/nurse_normal.png"
    pause .5
    repeat

image I_nurse = "Images/Personnages/001-Adultes/Inactif/nurse_normal.png"



image prof1 = "Images/Personnages/001-Adultes/Actif/prof_1_normal.png"
image prof1_P:
    "Images/Personnages/001-Adultes/Actif/prof_1_normal_P.png"
    pause .5
    "Images/Personnages/001-Adultes/Actif/prof_1_normal.png"
    pause .5
    repeat
image prof2 = "Images/Personnages/001-Adultes/Actif/prof_2_normal.png"
image prof2_P:
    "Images/Personnages/001-Adultes/Actif/prof_2_normal_P.png"
    pause .5
    "Images/Personnages/001-Adultes/Actif/prof_2_normal.png"
    pause .5
    repeat
image prof3 = "Images/Personnages/001-Adultes/Actif/prof_3_normal.png"
image prof3_P:
    "Images/Personnages/001-Adultes/Actif/prof_3_normal_P.png"
    pause .5
    "Images/Personnages/001-Adultes/Actif/prof_3_normal.png"
    pause .5
    repeat


image I_prof1 = "Images/Personnages/001-Adultes/Inactif/prof_1_normal.png"
image I_prof2 = "Images/Personnages/001-Adultes/Inactif/prof_2_normal.png"
image I_prof3 = "Images/Personnages/001-Adultes/Inactif/prof_3_normal.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
