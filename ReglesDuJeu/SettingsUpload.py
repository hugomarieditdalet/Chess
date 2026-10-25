import pygame as py

boardSide = 700
settingsSide = 200
numberSize = 20
pointRadius = boardSide/36
side = boardSide//8

py.init()
py.display.set_caption("Chess")
screen = py.display.set_mode((boardSide + settingsSide,boardSide))


#------- Black Pieces ------- #

br= py.image.load("img/br.png")
br= py.transform.scale(br, (boardSide//8,boardSide//8))

bn= py.image.load("img/bn.png")
bn= py.transform.scale(bn, (boardSide//8,boardSide//8))

bb= py.image.load("img/bb.png")
bb= py.transform.scale(bb, (boardSide//8,boardSide//8))

bk= py.image.load("img/bk.png")
bk= py.transform.scale(bk, (boardSide//8,boardSide//8))
bq= py.image.load("img/bq.png")
bq= py.transform.scale(bq, (boardSide//8,boardSide//8))
bq= py.image.load("img/bq.png")
bq= py.transform.scale(bq, (boardSide//8,boardSide//8))

bp= py.image.load("img/bp.png")
bp= py.transform.scale(bp, (boardSide//8,boardSide//8))

#---------White Pieces ---------- #

wr= py.image.load("img/wr.png")
wr= py.transform.scale(wr, (boardSide//8,boardSide//8))

wn= py.image.load("img/wn.png")
wn= py.transform.scale(wn, (boardSide//8,boardSide//8))

wb= py.image.load("img/wb.png")
wb= py.transform.scale(wb, (boardSide//8,boardSide//8))

wk= py.image.load("img/wk.png")
wk= py.transform.scale(wk, (boardSide//8,boardSide//8))

wq= py.image.load("img/wq.png")
wq= py.transform.scale(wq, (boardSide//8,boardSide//8))

wp= py.image.load("img/wp.png")
wp= py.transform.scale(wp, (boardSide//8,boardSide//8))

promotionWhite = [wq,wn,wr,wb]
promotionBlack = [bq,bn,br,bb]

#------------------- Numbers ----------------------- #

one =  py.font.SysFont(None,numberSize)
one = one.render("1", True, (0,0,0))

two =  py.font.SysFont(None,numberSize)
two = two.render("2", True, (0,0,0))

three =  py.font.SysFont(None,numberSize)
three = three.render("3", True, (0,0,0))

four =  py.font.SysFont(None,numberSize)
four = four.render("4", True, (0,0,0))

five =  py.font.SysFont(None,numberSize)
five = five.render("5", True, (0,0,0))

six =  py.font.SysFont(None,numberSize)
six = six.render("6", True, (0,0,0))

seven =  py.font.SysFont(None,numberSize)
seven = seven.render("7", True, (0,0,0))

eight =  py.font.SysFont(None,numberSize)
eight = eight.render("8", True, (0,0,0))

numbers = [one,two,three,four,five,six,seven,eight]


#-------------------Letters-----------------------#

a =  py.font.SysFont(None,numberSize)
a =  a.render("A", True, (0,0,0))

b =  py.font.SysFont(None,numberSize)
b =  b.render("B", True, (0,0,0))

c =  py.font.SysFont(None,numberSize)
c =  c.render("C", True, (0,0,0))

d =  py.font.SysFont(None,numberSize)
d =  d.render("D", True, (0,0,0))

e =  py.font.SysFont(None,numberSize)
e =  e.render("E", True, (0,0,0))

f =  py.font.SysFont(None,numberSize)
f =  f.render("F", True, (0,0,0))

g =  py.font.SysFont(None,numberSize)
g =  g.render("G", True, (0,0,0))

h =  py.font.SysFont(None,numberSize)
h =  h.render("H", True, (0,0,0))

letters = [a,b,c,d,e,f,g,h]