screen Menu_des_objets():
    modal True
    frame:
        xalign 0.3
        ypos 50
        background Frame("gui/frame_sac.png", gui.frame_borders, tile=gui.frame_tile)
        has vbox:
            ysize 500
            spacing 5
            xalign 0.5
            yalign 0.5
        if numInv == "pocheInv":
            label _("Inventaire") xalign 0.5 yalign 1.0
            grid 2 3:
                use BoutonInv(_("Objets Importants"), "pocheImp")
                use BoutonInv(_("Poche à Flipis"), "pocheFlip")
                use BoutonInv(_("Poche à Cadeaux"), "pocheCdx")
                use BoutonInv(_("Poche à Objets"), "pocheObj")
                use BoutonInv(_("Poche à Livres"), "pocheBook")
                null
        elif numInv == "pocheImp":
            label _("Objets Importants") xalign 0.5 yalign 1.0
            grid 4 2:
                spacing 10
                xalign 0.5
                yalign 0.5

                use obj_inv(3, permis, "permis", "")
                use obj_inv(3, phone, "phone", "")
                use obj_inv(3, tournevis, "tournevis", "")
                use obj_inv(3, radio, "radio", "")
                use obj_inv(3, boost_secret, "boost_secret", "")
                if coco_jambe_1 == "inpoche":
                    use obj_quete(coco_jambe_1, "coco_jambe")
                elif mom_cle == "go":
                    use obj_quete(mom_cle, "cle_rita")
                else:
                    null
                null
                null
        elif numInv == "pocheFlip":
            label _("Poche à Flipis") xalign 0.5 yalign 1.0
            grid 4 2:
                spacing 10
                xalign 0.5
                yalign 0.5

                use obj_inv(2, flipi_citron, "flipi_citron", "")
                use obj_inv(2, flipi_fraise, "flipi_fraise", "")
                use obj_inv(2, flipi_framboise_bleu, "flipi_framboise_bleu", "")
                use obj_inv(2, flipi_framboise, "flipi_framboise", "")
                use obj_inv(2, flipi_kiwi, "flipi_kiwi", "")
                use obj_inv(2, flipi_pastheque, "flipi_pastheque", "")
                use obj_inv(2, flipi_raisin, "flipi_raisin", "")
                null
        elif numInv == "pocheCdx":
            label _("Poche à Cadeaux") xalign 0.5 yalign 1.0
            grid 4 2:
                spacing 10
                xalign 0.5
                yalign 0.5

                use obj_inv(1, fleur, "fleur", "")
                use obj_inv(1, clopes, "clopes", "")
                use obj_inv(1, boucle, "boucle", "")
                use obj_inv(1, lingerie_sexy, "lingerie_sexy", "")
                use obj_inv(1, pomgirl_1, "pomgirl_1", "")
                use obj_inv(1, pomgirl_2, "pomgirl_2", "")
                use obj_inv(1, halteres, "halteres", "")
                use obj_inv(1, journal, "journal", "")
        elif numInv == "pocheObj":
            label _("Poche à Objets") xalign 0.5 yalign 1.0
            grid 6 2:
                spacing 10
                xalign 0.5
                yalign 0.5

                use obj_inv(1, mouchoir, "mouchoir", "")
                use obj_inv(1, bonbon, "bonbon", "")
                use obj_inv(1, chocolat, "chocolat", "")
                use obj_inv(1, usb, "usb", "")
                use obj_inv(1, bouteille, "bouteille", "")
                use obj_inv(1, eau, "eau", "")
                use obj_inv(1, alcool, "alcool", "")
                use obj_inv(1, boost_love, "boost_love", "")
                use obj_inv(1, boost_sex, "boost_sex", "")
                use obj_inv(1, boost_boobs, "boost_boobs", "")
                use obj_inv(1, boost_invisible, "boost_invisible", "")
                null
        elif numInv == "pocheBook":
            label _("Poche à Livres") xalign 0.5 yalign 1.0
            grid 4 1:
                spacing 10
                xalign 0.5
                yalign 0.5

                use obj_inv(1, book_1, "book_1", "")
                use obj_inv(1, book_2, "book_2", "")
                use obj_inv(1, book_3, "book_3", "")
                use obj_inv(1, book_princess_pony, "book_princess_pony", "")
        imagebutton:
            xalign 0.5
            idle "Images/Bases/Icones/sac_retour.png"
            hover "Images/Bases/Icones/sac_retour_hover.png"
            if numInv == "pocheInv":
                action Return()
            else:
                action SetVariable("numInv", "pocheInv")

screen BoutonInv(pocheName, pocheDest):
    button:
        xalign 0.5
        yalign 0.5
        frame:
            xsize 150
            background Frame("gui/frame_sac_poche.png", gui.frame_borders, tile=gui.frame_tile)
            hover_background Frame("gui/frame_hover.png", gui.frame_borders, tile=gui.frame_tile)
            has vbox:
                xalign 0.5
                yalign 0.5
            text pocheName xalign 0.5
        action SetVariable("numInv", pocheDest)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
