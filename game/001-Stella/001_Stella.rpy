define stella = Character(
    "Stella",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_stella_points = 15
    $ sex_stella_points = 5
    $ stella_win = False
    $ stella_tel = False
    $ stella_key = False
    $ casier_key_2 = False

screen stella_menu_stats():
    use girl_stats("stella", stella_win, "Stella", _("meilleure amie"), _("essayer de nouveaux trucs"), _("la solitude"), "18", love_stella_points, sex_stella_points, "")

screen stella_talk():
    use menu_talk(stella, love_stella_points, sex_stella_points, "stella_menu_stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
