
define user = Character(
    "Lincoln",
    window_background="gui/textbox/user.png",
    color="#FF5733",
    what_outlines=[( 1, "#FF5733", 0, 0 )]
    )

init:
    $ vie_points = 100
    $ sex_points = 5
    $ int_points = 0
    $ force_points = 1
    $ warn_loud_points = 0
    $ warn_school_points = 0
    $ warn_ville_points = 0
    $ school_points = 50
    $ user_room = False
    $ user_coins = 0
    $ permis = False


image INTRO_user = "Images/CG/00-Histoire/mini_intro/1_user/corps.png"

image sleep_user = "Images/CG/05-User/user_sleep.png"
image masturbe_user = "Images/CG/05-User/user_masturbe.png"
image parc_cool_user = "Images/CG/05-User/user_parc_1.png"
image eat_user_home = "Images/CG/05-User/user_eat_home.png"
image eat_user_school = "Images/CG/05-User/user_eat_school.png"

image miam_bol_1 = "Images/CG/05-User/food_1.png"


image Lincoln_grab_ass_1 = "Images/CG/01-Personnages/106-Lincoln/user_grab_ass_1.png"
image Lincoln_grab_ass_2 = "Images/CG/01-Personnages/106-Lincoln/user_grab_ass_2.png"
image Lincoln_claque = "Images/CG/01-Personnages/106-Lincoln/user_claque.png"


image Intro_Lincoln_salut = "Images/Personnages/106-Lincoln/Intro/lincoln_salut.png"
image Intro_Lincoln_P:
    "Images/Personnages/106-Lincoln/Intro/lincoln_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Intro/lincoln.png"
    pause .5
    repeat
image Intro_Lincoln_vieux_P:
    "Images/Personnages/106-Lincoln/Intro/lincoln_normal_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Intro/lincoln_normal.png"
    pause .5
    repeat
image Intro_Lincoln_S = "Images/Personnages/106-Lincoln/Intro/lincoln_S.png"
image Intro_Lincoln = "Images/Personnages/106-Lincoln/Intro/lincoln.png"



image user_Neutre_talk:
    "Images/Personnages/nouveau/user/Expression/Neutre/0.png"
    pause .5
    "Images/Personnages/nouveau/user/Expression/Neutre/1.png"
    pause .5
    repeat

image Lincoln = "Images/Personnages/106-Lincoln/Actif/lincoln_normal.png"
image Lincoln_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_normal_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_normal.png"
    pause .5
    repeat
image Lincoln_R = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_R.png"
image Lincoln_A = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_A.png"
image Lincoln_X = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_X.png"
image Lincoln_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_normal_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_normal_XA.png"
    pause .5
    repeat
image Lincoln_H = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_H.png"
image Lincoln_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_normal_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_normal_H2.png"
    pause .2
    repeat
image Lincoln_T = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_T.png"
image Lincoln_M = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_M.png"
image Lincoln_C = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_C.png"
image Lincoln_S = "Images/Personnages/106-Lincoln/Actif/lincoln_normal_S.png"


image Lincoln_nu = "Images/Personnages/106-Lincoln/Actif/lincoln_nu.png"
image Lincoln_nu_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_nu_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_nu.png"
    pause .5
    repeat
image Lincoln_nu_R = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_R.png"
image Lincoln_nu_A = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_A.png"
image Lincoln_nu_X = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_X.png"
image Lincoln_nu_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_nu_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_nu_XA.png"
    pause .5
    repeat
image Lincoln_nu_H = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_H.png"
image Lincoln_nu_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_nu_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_nu_H2.png"
    pause .2
    repeat
image Lincoln_nu_T = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_T.png"
image Lincoln_nu_M = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_M.png"
image Lincoln_nu_C = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_C.png"
image Lincoln_nu_S = "Images/Personnages/106-Lincoln/Actif/lincoln_nu_S.png"


image Lincoln_slip = "Images/Personnages/106-Lincoln/Actif/lincoln_slip.png"
image Lincoln_slip_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_slip_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_slip.png"
    pause .5
    repeat
image Lincoln_slip_R = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_R.png"
image Lincoln_slip_A = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_A.png"
image Lincoln_slip_X = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_X.png"
image Lincoln_slip_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_slip_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_slip_XA.png"
    pause .5
    repeat
