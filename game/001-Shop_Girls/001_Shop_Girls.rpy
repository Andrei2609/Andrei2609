
define shop_girl_1 = Character(
    "Caissière",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_shop_girl_1_points = 5
    $ sex_shop_girl_1_points = 0
    $ shop_girl_1_win = False
    $ shop_girl_1_tel = False
    $ shop_girl_1_key = False

screen shop_girl_1_menu_stats():
    use girl_stats("shop_girl_1", shop_girl_1_win, _("la Caissière"), _("la caissière"), _("La moto"), _("Le travail"), "28", love_shop_girl_1_points, sex_shop_girl_1_points, "")

screen shop_girl_1_talk():
    use menu_talk(shop_girl_1, love_shop_girl_1_points, sex_shop_girl_1_points, "shop_girl_1_menu_stats")

screen shop_girl_1_option():
    use menu_shop_talk(shop_girl_1, love_shop_girl_1_points, sex_shop_girl_1_points, "general_girl_talk", "General_shop_prod", "General_shop")



define electro_girl = Character(
    "Vera",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_electro_girl_points = 5
    $ sex_electro_girl_points = 0
    $ electro_girl_win = False
    $ electro_girl_tel = False
    $ electro_girl_key = False

screen electro_girl_menu_stats():
    use girl_stats("electro_girl", electro_girl_win, "Vera", _("la vendeuse High-Tech"), _("Les robots"), _("La Musique"), "26", love_electro_girl_points, sex_electro_girl_points, "")

screen electro_girl_talk():
    use menu_talk(electro_girl, love_electro_girl_points, sex_electro_girl_points, "electro_girl_menu_stats")

screen electro_girl_option():
    use menu_shop_talk(electro_girl, love_electro_girl_points, sex_electro_girl_points, "electro_girl_talk", "Electro_shop_prod", "Electro_shop")



define BD_girl = Character(
    "Wendy",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_BD_girl_points = 5
    $ sex_BD_girl_points = 0
    $ BD_girl_win = False
    $ BD_girl_tel = False
    $ BD_girl_key = False

screen BD_girl_menu_stats():
    use girl_stats("BD_girl", BD_girl_win, "Wendy", _("la libraire"), _("Ace Savy"), _("La Vielle Dame"), "32", love_BD_girl_points, sex_BD_girl_points, "")

screen BD_girl_talk():
    use menu_talk(BD_girl, love_BD_girl_points, sex_BD_girl_points, "BD_girl_menu_stats")

screen BD_girl_option():
    use menu_shop_talk(BD_girl, love_BD_girl_points, sex_BD_girl_points, "BD_girl_talk", "BD_shop_prod", "BD_shop")



define candy_girl = Character(
    "Candice",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_candy_girl_points = 5
    $ sex_candy_girl_points = 0
    $ candy_girl_win = False
    $ candy_girl_tel = False
    $ candy_girl_key = False

screen candy_girl_menu_stats():
    use girl_stats("candy_girl", candy_girl_win, "Candice", _("la marchande de bonbons"), _("Les sucettes"), _("Le poisson"), "19", love_candy_girl_points, sex_candy_girl_points, "")

screen candy_girl_talk():
    use menu_talk(candy_girl, love_candy_girl_points, sex_candy_girl_points, "candy_girl_menu_stats")

screen candy_girl_option():
    use menu_shop_talk(candy_girl, love_candy_girl_points, sex_candy_girl_points, "candy_girl_talk", "Bonbon_shop_prod", "Bonbon_shop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
