from PIL import Image

def load_img(filename):
    return Image.open(filename) #needs capital Image because this is a factory function, which sets up image objects

def show_img(img):
    img.show()      #lowercase cuz it's a method of an object of the image module

def save_img(img, filename):
    img.save(filename, "jpeg")
    show_img(img)

def obamicon(img):
    pixel_data = img.getdata()  #this returns a list of tuples which contain RGB values for each pixel
    edited_data = []

    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    for pixel in pixel_data:
        intensity = pixel[0] + pixel[1] + pixel[2]  #getting intensity by adding R + G + B
        if(intensity<182):
            edited_data.append(darkBlue)
        elif(intensity>182 and intensity<364):
            edited_data.append(red)
        elif(intensity>364 and intensity<546):
            edited_data.append(lightBlue)
        else:
            edited_data.append(yellow)

    new_img = Image.new("RGB", img.size)    #img.size doesn't need () cuz it's an attribute
    new_img.putdata(edited_data)

    return new_img

def yellow_purple(img):
    pixel_data = img.getdata()  #this returns a list of tuples which contain RGB values for each pixel
    edited_data = []

    amber = (255,191,0)
    purple = (77,0,77)
    lightpurple = (149,0,179)
    lightyellow = (255,255,168)

    for pixel in pixel_data:
        intensity = pixel[0] + pixel[1] + pixel[2]  #getting intensity by adding R + G + B
        if(intensity<182):
            edited_data.append(amber)
        elif(intensity>182 and intensity<364):
            edited_data.append(purple)
        elif(intensity>364 and intensity<546):
            edited_data.append(lightpurple)
        else:
            edited_data.append(lightyellow)

    new_img = Image.new("RGB", img.size)    #img.size doesn't need () cuz it's an attribute
    new_img.putdata(edited_data)

    return new_img

def alien(img):
    pixel_data = img.getdata()  #this returns a list of tuples which contain RGB values for each pixel
    edited_data = []

    alien_armpit = (132,222,2)
    indigo = (64,0,128)
    lightBlue = (77,166,255)
    pink = (217,25,255)

    for pixel in pixel_data:
        intensity = pixel[0] + pixel[1] + pixel[2]  #getting intensity by adding R + G + B
        if(intensity<182):
            edited_data.append(alien_armpit)
        elif(intensity>182 and intensity<364):
            edited_data.append(indigo)
        elif(intensity>364 and intensity<546):
            edited_data.append(lightBlue)
        else:
            edited_data.append(pink)

    new_img = Image.new("RGB", img.size)    #img.size doesn't need () cuz it's an attribute
    new_img.putdata(edited_data)

    return new_img

def monochromatic(img):
    pixel_data = img.getdata()  #this returns a list of tuples which contain RGB values for each pixel
    edited_data = []

    darkgreen = (30,77,43)
    bluegreen = (13,152,130)
    lightgreen = (0,107,60)
    lightergreen = (123,187,97)

    for pixel in pixel_data:
        intensity = pixel[0] + pixel[1] + pixel[2]  #getting intensity by adding R + G + B
        if(intensity<182):
            edited_data.append(bluegreen)
        elif(intensity>182 and intensity<364):
            edited_data.append(darkgreen)
        elif(intensity>364 and intensity<546):
            edited_data.append(lightgreen)
        else:
            edited_data.append(lightergreen)

    new_img = Image.new("RGB", img.size)    #img.size doesn't need () cuz it's an attribute
    new_img.putdata(edited_data)

    return new_img

def hello(img):
    pixList = img.getdata()
    newPixList =[]
    darkblue = (1,0,0)
    darkblue1 = (0,0,500)
    darkblue2 = (1000,0,0)
    darkblue3 = (250,500,750)
    for pixel in pixList:
        intensity = pixel[0] + pixel[1] +pixel [2]
        if(intensity < 182):
            newPixList.append(darkblue)
        elif(intensity>=182 and intensity <364):
            newPixList.append(darkblue1)
        elif(intensity>=364 and intensity <546):
            newPixList.append(darkblue2)
        elif(intensity>=546):
            newPixList.append(darkblue3)

    new_img2 = Image.new("RGB", img.size)
    new_img2.putdata(newPixList)
    return new_img2

def owneon(img):
    pixlist = img.getdata()
    newPixlist = []
    for pixel in pixlist:
        intensity = pixel[0]+pixel[1]+pixel[2]
        if(intensity<182):
            newPixlist.append((255,0,0))
        elif(intensity>=182 and intensity <=364):
            newPixlist.append((0,255,236))
        elif(intensity>364 and intensity<=546):
            newPixlist.append((51,255,66))
        elif (intensity>546):
            newPixlist.append((255,255,0))
    new_img = Image.new("RGB",img.size)
    new_img.putdata(newPixlist)
    return new_img

def thanoss(img):
    pixlist = img.getdata()
    newPixlist = []
    for pixel in pixlist:
        intensity = pixel[0]+pixel[1]+pixel[2]
        if(intensity<182):
            newPixlist.append((90,238,115))
        elif(intensity>=182 and intensity <=364):
            newPixlist.append((91,24,106))
        elif(intensity>364 and intensity<=546):
            newPixlist.append((246,92,205))
        elif (intensity>546):
            newPixlist.append((149,113,146))
    new_img = Image.new("RGB",img.size)
    new_img.putdata(newPixlist)
    return new_img

def flaggy(img):
    pixlist = img.getdata()
    newPixlist = []
    for pixel in pixlist:
        intensity = pixel[0]+pixel[1]+pixel[2]
        if(intensity<182):
            newPixlist.append((74,44,47))
        elif(intensity>=182 and intensity <=364):
            newPixlist.append((223,94,70))
        elif(intensity>364 and intensity<=546):
            newPixlist.append((139,162,160))
        elif (intensity>546):
            newPixlist.append((38,139,209))
    new_img = Image.new("RGB",img.size)
    new_img.putdata(newPixlist)
    return new_img
