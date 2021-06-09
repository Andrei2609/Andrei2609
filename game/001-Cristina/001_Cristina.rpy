define cristina = Character(
    "Cristina",
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_cristina_points = 5
    $ sex_cristina_points = 0
    $ cristina_win = False
    $ cristina_tel = False
    $ cristina_key = False
    $ casier_key_6 = False

screen cristina_menu_stats():
    use girl_stats("cristina", cristina_win, "Cristina", _("premier amour de Lincoln"), _("???"), _("???"), "18", love_cristina_points, sex_cristina_points, "")

screen cristina_talk():
    use menu_talk(cristina, love_cristina_points, sex_cristina_points, "cristina_menu_stats")


image cristina_WC_peek = "Images/CG/01-Personnages/001-Cristina/cristina_wc.png"

image cristina_WC_boobs_size:
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_1.png"
    pause .5
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_2.png"
    pause .3
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_3.png"
    pause .2
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_4.png"
    pause .2
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_3.png"
    pause .2
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_4.png"
    pause .2
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_3.png"
    pause .3
    "Images/CG/01-Personnages/001-Cristina/wc_boobs_size_2.png"
    pause .3
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
