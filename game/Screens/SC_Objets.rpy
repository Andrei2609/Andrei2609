screen obj_shop(shop, obj_var, obj_name, obj_price):
    if user_coins >= obj_price:
        button:
            xalign 0.5
            yalign 0.5
            frame:
                xsize 150
                ysize 150
                hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
                has vbox:
                    xalign 0.5
                    yalign 0.5
                if shop == "flip":
                    add "Images/Objets/flipi/[obj_name].png"
                else:
                    add "Images/Objets/item_[obj_name].png"
                text "[obj_price] $" xalign 0.5
            if shop == "lisa":
                action SetVariable(obj_name, obj_var + 1), SetVariable("user_coins", user_coins - obj_price)
            else:
                action SetVariable(obj_name, obj_var + 1), SetVariable("user_coins", user_coins - obj_price)
    else:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 150
            ysize 150
            background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
            has vbox:
                xalign 0.5
                yalign 0.5
                spacing 5
            if shop == "lisa":
                add "Images/Objets/item_boost_no_dispo.png" xalign 0.5
                text _("pas possible") xalign 0.5
            else:
                if shop == "flip":
                    add "Images/Objets/flipi/flipi_no_dispo.png" xalign 0.5
                else:
                    add "Images/Objets/item_[obj_name]_no_dispo.png" xalign 0.5
                hbox:
                    spacing 5
                    add "Images/Bases/Icones/trop_cher.png" xalign 0.5
                    text _("trop cher") xalign 0.5

screen obj_troc(obj_var, obj_name, obj_price):
    frame:
        xsize 150
        ysize 150
        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
        if user_coins >= obj_price and bouteille > 0:
            button:
                xalign 0.5
                add "Images/Objets/item_[obj_name].png"

                action SetVariable(obj_name, obj_var + 1), SetVariable("user_coins", user_coins - obj_price), SetVariable("bouteille", bouteille - 1)
            text "[obj_price] $" xalign 0.5
        else:
            add "Images/Objets/item_boost_no_dispo.png" xalign 0.5
            text _("pas possible") xalign 0.5

screen obj_inv(obj_type, obj_var, obj_img, act):
    vbox:
        spacing 1
        if obj_var > 0 or obj_var == "inpoche":
            if obj_type == 1 or obj_type == 3:
                add "Images/Objets/item_[obj_img].png" xalign 0.5
            elif obj_type == 2:
                add "Images/Objets/flipi/[obj_img].png" xalign 0.5
            if obj_type <> 3 and obj_var <> 1:
                text "X [obj_var]" xalign 0.5
            if act <> "":
                textbutton _("Utiliser"):
                    action Jump(act)

screen obj_quete(obj_var, obj_img):
    vbox:
        spacing 1
        if obj_var == "inpoche":
            add "Images/Objets/item_[obj_img].png" xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