image Lincoln_slip_H = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_H.png"
image Lincoln_slip_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_slip_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_slip_H2.png"
    pause .2
    repeat
image Lincoln_slip_T = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_T.png"
image Lincoln_slip_M = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_M.png"
image Lincoln_slip_C = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_C.png"
image Lincoln_slip_S = "Images/Personnages/106-Lincoln/Actif/lincoln_slip_S.png"


image Lincoln_slipA = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA.png"
image Lincoln_slipA_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_slipA.png"
    pause .5
    repeat
image Lincoln_slipA_R = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_R.png"
image Lincoln_slipA_A = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_A.png"
image Lincoln_slipA_X = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_X.png"
image Lincoln_slipA_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_XA.png"
    pause .5
    repeat
image Lincoln_slipA_H = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_H.png"
image Lincoln_slipA_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_H2.png"
    pause .2
    repeat
image Lincoln_slipA_T = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_T.png"
image Lincoln_slipA_M = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_M.png"
image Lincoln_slipA_C = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_C.png"
image Lincoln_slipA_S = "Images/Personnages/106-Lincoln/Actif/lincoln_slipA_S.png"


image Lincoln_class = "Images/Personnages/106-Lincoln/Actif/lincoln_class.png"
image Lincoln_class_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_class_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_class.png"
    pause .5
    repeat
image Lincoln_class_R = "Images/Personnages/106-Lincoln/Actif/lincoln_class_R.png"
image Lincoln_class_A = "Images/Personnages/106-Lincoln/Actif/lincoln_class_A.png"
image Lincoln_class_X = "Images/Personnages/106-Lincoln/Actif/lincoln_class_X.png"
image Lincoln_class_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_class_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_class_XA.png"
    pause .5
    repeat
image Lincoln_class_H = "Images/Personnages/106-Lincoln/Actif/lincoln_class_H.png"
image Lincoln_class_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_class_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_class_H2.png"
    pause .2
    repeat
image Lincoln_class_T = "Images/Personnages/106-Lincoln/Actif/lincoln_class_T.png"
image Lincoln_class_M = "Images/Personnages/106-Lincoln/Actif/lincoln_class_M.png"
image Lincoln_class_C = "Images/Personnages/106-Lincoln/Actif/lincoln_class_C.png"
image Lincoln_class_S = "Images/Personnages/106-Lincoln/Actif/lincoln_class_S.png"


image Lincoln_classA = "Images/Personnages/106-Lincoln/Actif/lincoln_classA.png"
image Lincoln_classA_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_classA_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_classA.png"
    pause .5
    repeat
image Lincoln_classA_R = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_R.png"
image Lincoln_classA_A = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_A.png"
image Lincoln_classA_X = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_X.png"
image Lincoln_classA_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_classA_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_classA_XA.png"
    pause .5
    repeat
image Lincoln_classA_H = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_H.png"
image Lincoln_classA_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_classA_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_classA_H2.png"
    pause .2
    repeat
image Lincoln_classA_T = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_T.png"
image Lincoln_classA_M = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_M.png"
image Lincoln_classA_C = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_C.png"
image Lincoln_classA_S = "Images/Personnages/106-Lincoln/Actif/lincoln_classA_S.png"


image Lincoln_hiver = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver.png"
image Lincoln_hiver_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_hiver.png"
    pause .5
    repeat
image Lincoln_hiver_R = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_R.png"
image Lincoln_hiver_A = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_A.png"
image Lincoln_hiver_X = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_X.png"
image Lincoln_hiver_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_XA.png"
    pause .5
    repeat
image Lincoln_hiver_H = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_H.png"
image Lincoln_hiver_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_H2.png"
    pause .2
    repeat
image Lincoln_hiver_T = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_T.png"
image Lincoln_hiver_M = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_M.png"
image Lincoln_hiver_C = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_C.png"
image Lincoln_hiver_S = "Images/Personnages/106-Lincoln/Actif/lincoln_hiver_S.png"


image Lincoln_ete = "Images/Personnages/106-Lincoln/Actif/lincoln_ete.png"
image Lincoln_ete_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_ete_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_ete.png"
    pause .5
    repeat
