define fiona = Character(
    "Fiona",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_fiona_points = 5
    $ sex_fiona_points = 0
    $ fiona_win = False
    $ fiona_tel = False
    $ fiona_key = False

screen fiona_menu_stats():
    use girl_stats("fiona", fiona_win, "fiona", _("vendeuse de vêtements"), _("La mode"), _("Les gamins"), "21", love_fiona_points, sex_fiona_points, "")

screen fiona_talk():
    use menu_talk(fiona, love_fiona_points, sex_fiona_points, "fiona_menu_stats")

screen fiona_option():
    use menu_shop_talk(fiona, love_fiona_points, sex_fiona_points, "vet_fiona_talk", "Vet_shop_prod", "Vet_shop")


image caisse_fiona = "Images/CG/01-Personnages/001-Autres/fiona_caisse.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
