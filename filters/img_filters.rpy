init:
    $ filters["image__filter_sepia"] = u"Ностальгическое Лето"
    $ filters["image__filter_gray"] = u"Чёрно-белое Лето"
    $ filters["image__filter_map"] = u"27-цветное Лето"

python early:
    def lb__recolor(im_op):
        for id, img in renpy.display.image.images.iteritems():
            try:
                for i,(c,sub) in enumerate(img.child.args[0]):
                    img.child.args[0][i] = (c,im_op(sub))
            except:
                try:
                    renpy.display.image.images[id] = im_op(img)
                except:
                    "TODO"
        for id in store.map_pics:
            store.map_pics[id] = im_op(store.map_pics[id])


    def image__filter_sepia():
        lb__recolor(im.Sepia)
        config.overlay_functions.append(lambda:ui.image("filters/sepia.png"))

    m = chr(0)*85+chr(128)*86+chr(255)*85
    image__filter_map   = lambda: lb__recolor(lambda i: im.Map(i,m,m,m))

    image__filter_gray = lambda: lb__recolor(im.Grayscale)
    image__filter_hue   = lambda: lb__recolor(lambda i: im.MatrixColor(i,im.matrix.hue(180)))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
