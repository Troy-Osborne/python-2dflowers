 
from PIL import Image,ImageDraw
from math import cos,sin,pi
from random import random

def make_flower(outlineThickness=2,outlineColor=(0,0,0),fill=(200,120,255),radius=40,petals=6,resolution=(200,200),centreType=2,pistilColors=((255,200,120),(180,100,60)),buldgeExpt=.3):
    hw=resolution[0]/2
    im=Image.new("RGBA",resolution,(0,0,0,0))
    dr=ImageDraw.Draw(im)
    ##draw stem
    centre=hw,radius
    lasty=centre[1]
    lastx=hw
    direction=random()*8-4
    x=hw
    for y in range(int(centre[1]),resolution[1],6):
        x+=direction
        direction*=.95
        
        
        dr.line((lastx,lasty,int(x),int(y)),fill=(20,30,10),width=6)
        dr.line((lastx,lasty,int(x),int(y)),fill=(40,90,60),width=3)
        lastx=int(x)
        lasty=int(y)

    if centreType==0:
        #no central pistil head
        pass
    ##draw petals
    points=[]
    #phaseshift=random()*pi
    phaseshift=0
    
    for i in range(360):
        ang=i/180*pi
        disp=radius*max(.2,((cos(phaseshift+ang*petals)+1)*.5)**buldgeExpt)
        x=hw+cos(ang)*disp
        y=radius+sin(ang)*disp
        points.append((x,y))
    dr.polygon(points,fill=fill,outline=outlineColor,width=outlineThickness)
    #end petal draw
    if centreType==1:
        #draw central pistil head as cingular circle (like a daisy cone)
        dr.ellipse((centre[0]-radius*.2,radius*.8,centre[0]+radius*.2,radius*1.2),fill=(pistilColors[0]),width=2,outline=pistilColors[1])
    if centreType==2:
        for pistil in range(int(radius**1.6)):
        #draw many pistils in the centre as a cluster
            ang,disp=random()*pi*2,random()*radius*.2
            x=centre[0]+cos(ang)*disp
            y=centre[1]+sin(ang)*disp
            dr.ellipse((x-2,y-2,x+2,y+2),fill=(pistilColors[1]))
            dr.ellipse((x-1,y-1,x+1,y+1),fill=(pistilColors[0]))
    return im.resize((100,100))

def mass_produce(amount=100):
    for i in range(amount):
        make_flower(fill=(int(random()*255),int(random()*255),int(random()*255)),centreType=int(random()*3),petals=4+int(random()*8),pistilColors=((int(random()*255),int(random()*255),int(random()*255)),(int(random()*255),int(random()*255),int(random()*255))),buldgeExpt=random()*.8+.2).save("./Renders/flower%04d.png"%i)        
mass_produce()
