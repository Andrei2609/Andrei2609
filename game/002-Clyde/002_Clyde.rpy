
define clyde = Character(
    "Clyde",
    window_background="gui/textbox/neutre.png",
    color="#582900",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

init:
    $ love_clyde_points = 15
    $ sex_clyde_points = 5

screen clyde_menu_stats():
    use boy_stats("clyde", "Clyde", _("meilleur ami"), _("Lori Loud"), _("Bobby Santiago"), "18", love_clyde_points, sex_clyde_points)

screen clyde_talk():
    use menu_talk("clyde", love_clyde_points, "clyde_menu_stats")



image Clyde = "Images/Personnages/002-Clyde/Actif/clyde_normal.png"
image Clyde_P:
    "Images/Personnages/002-Clyde/Actif/clyde_normal_P.png"
    pause .5
    "Images/Personnages/002-Clyde/Actif/clyde_normal.png"
    pause .5
    repeat
image Clyde_R = "Images/Personnages/002-Clyde/Actif/clyde_normal_R.png"
image Clyde_A = "Images/Personnages/002-Clyde/Actif/clyde_normal_A.png"
image Clyde_X = "Images/Personnages/002-Clyde/Actif/clyde_normal_X.png"
image Clyde_H = "Images/Personnages/002-Clyde/Actif/clyde_normal_H.png"
image Clyde_T = "Images/Personnages/002-Clyde/Actif/clyde_normal_T.png"
image Clyde_M = "Images/Personnages/002-Clyde/Actif/clyde_normal_M.png"
image Clyde_C = "Images/Personnages/002-Clyde/Actif/clyde_normal_C.png"
image Clyde_S = "Images/Personnages/002-Clyde/Actif/clyde_normal_S.png"


image Clyde_job = "Images/Personnages/002-Clyde/Actif/clyde_job.png"
image Clyde_job_P:
    "Images/Personnages/002-Clyde/Actif/clyde_job_P.png"
    pause .5
    "Images/Personnages/002-Clyde/Actif/clyde_job.png"
    pause .5
    repeat



image I_Clyde = "Images/Personnages/002-Clyde/Inactif/clyde_normal.png"


image I_Clyde_job = "Images/Personnages/002-Clyde/Inactif/clyde_job.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
