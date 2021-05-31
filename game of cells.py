import pygame
pygame.init()
win = pygame.display.set_mode((562,582))
pygame.display.set_caption('Conway\'s Game of Life')
cells='0'*6400
leh=80
nex=cells
cube_size=6
pause=True
ikan=0
saved_cells=cells
generation=0
def lis(s):
    l=[]
    for i in s:
        l.append(i)
    return l
def string(l):
    s=''
    for i in l:
        s+=i
    return s
def line(st,y):
    global cells
    global ikan
    x=2
    for i in st:
        R = pygame.draw.rect(win, (255*int(i), 0, 0), (x, y, cube_size,cube_size))
        mpos = pygame.mouse.get_pos()
        if R.collidepoint(mpos) and pygame.mouse.get_pressed()[0]:
            l=lis(cells)
            if l[ikan]=='0':
                l[ikan]='1'
            else:
                l[ikan]='0'
            cells=string(l)
            nex=string(l)
        x+=(1+cube_size)
        ikan+=1
def show():
    global cells
    global leh
    global cube_size
    global ikan
    ikan=0
    y = 2
    for i in range(leh):
        i*=leh
        line(cells[i:i+leh],y)
        y += (1+cube_size)
def update():
    global nex
    global cells
    global leh
    show()
    nex=''
    index=0
    if True:
        for cell in cells:
            neighbours=0
            try:
                if bool(int(cells[index-(leh-1)])) and not index<80:
                    neighbours+=1
                if bool(int(cells[index-leh])) and not index<80:
                    neighbours+=1
                if bool(int(cells[index-(leh+1)])) and not index<80:
                    neighbours+=1
                if bool(int(cells[index-1])):
                    neighbours+=1
                if bool(int(cells[index+1])):
                    neighbours+=1
                if bool(int(cells[index+(leh-1)])):
                    neighbours+=1
                if bool(int(cells[index+leh])):
                    neighbours+=1
                if bool(int(cells[index+(leh+1)])):
                    neighbours+=1
            except IndexError:
                pass
            if cell == '1':
                if neighbours<2:
                    nex+='0'
                elif neighbours==2 or neighbours==3:
                    nex+='1'
                elif neighbours>3:
                    nex+='0'
            elif cell=='0':
                if neighbours==3:
                    nex+='1'
                else:
                    nex+='0'
            index+=1
    cells=nex
def make_l(letter, x, y, col1, col2, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(letter, True, col1, col2)
    textR=text.get_rect()
    textR.center=(x,y)
    win.blit(text, textR)
    return textR
while True:
    if pygame.key.get_pressed()[pygame.K_s]:
        saved_cells=cells
    if pygame.key.get_pressed()[pygame.K_l]:
        cells=saved_cells
    if pygame.key.get_pressed()[pygame.K_r]:
        generation=0
        cells='0'*6400
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pause=False
        generation+=1
    else:
        pause=True
    pygame.event.get()
    win.fill((40,40,40))
    make_l('generation : '+str(generation), 80,570, (0,0,0), (40,40,40),10)
    if pause:
        show()
    else:
        update()
    pygame.display.update()
    if not pause:
        pygame.time.delay(0)
