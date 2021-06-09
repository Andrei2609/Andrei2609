
define l2 = Character(
    "Leni",
    window_background="gui/textbox/l2.png",
    color="#00FF93",
    what_outlines=[( 1, "#00FF93", 0, 0 )]
    )

screen l2_talk():
    use menu_talk(l2, love_l2_points, sex_l2_points, "l2_menu_stats")

screen l2_menu_stats():
    use girl_stats("l2", l2_win, "Leni", _("la stupide"), _("Les magazines"), _("Araignées"), "21", love_l2_points, sex_l2_points, l2_cum)

screen l2_option():
    use menu_shop_talk(l2, love_l2_points, sex_l2_points, "vet_l2_talk", "Vet_shop_prod", "Vet_shop")

init:
    $ love_l2_points = 10
    $ sex_l2_points = 0
    $ l2_cum = 0


    $ l2_win = False
    $ l2_win_job = False
    $ l2_win_plage = False
    $ l2_win_shower = False
    $ l2_win_sleep = False


    $ l2_halloween_2020 = False
    $ l2_fiesta = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
