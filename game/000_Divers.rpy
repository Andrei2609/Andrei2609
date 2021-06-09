
image fig_R = "Images/Personnages/000-Intervenants/Actif/figurant_R.png"
image fig_L = "Images/Personnages/000-Intervenants/Actif/figurant_L.png"
image I_fig_R = "Images/Personnages/000-Intervenants/Inactif/figurant_R.png"
image I_fig_L = "Images/Personnages/000-Intervenants/Inactif/figurant_L.png"

define sis_loud = Character(
    _("Les soeurs Loud"),
    window_background="gui/textbox/neutre.png",
    color="#000000",
    what_outlines=[( 1, "#FFFFFF", 0, 0 )]
    )

define nar = Character(
    None,
    window_background = None,
    what_size=30,
    what_outlines=[( 2, "#ffffff", 0, 0 )],
    what_yalign=0,
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle'
    )

define tel = Character(
    None,
    what_yalign=0.1,
    what_xalign=0.65,
    what_font="FT_Open24.ttf",
    window_background="gui/textbox/phone.png"
    )

image bus = "Images/Personnages/000-Vehicules/bus.png"


image coco_jambe = "Images/Objets/item_coco_jambe.png"
image mom_cles = "Images/Objets/item_cle_rita.png"
image l1_phone = "Images/Objets/item_lori_phone.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
