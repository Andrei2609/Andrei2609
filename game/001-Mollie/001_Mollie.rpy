define mollie = Character(
    "Mollie",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_mollie_points = 1
    $ sex_mollie_points = 10
    $ mollie_win = False
    $ mollie_tel = False
    $ mollie_key = False

screen mollie_menu_stats():
    use girl_stats("mollie", mollie_win, "Mollie", _("la chaudasse"), _("le sexe"), _("les petites bites"), "18", love_mollie_points, sex_mollie_points, "")

screen mollie_talk():
    use menu_talk(mollie, love_mollie_points, sex_mollie_points, "mollie_menu_stats")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
