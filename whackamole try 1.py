from machine import PWM, Pin, TouchPad
import time
import neopixel
import random
import utime

arrow = PWM(Pin(15))
arrow.freq(50)
arrow.duty(26)
A = 26

np = neopixel.NeoPixel(Pin(21), 16)
lol = []

capone = TouchPad(Pin(13))
captwo = TouchPad(Pin(12))
capthree = TouchPad(Pin(14))
capfour = TouchPad(Pin(27))
capfive = TouchPad(Pin(33))
capsix = TouchPad(Pin(32))
capseven = TouchPad(Pin(2))
capeight = TouchPad(Pin(4))

ledone = Pin(16, Pin.OUT)
ledtwo = Pin(17, Pin.OUT)
ledthree = Pin(18, Pin.OUT)
ledfour = Pin(19, Pin.OUT)
ledfive = Pin(25, Pin.OUT)
ledsix = Pin(26, Pin.OUT)
ledseven = Pin(22, Pin.OUT)
ledeight = Pin(23, Pin.OUT)

buzzer = Pin(5, Pin.OUT)
buzzer.value(0)

score = 0
timer = 0.7

moles = ["ledone", "ledtwo", 'ledthree', 'ledfour', 'ledfive', 'ledsix', "ledeight"]

startO = utime.time()
timerO = 10


#game start indicator

ledone.value(1)
ledtwo.value(1)
ledthree.value(1)
ledfour.value(1)
ledfive.value(1)
ledsix.value(1)
ledseven.value(1)
ledeight.value(1)
#time.sleep(100)

np[0] = (0,0,255)
np.write()
ledone.value(0)
ledtwo.value(0)
ledthree.value(0)
ledfour.value(0)
ledfive.value(0)
ledsix.value(0)
ledseven.value(0)
ledeight.value(0)
time.sleep(0.75)

#game

while True:
    time.sleep(1)
    read1 = capone.read()
    read2 = captwo.read()
    read3 = capthree.read()
    read4 = capfour.read()
    read5 = capfive.read()
    read6 = capsix.read()
    #read7 = capseven.read()
    read8 = capeight.read()

    while (score<8 and utime.time() - startO < timerO):
        buzzer.value(1)
        random_num = random.choice(moles)
        print(random_num)
        print('TIME CONSUMED:', utime.time() - startO)
        arrow.duty(A)
        print(A)

        if (random_num == "ledone"):
            start = utime.time()
            print("START:::", start)
            ledone.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read1 = capone.read()
                print("CAP VALUE:", read1)
                if (read1<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledone.value(0)
                    print("SCORE : ", score)
                    break
            ledone.value(0)
            print("SCORE : ", score)

        elif (random_num == "ledtwo"):
            start = utime.time()
            ledtwo.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read2 = captwo.read()
                if (read2<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledtwo.value(0)
                    print("SCORE : ", score)
                    break
            ledtwo.value(0)
            print("SCORE : ", score)

        elif (random_num == "ledthree"):
            start = utime.time()
            ledthree.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read3 = capthree.read()
                if (read3<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledthree.value(0)
                    print("SCORE : ", score)
                    break
            ledthree.value(0)
            print("SCORE : ", score)

        elif (random_num == "ledfour"):
            start = utime.time()
            ledfour.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read4 = capfour.read()
                if (read4<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledfour.value(0)
                    print("SCORE : ", score)
                    break
            ledfour.value(0)
            print("SCORE : ", score)

        elif (random_num == "ledfive"):
            start = utime.time()
            ledfive.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read5 = capfive.read()
                if (read5<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledfive.value(0)
                    print("SCORE : ", score)
                    break
            ledfive.value(0)
            print("SCORE : ", score)

        elif (random_num == "ledsix"):
            start = utime.time()
            ledsix.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read6 = capsix.read()
                if (read6<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledsix.value(0)
                    print("SCORE : ", score)
                    break
            ledsix.value(0)
            print("SCORE : ", score)

        #elif (random_num == "ledseven"):
            start = utime.time()
            ledseven.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                #read7 = capseven.read()
                #if (read7<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledseven.value(0)
                    print("SCORE : ", score)
                    break
            ledseven.value(0)
            print("SCORE : ", score)

        else:  #(random_num == "ledeight")
            start = utime.time()
            ledeight.value(1)
            buzzer.value(0)
            while(utime.time() - start < timer):
                read8 = capeight.read()
                if (read8<300):
                    score = score+1
                    lol.append(score)
                    A = A+13
                    ledeight.value(0)
                    print("SCORE : ", score)
                    break
            ledeight.value(0)
            print("SCORE : ", score)

        np[score] = (0,0,255)
        np.write()

    if (score == 8 and utime.time() - startO < timerO):
        print("WINNER")
        print(A)
        for i in range(0,9):
            np[i] = (0,255,0)
            np.write()
        break

    else:
        print("LOSER TIME OVER")
        print(A)
        for i in range(0,score+1):
            np[i] = (255,0,0)
            np.write()
        break