image Lincoln_ete_R = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_R.png"
image Lincoln_ete_A = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_A.png"
image Lincoln_ete_X = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_X.png"
image Lincoln_ete_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_ete_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_ete_XA.png"
    pause .5
    repeat
image Lincoln_ete_H = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_H.png"
image Lincoln_ete_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_ete_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_ete_H2.png"
    pause .2
    repeat
image Lincoln_ete_T = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_T.png"
image Lincoln_ete_M = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_M.png"
image Lincoln_ete_C = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_C.png"
image Lincoln_ete_S = "Images/Personnages/106-Lincoln/Actif/lincoln_ete_S.png"


image Lincoln_sport = "Images/Personnages/106-Lincoln/Actif/lincoln_sport.png"
image Lincoln_sport_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_sport_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_sport.png"
    pause .5
    repeat
image Lincoln_sport_R = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_R.png"
image Lincoln_sport_A = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_A.png"
image Lincoln_sport_X = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_X.png"
image Lincoln_sport_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_sport_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_sport_XA.png"
    pause .5
    repeat
image Lincoln_sport_H = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_H.png"
image Lincoln_sport_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_sport_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_sport_H2.png"
    pause .2
    repeat
image Lincoln_sport_T = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_T.png"
image Lincoln_sport_M = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_M.png"
image Lincoln_sport_C = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_C.png"
image Lincoln_sport_S = "Images/Personnages/106-Lincoln/Actif/lincoln_sport_S.png"


image Lincoln_swim = "Images/Personnages/106-Lincoln/Actif/lincoln_swim.png"
image Lincoln_swim_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_swim_P.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_swim.png"
    pause .5
    repeat
image Lincoln_swim_R = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_R.png"
image Lincoln_swim_A = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_A.png"
image Lincoln_swim_X = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_X.png"
image Lincoln_swim_X_P:
    "Images/Personnages/106-Lincoln/Actif/lincoln_swim_XP.png"
    pause .5
    "Images/Personnages/106-Lincoln/Actif/lincoln_swim_XA.png"
    pause .5
    repeat
image Lincoln_swim_H = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_H.png"
image Lincoln_swim_Ha:
    "Images/Personnages/106-Lincoln/Actif/lincoln_swim_H1.png"
    pause .2
    "Images/Personnages/106-Lincoln/Actif/lincoln_swim_H2.png"
    pause .2
    repeat
image Lincoln_swim_T = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_T.png"
image Lincoln_swim_M = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_M.png"
image Lincoln_swim_C = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_C.png"
image Lincoln_swim_S = "Images/Personnages/106-Lincoln/Actif/lincoln_swim_S.png"



image I_Lincoln = "Images/Personnages/106-Lincoln/Inactif/lincoln_normal.png"
image I_Lincoln_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_normal_X.png"


image I_Lincoln_nu = "Images/Personnages/106-Lincoln/Inactif/lincoln_nu.png"
image I_Lincoln_nu_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_nu_X.png"


image I_Lincoln_slip = "Images/Personnages/106-Lincoln/Inactif/lincoln_slip.png"
image I_Lincoln_slip_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_slip_X.png"


image I_Lincoln_slipA = "Images/Personnages/106-Lincoln/Inactif/lincoln_slipA.png"
image I_Lincoln_slipA_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_slipA_X.png"


image I_Lincoln_class = "Images/Personnages/106-Lincoln/Inactif/lincoln_class.png"
image I_Lincoln_class_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_class_X.png"


image I_Lincoln_classA = "Images/Personnages/106-Lincoln/Inactif/lincoln_classA.png"
image I_Lincoln_classA_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_classA_X.png"


image I_Lincoln_hiver = "Images/Personnages/106-Lincoln/Inactif/lincoln_hiver.png"
image I_Lincoln_hiver_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_hiver_X.png"


image I_Lincoln_ete = "Images/Personnages/106-Lincoln/Inactif/lincoln_ete.png"
image I_Lincoln_ete_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_ete_X.png"


image I_Lincoln_sport = "Images/Personnages/106-Lincoln/Inactif/lincoln_sport.png"
image I_Lincoln_sport_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_sport_X.png"


image I_Lincoln_swim = "Images/Personnages/106-Lincoln/Inactif/lincoln_swim.png"
image I_Lincoln_swim_X = "Images/Personnages/106-Lincoln/Inactif/lincoln_swim_X.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
