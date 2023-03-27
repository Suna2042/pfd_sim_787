import pygame
from pygame.locals import *
import sys,math

class Pfd:
    screen=None
    CYAN=(77,164,235)
    BLOWN=(149,91,35)
    BLACK=(30,30,30)
    GRAY=(95,95,110)
    GRAY2=(80,65,90)
    GRAY3=(130,130,130)
    WHITE=(230,230,230)
    GREEN=(100,160,50)
    PINK=(242,126,215)
    x=0
    y=0
    Xmax=900 #900
    Ymax=900 #900

    FPV=0
    alt=10000
    spd=140
    vs=0
    hdg=360

    indicator_X=75
    indicator_Y=450
    mode_ind_X=290
    mode_ind_Y=40

    airlane_left_x=210
    airlane_right_x=340
    airlane_y=295
    airlane_w=10
    airlane_len=50

    att_lane=3.5 #姿勢指示白線の幅

    def __init__(self,screen):
        self.screen=screen
        print("constructer is called.\n")

    def draw(self,speed,altitude,heading):
        screen=self.screen

        # Pfd.spd=speed
        # Pfd.alt=altitude
        # Pfd.hdg=heading
        

        spd_tape_x=75 #速度テープx左
        alt_tape_x=600-Pfd.indicator_X #高度テープx右




        #ピッチ操作
        pressed_key=pygame.key.get_pressed()
        if pressed_key[K_UP]:
            Pfd.FPV+=2
            if Pfd.FPV > 90*2*Pfd.att_lane:
                Pfd.FPV=90*2*Pfd.att_lane
            Pfd.alt+=10
            Pfd.spd+=0.25
            Pfd.vs+=50
        if pressed_key[K_DOWN]:
            Pfd.FPV-=2
            if Pfd.FPV < -90*2*Pfd.att_lane:
                Pfd.FPV=-90*2*Pfd.att_lane
            Pfd.alt-=10
            Pfd.spd-=0.25
            Pfd.vs-=50
        #HDG操作
        if pressed_key[K_LEFT]:
            Pfd.hdg-=1
            if Pfd.hdg < 1:
                Pfd.hdg=360
        if pressed_key[K_RIGHT]:
            Pfd.hdg+=1
            if Pfd.hdg > 360:
                Pfd.hdg=1


        #ピッチとV/S計算
        pitch=(Pfd.FPV/Pfd.att_lane)/2
        vs=Pfd.spd*(6076.12/60)*math.sin(pitch*math.pi/180)
        #knot:nm/h → ft/m,
        #1nm = 6076.12ft,
        #1nm * 6076.12(ft/nm) / 1h * 60(min/h),
        #1knot(nm/h) = 6076.12/60 ft/min,
        #vs= {spd(knot) * (6076.12/60) ft/min} * sin(pitch) ?
        #print("SPD=%f V/S=%f Pitch=%f" %(Pfd.spd, vs, pitch))


        screen.fill(Pfd.BLACK)

        #PFDbg描画
        pygame.draw.rect(screen,Pfd.CYAN,Rect(0,0,600,min(300+Pfd.FPV,600)))
        pygame.draw.rect(screen,Pfd.BLOWN,Rect(0,300+Pfd.FPV,600,300-Pfd.FPV))

        #LEG情報描画
        pygame.draw.rect(screen,Pfd.GRAY2,Rect(607,0,300,150))
        pygame.draw.line(screen,Pfd.GRAY3,(607,151),(900,151),3)
        pygame.draw.line(screen,Pfd.GRAY3,(607,110),(900,110),3)

        #PFD仕切り線
        pygame.draw.rect(screen,Pfd.GRAY,Rect(601,0,5,900))
        pygame.draw.rect(screen,Pfd.BLACK,Rect(601,0,5,900),1)

        #白線上限目安(y=170)
        #pygame.draw.line(screen,Pfd.WHITE,(100,170),(500,170),2)
        #白線下限目安(y=470)
        #pygame.draw.line(screen,Pfd.WHITE,(100,470),(500,470),2)


        #姿勢指示線描画
        if-130 < Pfd.FPV < 170:
            pygame.draw.line(screen,Pfd.WHITE,(200,300+Pfd.FPV),(400,300+Pfd.FPV),3) #姿勢0度
        for i in range(-180,180):
            if (i/2)%10 == 0 and -130 < Pfd.FPV+i*Pfd.att_lane < 170:
                pygame.draw.line(screen, Pfd.WHITE,(250,300+Pfd.FPV+i*Pfd.att_lane),(350,300+Pfd.FPV+i*Pfd.att_lane),3)

                font10=pygame.font.Font(None,20)
                text_degree=font10.render(str(int(abs(i/2))),True,Pfd.WHITE)
                if i/2 != 0:
                    screen.blit(text_degree,(230,300-Pfd.att_lane+Pfd.FPV+i*Pfd.att_lane))
                    screen.blit(text_degree,(360,300-Pfd.att_lane+Pfd.FPV+i*Pfd.att_lane))
            if (i/2)%5 == 0 and -130 < Pfd.FPV+i*Pfd.att_lane < 170:
                pygame.draw.line(screen, Pfd.WHITE,(275,300+Pfd.FPV+i*Pfd.att_lane),(325,300+Pfd.FPV+i*Pfd.att_lane),3)
            if (i/2)%2.5 == 0 and -130 < Pfd.FPV+i*Pfd.att_lane < 170:
                pygame.draw.line(screen, Pfd.WHITE,(285,300+Pfd.FPV+i*Pfd.att_lane),(315,300+Pfd.FPV+i*Pfd.att_lane),3)
        
        
        #左姿勢指示 AIRLANE SIMBOL LEFT 2=白線幅
        
        pygame.draw.rect(screen,Pfd.BLACK,Rect(Pfd.airlane_left_x+Pfd.airlane_len-Pfd.airlane_w, Pfd.airlane_y, Pfd.airlane_w, 25))
        pygame.draw.rect(screen,Pfd.WHITE,Rect(Pfd.airlane_left_x+Pfd.airlane_len-Pfd.airlane_w, Pfd.airlane_y, Pfd.airlane_w, 25),2)
        pygame.draw.rect(screen,Pfd.BLACK,Rect(Pfd.airlane_left_x, Pfd.airlane_y, Pfd.airlane_len, Pfd.airlane_w))
        pygame.draw.rect(screen,Pfd.WHITE,Rect(Pfd.airlane_left_x, Pfd.airlane_y, Pfd.airlane_len, Pfd.airlane_w),2)
        pygame.draw.rect(screen,Pfd.BLACK,Rect(252, 297, 6, 21)) #白線消し

        #右姿勢指示
        pygame.draw.rect(screen,Pfd.BLACK,Rect(Pfd.airlane_right_x,295,10,25))
        pygame.draw.rect(screen,Pfd.WHITE,Rect(Pfd.airlane_right_x,295,10,25),2)
        pygame.draw.rect(screen,Pfd.BLACK,Rect(Pfd.airlane_right_x,295,50,10))
        pygame.draw.rect(screen,Pfd.WHITE,Rect(Pfd.airlane_right_x,295,50,10),2)
        pygame.draw.rect(screen,Pfd.BLACK,Rect(Pfd.airlane_right_x+2,Pfd.airlane_y+2,6,21)) #白線消し

        #真ん中姿勢指示
        pygame.draw.rect(screen,Pfd.BLACK,Rect(295,295,10,10))
        pygame.draw.rect(screen,Pfd.WHITE,Rect(295,295,10,10),2)
        
        #高度tape/速度tape/mode_tape/vs_tape bg描画
        tape=pygame.Surface((600,600),flags=pygame.SRCALPHA)
        tape.set_alpha(196)
        pygame.draw.rect(tape,Pfd.GRAY,Rect(75,75,Pfd.indicator_X,Pfd.indicator_Y)) #spd
        pygame.draw.rect(tape,Pfd.BLACK,Rect(75,75,Pfd.indicator_X,Pfd.indicator_Y),1)

        pygame.draw.rect(tape,Pfd.GRAY,Rect(600-Pfd.indicator_X-75,75,Pfd.indicator_X,Pfd.indicator_Y)) #alt
        pygame.draw.rect(tape,Pfd.BLACK,Rect(600-Pfd.indicator_X-75,75,Pfd.indicator_X,Pfd.indicator_Y),1)

        pygame.draw.rect(tape,Pfd.GRAY,Rect(75+Pfd.indicator_X+5,5,Pfd.mode_ind_X,Pfd.mode_ind_Y)) #mode
        pygame.draw.rect(tape,Pfd.BLACK,Rect(75+Pfd.indicator_X+5,5,Pfd.mode_ind_X,Pfd.mode_ind_Y),1)
        
        vs_std_x=alt_tape_x+15 #VSテープ基準
        vs_std_y=275-10
        pygame.draw.polygon(tape,Pfd.GRAY,[(vs_std_x,150),(vs_std_x,vs_std_y-10),(vs_std_x+15,vs_std_y),(vs_std_x+15,300),(vs_std_x+15,335),(vs_std_x,335+10),(vs_std_x,450),(vs_std_x+20,450),(580,375),(580,225),(vs_std_x+20,150)]) #vs_tape
        pygame.draw.polygon(tape,Pfd.BLACK,[(vs_std_x,150),(vs_std_x,vs_std_y-10),(vs_std_x+15,vs_std_y),(vs_std_x+15,300),(vs_std_x+15,335),(vs_std_x,335+10),(vs_std_x,450),(vs_std_x+20,450),(580,375),(580,225),(vs_std_x+20,150)],1)

        screen.blit(tape,(0,0))

        #昇降計
        j=0
        font_sub_y=[0,60/2,60,(60+75+75/2)/2,75+75/2,(75+75/2+150-10)/2,150-10]
        vs_list=[0,0,1,0,2,0,6,0,0]
        vs=min(Pfd.vs,6000) if Pfd.vs >=0 else max(Pfd.vs,-6000)
        font_vs=pygame.font.Font(None,20)
        for i in font_sub_y:
            vs_width=3 if j%2==0 else 2
            vs_zero=7 if j==0 else 0
            pygame.draw.line(screen,Pfd.WHITE,(vs_std_x+15-2,300-i),(vs_std_x+15-2+5+vs_zero,300-i),vs_width)
            pygame.draw.line(screen,Pfd.WHITE,(vs_std_x+15-2,300+i),(vs_std_x+15-2+5+vs_zero,300+i),vs_width)
            if j%2==0 and j!=0:
                vs_num=font_vs.render('{:1.0f}'.format(vs_list[j]),True,Pfd.WHITE)
                screen.blit(vs_num,(vs_std_x+5,300+i-6))
                screen.blit(vs_num,(vs_std_x+5,300-i-6))
            j+=1
        if vs >= 0:
            if 0 <= vs < 1000:
                pygame.draw.line(screen,Pfd.WHITE,(580,300-(vs/1000)*75/2),(vs_std_x+15,300-60*vs/1000),3)
            elif 1000 <= vs < 2000:
                pygame.draw.line(screen,Pfd.WHITE,(580,300-75/2-((vs-1000)/1000)*75/4),(vs_std_x+15,300-60-((75+75/2)-60)*(vs-1000)/1000),3)
            elif 2000 <= vs <= 6000:
                pygame.draw.line(screen,Pfd.WHITE,(580,300-75/2-75/4-((vs-2000)/4000)*75/4),(vs_std_x+15,300-60-((75+75/2)-60)-((150-10)-(75+75/2))*(vs-2000)/4000),3)
        elif vs < 0:
            if 0 >= vs > -1000:
                pygame.draw.line(screen,Pfd.WHITE,(580,300-(vs/1000)*75/2),(vs_std_x+15,300-60*vs/1000),3)
            elif -1000 >= vs > -2000:
                pygame.draw.line(screen,Pfd.WHITE,(580,300+75/2-((vs+1000)/1000)*75/4),(vs_std_x+15,300+60-((75+75/2)-60)*(vs+1000)/1000),3)
            elif -2000 >= vs >= -6000:
                pygame.draw.line(screen,Pfd.WHITE,(580,300+75/2+75/4-((vs+2000)/4000)*75/4),(vs_std_x+15,300+60+((75+75/2)-60)-((150-10)-(75+75/2))*(vs+2000)/4000),3)

        font_vs_num=pygame.font.Font(None,30)
        
        vs_digital_x_sub=0 if -1000 < Pfd.vs < 1000 else 9.5
        if Pfd.vs>=400:
            vs_digital=font_vs_num.render('{:3.0f}'.format(math.fabs(Pfd.vs-Pfd.vs%50)),True,Pfd.WHITE)
            screen.blit(vs_digital,(vs_std_x-vs_digital_x_sub+10,120))
        elif Pfd.vs<=-400:
            vs_digital=font_vs_num.render('{:3.0f}'.format(math.fabs(Pfd.vs+(50-Pfd.vs%50)%50)),True,Pfd.WHITE)
            screen.blit(vs_digital,(vs_std_x-vs_digital_x_sub+10,470))

            

        #mode indicator
        for i in range(2):
            mode_line_x=75+Pfd.indicator_X+5+Pfd.mode_ind_X*(i+1)/3
            pygame.draw.line(screen,Pfd.WHITE,(mode_line_x,5+2),(mode_line_x,5+Pfd.mode_ind_Y-2),3)


        #spd表示
        font_spd=pygame.font.Font(None,40)
        font_spd_20=pygame.font.Font(None,30)
        spd=max(30,Pfd.spd)
        spd1=spd%10
        spd10=spd%100
        spd100=spd%1000

        #アナログ速度計
        spd_width=37.5
        for i in range(-10,10):
            spdline_y=300-i*spd_width-spd_width*((math.floor(spd/10)*10)-spd)/10
            spdnum_y=spdline_y-7
            spd_analog_num=max(math.floor(spd/10)*10+10*i,29.99)
            if (math.floor((spd+10*i)/100)*100)%10==0 and 75 < spdline_y < 75+Pfd.indicator_Y and spd_analog_num>=30: 
                pygame.draw.line(screen,Pfd.WHITE,(spd_tape_x+75-15,300-i*spd_width-spd_width*((math.floor(spd/10)*10)-spd)/10),(spd_tape_x+75,300-i*spd_width-spd_width*((math.floor(spd/10)*10)-spd)/10),2)
            
            if (math.floor(spd/10)*10+10*i)%20==0 and 75 < spdnum_y < 75+Pfd.indicator_Y-15:
                spd_analog100=font_spd_20.render('{:3.0f}'.format(spd_analog_num),True,Pfd.WHITE)
                if math.floor(spd_analog_num) >= 100:
                    screen.blit(spd_analog100,(spd_tape_x+20,300-7-i*spd_width-spd_width*((math.floor(spd/10)*10)-spd)/10))
                elif 100 > math.floor(spd_analog_num) >= 30:
                    screen.blit(spd_analog100,(spd_tape_x+20+5,300-7-i*spd_width-spd_width*((math.floor(spd/10)*10)-spd)/10))

        #spd_tape_x=75 #速度窓
        pygame.draw.polygon(screen,Pfd.BLACK,[(spd_tape_x-5,325),(spd_tape_x+50,325),(spd_tape_x+50,310),(spd_tape_x+50+10,300),(spd_tape_x+50,290),(spd_tape_x+50,275),(spd_tape_x-5,275)])
        pygame.draw.polygon(screen,Pfd.WHITE,[(spd_tape_x-5,325),(spd_tape_x+50,325),(spd_tape_x+50,310),(spd_tape_x+50+10,300),(spd_tape_x+50,290),(spd_tape_x+50,275),(spd_tape_x-5,275)],2)
        
        #デジタル速度計
        font_spd=pygame.font.Font(None,40)

        for i in [-1,0,1,2,3,4,5,6,7,8,9,10,11]:#1桁目
            if spd > 35: #35以下の時9を出力しない
                rend_spd1=font_spd.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
                screen.blit(rend_spd1,(950-200,600+200-3-21*(i-spd1)))
            if spd <= 35 and i%10 != 9:
                rend_spd1=font_spd.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
                screen.blit(rend_spd1,(950-200,600+200-3-21*(i-spd1)))
        for i in [-1,0,1,2,3,4,5,6,7,8,9,10,11]:#2桁目
            rend_spd10=font_spd.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
            screen.blit(rend_spd10,(950-200-15,600+200-3-40*(i-math.floor(spd10/10))+40*(max((spd1-9),0))))
        for i in [1,2,3,4,5,6,7,8,9,10,11]:#3桁目
            rend_spd100=font_spd.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
            screen.blit(rend_spd100,(950-200-30,600+200-3-40*(i-math.floor(spd100/100))+40*(max((spd10-99),0))))
        
        screen.blit(screen,(spd_tape_x,275+6),area=Rect(950-200-30,600+187,50,40))


        #alt表示

        #高度桁別取得35580
        alt10=Pfd.alt%100
        alt100=Pfd.alt%1000
        alt1000=Pfd.alt%10000
        alt10000=Pfd.alt
        
        font_alt_20=pygame.font.Font(None,20)
        font_alt_100=pygame.font.Font(None,30)
        font_alt_1000=pygame.font.Font(None,40)

        #アナログ高度計 真ん中:(alt_tape_x-75-2,300-7)
        alt_width=50
        
        for i in range(-10,10):
            altline_y=300-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100
            altnum_y=300-7-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100
            alt_analog_num=math.floor(Pfd.alt/100)*100+100*i
            if (math.floor((Pfd.alt+10*i)/100)*100)%100==0 and 75 < altline_y < 75+Pfd.indicator_Y and alt_analog_num%500==0:
                pygame.draw.line(screen,Pfd.WHITE,(alt_tape_x-75-2,300-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100),(alt_tape_x-60,300-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100),6)
            elif (math.floor((Pfd.alt+10*i)/100)*100)%100==0 and 75 < altline_y < 75+Pfd.indicator_Y:
                pygame.draw.line(screen,Pfd.WHITE,(alt_tape_x-75-2,300-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100),(alt_tape_x-60,300-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100),2)

            if (math.floor(Pfd.alt/100)*100+100*i)%200==0 and 75 < altnum_y < 75+Pfd.indicator_Y-15:
                alt_analog=font_alt_100.render('{:.0f}'.format(math.floor(alt_analog_num/1000)),True,Pfd.WHITE)
                alt_analog100=font_alt_20.render('{:003.0f}'.format(alt_analog_num%1000),True,Pfd.WHITE)
                if math.floor(alt_analog_num/1000) >= 10:
                    screen.blit(alt_analog,(alt_tape_x-75-2+30,300-7-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100))
                elif 0 < math.floor(alt_analog_num/1000) < 10:
                    screen.blit(alt_analog,(alt_tape_x-75-2+30+11,300-7-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100))

                if math.floor(alt_analog_num)%1000==0:
                    pygame.draw.line(screen,Pfd.WHITE,((alt_tape_x-75-2+20,300-9-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100)),((alt_tape_x-75-2+20+55,300-9-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100)),2)
                    pygame.draw.line(screen,Pfd.WHITE,((alt_tape_x-75-2+20,300-9+20-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100)),((alt_tape_x-75-2+20+55,300-9+20-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100)),2)
                screen.blit(alt_analog100,(alt_tape_x-75-2+3+30+20,300-7+5-i*alt_width-alt_width*((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100))
                #print(((math.floor(Pfd.alt/100)*100)-Pfd.alt)/100)
        
        #print(str(math.floor(Pfd.alt/100)*100))
        
        #alt_tape_x=Pfd.Xmax-Pfd.indicator_X #高度窓
        pygame.draw.polygon(screen,Pfd.BLACK,[(alt_tape_x+25,325),(alt_tape_x-50,325),(alt_tape_x-50,310),(alt_tape_x-50-10,300),(alt_tape_x-50,290),(alt_tape_x-50,275),(alt_tape_x+25,275)])
        pygame.draw.polygon(screen,Pfd.WHITE,[(alt_tape_x+25,325),(alt_tape_x-50,325),(alt_tape_x-50,310),(alt_tape_x-50-10,300),(alt_tape_x-50,290),(alt_tape_x-50,275),(alt_tape_x+25,275)],2)
        alt_ind=pygame.Surface((100,100))

        #デジタル高度計
        #隠すために左に200,下に600オフセット
        for i in [-20,0,20,40,60,80,100,120]:#1,2桁目
            rend_alt10=font_alt_100.render('{:0=2}'.format(i%100),True,Pfd.WHITE)
            screen.blit(rend_alt10,(1050-200,600+200+0.8*(alt10-i)))
        for i in [-1,0,1,2,3,4,5,6,7,8,9,10,11]:#3桁目
            rend_alt100=font_alt_100.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
            screen.blit(rend_alt100,(1039-200,600+200-40*(i-math.floor(alt100/100))+40*(max((alt10-80)/20,0))))
        for i in [0,1,2,3,4,5,6,7,8,9,10,11]:#4桁目
            rend_alt_1000=font_alt_1000.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
            if Pfd.alt>=10000:
                screen.blit(rend_alt_1000,(1025-200,600+200-5-40*(i-math.floor(alt1000/1000))+40*(max((alt100-980)/20,0))))
            elif Pfd.alt<10000 and i!=0:
                screen.blit(rend_alt_1000,(1025-200,600+200-5-40*(i-math.floor(alt1000/1000))+40*(max((alt100-980)/20,0))))
        for i in [1,2,3,4,5,6,7,8,9,10,11]:#5桁目
            rend_alt_10000=font_alt_1000.render('{:1.0f}'.format(i%10),True,Pfd.WHITE)
            screen.blit(rend_alt_10000,(1011-200,600+200-5-40*(i-math.floor(alt10000/10000))+40*(max((alt1000-9980)/20,0))))
        
        #pygame.draw.rect(screen,Pfd.WHITE,Rect(1010,187.5,75,40),2)
        screen.blit(screen,(alt_tape_x-50+6,275+6),area=Rect(1010-200,600+187,65,40))
        pygame.draw.rect(screen,Pfd.BLACK,Rect(610,300,300,900))#右に置いた高度計を隠すためにrect
        if Pfd.alt < 9980:
            pygame.draw.rect(screen,Pfd.GREEN,Rect(alt_tape_x-50+6,275+12,15,27))
    

        #mini-map 620->810  """5nm=95px""" """me(x,y)=(300,810)"""
        pygame.draw.polygon(screen,Pfd.WHITE,[(300,810),(285,850),(315,850)],2)
        pygame.draw.polygon(screen,Pfd.WHITE,[(300,620),(290,602),(310,602)],1)
        pygame.draw.line(screen,Pfd.WHITE,(300,810),(300,620),1)
        pygame.draw.line(screen,Pfd.WHITE,(295,715),(305,715),1)

        

        hdg_num=pygame.font.Font(None,20)
        for i in range(1,364):
            if math.cos((i-Pfd.hdg)*math.pi/180)>-0.15:
                if i%5==0:
                    pygame.draw.line(screen,Pfd.WHITE,(300+190*math.sin((i-Pfd.hdg)*math.pi/180),810-190*math.cos((i-Pfd.hdg)*math.pi/180)),(300+185*math.sin((i-Pfd.hdg)*math.pi/180),810-185*math.cos((i-Pfd.hdg)*math.pi/180)),2)
                if i%10==0:
                    pygame.draw.line(screen,Pfd.WHITE,(300+190*math.sin((i-Pfd.hdg)*math.pi/180),810-190*math.cos((i-Pfd.hdg)*math.pi/180)),(300+175*math.sin((i-Pfd.hdg)*math.pi/180),810-175*math.cos((i-Pfd.hdg)*math.pi/180)),2)
                if i%30==0 or i==360:
                    
                    render_hdg1=hdg_num.render('{:2.0f}'.format(math.floor(i/10)),True,Pfd.WHITE)
                    screen.blit(render_hdg1,(300+175*math.sin((i-Pfd.hdg)*math.pi/180),810-175*math.cos((i-Pfd.hdg)*math.pi/180)))
                

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()



    