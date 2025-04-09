from cmu_graphics import *
from PIL import Image
import random
import os, pathlib

'''
15-112 Term Project by Chloe Zhu (Andrew ID: qingyuzh)
Last Updated: 04/22/2023

Project Title: Hungry Bunny

Project Description:
The project is a 2D casual parkour game where players control
a bunny on a randomly generated terrain, trying to catch as 
much food and coins as possible while avoiding obstacles such 
as coffee, ice, and bombs. The game offers straightforward 
controls, visually pleasing original hand-painted graphics, 
and engaging power-ups. The player can interact with the bunny 
on the starting screen, and use gold coins earned in-game to 
improve the bunny's attributes in the store. All upgrades are 
only valid for one game.

Note: All the pictures in the game are hand-drawings
      done by myself.
'''

class Bunny:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawBunny(self):
        self.bunny1 = Image.open("images/bunny1.png")
        self.bunny1 = CMUImage(self.bunny1)
        self.bunny2 = Image.open("images/bunny2.png")
        self.bunny2 = CMUImage(self.bunny2)
        self.bunny = [self.bunny1, self.bunny2]

        self.bunnydead = Image.open("images/bunny_dead.png")
        self.bunnydead = CMUImage(self.bunnydead)
    
        self.bunnyfrozen = Image.open("images/bunny_frozen.png")
        self.bunnyfrozen = CMUImage(self.bunnyfrozen)

        self.bunnycrazy1 = Image.open("images/bunny_crazy1.png")
        self.bunnycrazy1 = CMUImage(self.bunnycrazy1)
        self.bunnycrazy2 = Image.open("images/bunny_crazy2.png")
        self.bunnycrazy2 = CMUImage(self.bunnycrazy2)
        self.bunnycrazy = [self.bunnycrazy1, self.bunnycrazy2]

        self.bunnyshield1 = Image.open("images/bunny_shield1.png")
        self.bunnyshield1 = CMUImage(self.bunnyshield1)
        self.bunnyshield2 = Image.open("images/bunny_shield2.png")
        self.bunnyshield2 = CMUImage(self.bunnyshield2)
        self.bunnyshield = [self.bunnyshield1, self.bunnyshield2]

        if self.dies:
            drawImage(self.bunnydead, self.x, self.y, 
                      width=180, height=180, align='bottom')
        elif self.frozen:
            drawImage(self.bunnyfrozen, self.x, self.y, 
                      width=188, height=115, align='bottom')
        elif self.crazy:
            bunnycrazy = self.bunnycrazy [self.crazyCounter]
            drawImage(bunnycrazy, self.x, self.y, 
                      width=180, height=105, align='bottom')
        elif self.shield:
            bunnyshield = self.bunnyshield [self.shieldCounter]
            drawImage(bunnyshield, self.x, self.y, 
                      width=180, height=105, align='bottom')
        else:
            bunny = self.bunny [self.counter]
            drawImage(bunny, self.x, self.y, 
                      width=180, height=105, align='bottom')
            
    def drawStartpageBunny(self):
        self.bunny1 = Image.open("images/bunny1.png")
        self.bunny1 = CMUImage(self.bunny1)
        self.bunny2 = Image.open("images/bunny2.png")
        self.bunny2 = CMUImage(self.bunny2)
        self.bunny = [self.bunny1, self.bunny2]

        self.bunny1f = Image.open("images/bunny1f.png")
        self.bunny1f = CMUImage(self.bunny1f)
        self.bunny2f = Image.open("images/bunny2f.png")
        self.bunny2f = CMUImage(self.bunny2f)
        self.bunnyf = [self.bunny1f, self.bunny2f]

        self.bunnyhappy1 = Image.open("images/bunny_happy1.png")
        self.bunnyhappy1 = CMUImage(self.bunnyhappy1)
        self.bunnyhappy2 = Image.open("images/bunny_happy2.png")
        self.bunnyhappy2 = CMUImage(self.bunnyhappy2)
        self.bunnyhappy = [self.bunnyhappy1, self.bunnyhappy2]

        self.bunnyhappy1f = Image.open("images/bunny_happy1f.png")
        self.bunnyhappy1f = CMUImage(self.bunnyhappy1f)
        self.bunnyhappy2f = Image.open("images/bunny_happy2f.png")
        self.bunnyhappy2f = CMUImage(self.bunnyhappy2f)
        self.bunnyhappyf = [self.bunnyhappy1f, self.bunnyhappy2f]

        self.bunnyangry = Image.open("images/bunny_angry.png")
        self.bunnyangry = CMUImage(self.bunnyangry)

        self.bunnyangryf = Image.open("images/bunny_angryf.png")
        self.bunnyangryf = CMUImage(self.bunnyangryf) # type: ignore

        
        if self.right:
            if self.happy:
                bunnyhappy = self.bunnyhappy [self.counter]
                drawImage(bunnyhappy, self.startpageX, 440, 
                        width=180, height=105, align='bottom')
            elif self.angry:
                drawImage(self.bunnyangry, self.startpageX, 440, 
                        width=180, height=105, align='bottom')
            else:
                bunny = self.bunny [self.counter]
                drawImage(bunny, self.startpageX, 440, 
                        width=180, height=105, align='bottom')
        else:
            if self.happy:
                bunnyhappyf = self.bunnyhappyf [self.counter]
                drawImage(bunnyhappyf, self.startpageX, 440, 
                        width=180, height=105, align='bottom')
            elif self.angry:
                drawImage(self.bunnyangryf, self.startpageX, 440, 
                        width=180, height=105, align='bottom')
            else:
                bunnyf = self.bunnyf [self.counter]
                drawImage(bunnyf, self.startpageX, 440, 
                        width=180, height=105, align='bottom')


class Item:
    def __init__(self):
        self.list = []
        self.landscape = []

    def loadItems(self):
        self.coin1 = Image.open("images/coin1.png")
        self.coin1 = CMUImage(self.coin1)
        self.coin2 = Image.open("images/coin2.png")
        self.coin2 = CMUImage(self.coin2)
        self.coin3 = Image.open("images/coin3.png")
        self.coin3 = CMUImage(self.coin3)
        self.coin4 = Image.open("images/coin4.png")
        self.coin4 = CMUImage(self.coin4)
        self.coin5 = Image.open("images/coin5.png")
        self.coin5 = CMUImage(self.coin5)
        self.coin = [self.coin1, self.coin2, self.coin3,
                     self.coin4, self.coin5]
        
        self.bomb1 = Image.open("images/bomb1.png")
        self.bomb1 = CMUImage(self.bomb1)
        self.bomb2 = Image.open("images/bomb2.png")
        self.bomb2 = CMUImage(self.bomb2)
        self.bomb3 = Image.open("images/bomb3.png")
        self.bomb3 = CMUImage(self.bomb3)
        self.bomb = [self.bomb1, self.bomb2, self.bomb3]

        self.strawberry = Image.open("images/strawberry.png")
        self.strawberry = CMUImage(self.strawberry)

        self.tomato = Image.open("images/tomato.png")
        self.tomato = CMUImage(self.tomato)

        self.carrot = Image.open("images/carrot.png")
        self.carrot = CMUImage(self.carrot)

        self.ice = Image.open("images/ice.png")
        self.ice = CMUImage(self.ice)

        self.coffee = Image.open("images/coffee.png")
        self.coffee = CMUImage(self.coffee)

        self.items = [self.coin, self.coin, self.coin, self.coin, 
                      self.coin, self.bomb, self.ice, self.coffee,
                      self.strawberry, self.carrot, self.tomato,
                      self.strawberry, self.carrot, self.tomato]
        
        self.purchased = Image.open("images/purchased.png")
        self.purchased = CMUImage(self.purchased)

        self.anticoffeine = Image.open("images/anticoffeine.png")
        self.anticoffeine = CMUImage(self.anticoffeine)

        self.antifreeze = Image.open("images/antifreeze.png")
        self.antifreeze = CMUImage(self.antifreeze)
    
        self.shield = Image.open("images/shield.png")
        self.shield = CMUImage(self.shield)

        self.land = Image.open("images/land.png")
        self.land = CMUImage(self.land)

    def drawLand(self):
        if self.landscape != []:
            for land in self.landscape:
                drawImage(self.land, land['x'], land['y'],
                          width=400, height=600, align='top')

        
    def drawItems(self):  
        if self.list != []:
            for item in self.list:
                for land in self.landscape:
                    if land['x']-200 < item['x'] < land['x'] + 200:
                        item['y'] = land['y'] - 10
                if item['name'] == self.coin:
                    coin = self.coin[self.coinCounter]
                    drawImage(coin, item['x'], item['y'], 
                              width=80, height=80, align='center')
                elif item['name'] == self.bomb:
                    bomb = self.bomb[self.bombCounter]
                    drawImage(bomb, item['x'], item['y'], 
                              width=80, height=80, align='center')
                else:
                    drawImage(item['name'], item['x'], item['y'], 
                              width=80, height=80, align='center')
                
    def loadNextItem(self):
        self.list.append({'name': random.choice(self.items), 'x': 1200, 'y': 460})

    def loadLandscape(self):
        self.landscape.append({'name':self.land,'x': 1200,
                               'y': random.choice([430, 460, 490, 520])})
        

class Game:
    def __init__(self):
        self.point = 10

    def drawOpenScreen(self):
        self.start = Image.open("images/startpage.png")
        self.start = CMUImage(self.start)
        self.play = Image.open("images/play.png")
        self.play = CMUImage(self.play)
        self.menu = Image.open("images/menu.png")
        self.menu = CMUImage(self.menu)

        drawImage(self.start, 0, 0, width=1200, height=800)
        drawImage(self.play, 600, 575, 
                  width=350, height=111, align='center')
        drawImage(self.menu, 20, 20, width=66, height=44)
        drawLabel('Menu', 53, 73, size=20, fill='white')

    def drawInstructionScreen(self):
        self.instruction = Image.open("images/instruction.png")
        self.instruction = CMUImage(self.instruction)

        drawImage(self.instruction, 0, 0, width=1200, height=800)
        drawLabel('INSTRUCTIONS', 600, 200, size=80, font='cinzel', 
                  fill='white', bold=True, align='center')
        
        drawLabel('1. Click or press "space" to jump', 300, 300,
                  size=30, font='cinzel', fill='white', align='left')
        drawLabel('2. The bunny can double jump', 300, 350,
                  size=30, font='cinzel', fill='white', align='left')
        drawLabel('3. Collect as much coins and food as you can', 300, 400,
                  size=30, font='cinzel', fill='white', align='left')
        drawLabel('4. Watch out for bombs, coffee, and ice!', 300, 450,
                  size=30, font='cinzel', fill='white', align='left')
        drawLabel('5. Get more exciting upgrades at the store :)', 300, 500,
                  size=30, font='cinzel', fill='white', align='left')
        drawLabel('6. Purchased upgrades are only valid for once', 300, 550,
                  size=30, font='cinzel', fill='white', align='left')
        
        if not self.ok:
            drawLabel('OK', 600, 620, size=30,
                  font='cinzel', fill='white', align='center')
        else:
            drawLabel('OK', 600, 620, size=30,
                  font='cinzel', fill='yellow', bold=True, align='center')
            drawLine(580, 635, 620, 635, fill='yellow')

    def drawMenuScreen(self):
        self.menupage = Image.open("images/menupage.png")
        self.menupage = CMUImage(self.menupage)

        drawImage(self.menupage, 0, 0, width=1200, height=800)
        drawLabel('MENU', 600, 230, size=80, font='cinzel', 
                  fill='white', bold=True, align='center')
        if not self.seeInstructions:
            drawLabel('Click here for Instructions', 600, 600, size=30,
                  font='cinzel', fill='white', align='center')
        else:
            drawLabel('Click here for Instructions', 600, 600, size=30,
                  font='cinzel', fill='yellow', bold=True, align='center')
            drawLine(415, 615, 785, 615, fill='yellow')
        
    def drawGameOverScreen(self):
        self.gameover = Image.open("images/gameover.png")
        self.gameover = CMUImage(self.gameover)

        drawImage(self.gameover, 0, 0, width=1200, height=800)
        drawLabel('GAME OVER', 600, 200, size=80, font='cinzel', 
                  fill='white', bold=True, align='center')

    def drawParkour(self):
        self.bg = Image.open("images/background.png")
        self.bg = CMUImage(self.bg)
        self.menu = Image.open("images/menu.png")
        self.menu = CMUImage(self.menu)

        drawImage(self.bg, 0, 0, width=1200, height=800)
        drawImage(self.menu, 20, 20, width=66, height=44)
        drawLabel('Menu', 53, 73, size=20, fill='white')

        if self.paused:
            drawLabel('Game Paused', 600, 200, size=80, font='cinzel', 
                      fill='white', bold=True, opacity=70)
            drawLabel('Click to Resume', 600, 280, size=40, font='cinzel', 
                      fill='white', bold=True, opacity=70)
        if self.over:
            drawLabel('Game Over', 600, 200, size=80, font='cinzel', 
                      fill='white', bold=True, opacity=70)
            # drawLabel('Click to Restart', 600, 280, size=40, font='cinzel', 
            #           fill='white', bold=True, opacity=70)
            
    def drawStore(self):
        self.store = Image.open("images/store.png")
        self.store = CMUImage(self.store)

        drawImage(self.store, 0, 0, width=1200, height=800)
        drawLabel('STORE', 600, 170, size=80, font='cinzel', 
                  fill='white', bold=True, align='center')

        drawLabel('Anti-Caffeine', 376, 300, size=25,
                  font='cinzel', bold=True, align='center')
        drawLabel('Take these pills to', 376, 500, size=15, font='cinzel')
        drawLabel('prevent your bunny from', 376, 520, size=15, font='cinzel')
        drawLabel('going crazy from coffee', 376, 540, size=15, font='cinzel')
        drawLabel('200', 376, 600, size=25, font='cinzel', bold=True, align='right')

        drawLabel('Anti-Freeze', 602, 300, size=25,
                  font='cinzel', bold=True, align='center')
        drawLabel('Take these pills to', 603, 500, size=15, font='cinzel')
        drawLabel('prevent your bunny from', 603, 520, size=15, font='cinzel')
        drawLabel('being frozen by ice', 603, 540, size=15, font='cinzel')
        drawLabel('200', 603, 600, size=25, font='cinzel', bold=True, align='right')

        drawLabel('Shield', 828, 300, size=25,
                  font='cinzel', bold=True, align='center')
        drawLabel('Take this shield to', 830, 500, size=15, font='cinzel')
        drawLabel('protect your bunny from', 830, 520, size=15, font='cinzel')
        drawLabel('the bomb for once', 830, 540, size=15, font='cinzel')
        drawLabel('100', 828, 600, size=25, font='cinzel', bold=True, align='right')


def onAppStart(app):
    app.coinsEarned = 0
    reset(app)

def reset(app):
    getSound(app)

    app.bunny = Bunny(200, 150)
    app.bunny.startpageX = 600
    app.bunny.right = True
    app.bunny.happy = False
    app.bunny.angry = False
    app.bunny.happyCounter = 0
    app.bunny.angryCounter = 0

    app.bunny.counter = 0
    app.bunny.runCounter = 0
    app.bunny.isjumping = False
    app.bunny.jumpCounter = 5
    app.bunny.jumptimes = 0
    app.bunny.frozen = False
    app.bunny.frozenCounter = 20
    app.bunny.crazy = False
    app.bunny.crazyCounter = 0

    app.bunny.isOnLand = False
    app.bunny.speed = 20
    app.bunny.gravity = 5

    app.bunny.anticoffeine = False
    app.bunny.antifreeze = False
    app.bunny.shield = False
    app.bunny.shieldrunCounter = 0
    app.bunny.shieldCounter = 0

    app.item = Item()
    app.item.loadItems()
    app.item.y = 460
    app.item.timeToNextItem = random.randint(5, 15)
    app.item.list = []
    app.item.coinCounter = 0
    app.item.bombCounter = 0

    app.item.landscape = []
    app.item.timeToNextLand = 1

    app.game = Game()
    app.game.paused = False
    app.game.over = False
    app.bunny.dies = app.game.over
    app.game.point = 10
    app.game.speed = 30
    app.game.overCounter = 0
    app.game.seeInstructions = False
    app.game.ok = False

    recordCoins(app)
    app.score = 0
    app.coinsEarned = 0
    app.landIndex = None
    app.gamestartCounter = 30
    app.gamespeedHelper = 10
    app.gamespeedCounter = 0


'''
Note: the "loadSound" function is from the soundDemo that
TA Shawn provided.
'''
def loadSound(relativePath):
    absolutePath = os.path.abspath(relativePath)
    url = pathlib.Path(absolutePath).as_uri()
    return Sound(url)


'''
Note: the coin, jump, countdown, and gameover sounds are from
the "Super Mario" game, and the home music and game music are
from web game "Roco Kingdom."
'''
def getSound(app):
    app.gameMusicplaying = False
    app.homeMusic = loadSound("sounds/home.mp3")
    app.gameMusic = loadSound("sounds/game.mp3")

    app.coinSound = loadSound("sounds/coin.mp3")
    app.jumpSound = loadSound("sounds/jump.mp3")
    app.countdownSound = loadSound("sounds/countdown.mp3")
    app.gameoverSound = loadSound("sounds/gameover.mp3")


'''
Note: the "recordBestScore" function is from the "highscore"
demo that the 15-112 website provided.
'''
# recording the best score and best score user
# if players get a new best score, a window comes out
# and allows players to text input their names
def recordBestScore(app):
    app.bestScore = 0
    app.bestScoreUser = ''

    if os.path.exists('bestScore.txt'):
        with open('bestScore.txt', 'r') as f:
            app.bestScore, app.bestScoreUser = f.read().split(',')
            app.bestScore = int(app.bestScore)

    if app.score > app.bestScore:
        app.bestScore = app.score
        app.bestScoreUser = app.getTextInput("New Best Score!! Enter Your Name:")
        with open('bestScore.txt', 'w+') as f:
            f.write(str(app.score) + ',' + app.bestScoreUser)

    setActiveScreen('gameover')

# recording the total coins
def recordCoins(app):
    if os.path.exists('coinsTotal.txt'):
        with open('coinsTotal.txt', 'r') as f:
            app.coinsTotal = f.read()
            app.coinsTotal = int(app.coinsTotal)
    else:
        app.coinsTotal = 0

    app.coinsTotal += app.coinsEarned
    with open('coinsTotal.txt', 'w+') as f:
        f.write(str(app.coinsTotal))


# SCREEN 1: INSTRUCTION
# this screen is shown when players first open the game
def instruction_redrawAll(app):
    app.game.drawInstructionScreen()

def instruction_onMouseMove(app, mouseX, mouseY):
    if 570 < mouseX < 630 and 600 < mouseY < 640:
        app.game.ok = True
    else:
        app.game.ok = False

def instruction_onMousePress(app, mouseX, mouseY):
    if 570 < mouseX < 630 and 600 < mouseY < 640:
        setActiveScreen('start')
        app.homeMusic.play(loop = True)


# SCREEN 2: START
def start_redrawAll(app):
    # draw the main screen
    app.game.drawOpenScreen()
    drawLabel(app.coinsTotal, 1000, 33, fill='white', 
              size=30, align='right')
    
    # draw the bunny
    app.bunny.drawStartpageBunny()
    
    # if players purchased any upgrade in the store,
    # the logo will be shown at the bottom of start screen
    if app.bunny.anticoffeine:
        drawImage(app.item.anticoffeine, 475, 690,
                  width=100, height=100, align='center')
    if app.bunny.antifreeze:
        drawImage(app.item.antifreeze, 595, 690,
                  width=100, height=100, align='center')
    if app.bunny.shield:
        drawImage(app.item.shield, 715, 690,
                  width=100, height=100, align='center')

def start_onMousePress(app, mouseX, mouseY):
    # the "PLAY" button
    if 520 < mouseY < 630 and 425 < mouseX < 775:
        setActiveScreen('parkour')
        app.homeMusic.pause()
        app.gameMusic.play(loop = True)
        app.gameMusicplaying = True
    # the "menu" button
    if 20 < mouseY < 83 and 20 < mouseX < 86:
        setActiveScreen('menu')

    # pressing different body parts of the bunny could
    # lead to its different reactions
    # pressing its head:
    if ((app.bunny.startpageX < mouseX < app.bunny.startpageX + 90 and
        390 < mouseY < 450 and app.bunny.right) or
        (app.bunny.startpageX - 90 < mouseX < app.bunny.startpageX and
        390 < mouseY < 450 and app.bunny.right == False)):
        app.bunny.happy = True
        app.bunny.happyCounter = 20
    # pressing its body:
    if ((app.bunny.startpageX - 90 < mouseX < app.bunny.startpageX and
        390 < mouseY < 490 and app.bunny.right) or
        (app.bunny.startpageX < mouseX < app.bunny.startpageX + 90 and
        390 < mouseY < 490 and app.bunny.right == False)):
        app.bunny.angry = True
        app.bunny.angryCounter = 20

def start_onStep(app):
    app.bunny.runCounter = (1 + app.bunny.runCounter) % 2
    if app.bunny.runCounter == 0:
        app.bunny.counter = (1 + app.bunny.counter) % 2

    if app.bunny.happyCounter != 0:
        app.bunny.happyCounter -= 1
        if app.bunny.happyCounter == 0:
            app.bunny.happy = False
    if app.bunny.angryCounter != 0:
        app.bunny.angryCounter -= 1
        if app.bunny.angryCounter == 0:
            app.bunny.angry = False

    if (app.bunny.startpageX < 1000 and app.bunny.right == True and
        not app.bunny.happy and not app.bunny.angry):
        app.bunny.startpageX += 5
        if app.bunny.startpageX == 1000:
            app.bunny.right = False
    if (app.bunny.startpageX > 600 and app.bunny.right == False and
        not app.bunny.happy and not app.bunny.angry):
        app.bunny.startpageX -= 5
        if app.bunny.startpageX == 600:
            app.bunny.right = True


# SCREEN 3: MENU
def menu_redrawAll(app):
    app.game.drawMenuScreen()

def menu_onMouseMove(app, mouseX, mouseY):
    if 405 < mouseX < 795 and 580 < mouseY < 620:
        app.game.seeInstructions = True
    else:
        app.game.seeInstructions = False

# letting players to choose whichever screen to go to
def menu_onMousePress(app, mouseX, mouseY):
    if 370 < mouseY < 522:
        if 306 < mouseX < 460:
            setActiveScreen('start')
            if app.gameMusicplaying == True:
                app.gameMusic.pause()
                app.homeMusic.play(loop = True)
                app.gameMusicplaying == False
        if 536 < mouseX < 690:
            setActiveScreen('parkour')
            if app.gameMusicplaying == False:
                app.homeMusic.pause()
                app.gameMusic.play(loop = True)
                app.gameMusicplaying == True
        if 745 < mouseX < 900:
            setActiveScreen('store')
            if app.gameMusicplaying == True:
                app.gameMusic.pause()
                app.homeMusic.play(loop = True)
                app.gameMusicplaying == False
    if 405 < mouseX < 795 and 580 < mouseY < 620:
        setActiveScreen('instruction')
        if app.gameMusicplaying == True:
                app.gameMusic.pause()
                app.homeMusic.play(loop = True)
                app.gameMusicplaying == False


# SCREEN 4: GAMEOVER
def gameover_redrawAll(app):
    app.game.drawGameOverScreen()
    # best score and best score user is shown when game is over
    drawLabel(f'Best Score: {app.bestScore} by {app.bestScoreUser}',
              600, 300, fill='white', size=40, font='cinzel', align='center')

# letting players to choose whichever screen to go to
# always automatically reset the game
def gameover_onMousePress(app, mouseX, mouseY):
    if 440 < mouseY < 590:
        if 306 < mouseX < 460:
            reset(app)
            setActiveScreen('start')
            app.gameMusic.pause()
            app.homeMusic.play(loop = True)
            app.gameMusicplaying == False
        if 536 < mouseX < 690:
            reset(app)
            setActiveScreen('parkour')
        if 745 < mouseX < 900:
            reset(app)
            setActiveScreen('store')
            app.gameMusic.pause()
            app.homeMusic.play(loop = True)
            app.gameMusicplaying == False


# SCREEN 5: STORE
def store_redrawAll(app):
    app.game.drawStore()
    if app.bunny.anticoffeine:
        drawImage(app.item.purchased, 376, 600,
                  width=121, height = 50, align='center')
    if app.bunny.antifreeze:
        drawImage(app.item.purchased, 601, 600,
                  width=121, height = 50, align='center')
    if app.bunny.shield:
        drawImage(app.item.purchased, 830, 600,
                  width=121, height = 50, align='center')

def store_onMousePress(app, mouseX, mouseY):
    # letting players to go back to start screen
    if 930 < mouseX < 980 and 100 < mouseY < 150:
        setActiveScreen('start')

    # players can purchase upgrades in the store
    # the system is recording the changes of total coins
    elif 575 < mouseY < 625:
        if (326 < mouseX < 426 and not app.bunny.anticoffeine and
            app.coinsTotal >= 200):
            app.coinsTotal -= 200
            with open('coinsTotal.txt', 'w+') as f:
                f.write(str(app.coinsTotal))
            app.bunny.anticoffeine = True
        elif (553 < mouseX < 653 and not app.bunny.antifreeze and
              app.coinsTotal >= 200):
            app.coinsTotal -= 200
            with open('coinsTotal.txt', 'w+') as f:
                f.write(str(app.coinsTotal))
            app.bunny.antifreeze = True
        elif (778 < mouseX < 878 and not app.bunny.shield and
              app.coinsTotal >= 100):
            app.coinsTotal -= 100
            with open('coinsTotal.txt', 'w+') as f:
                f.write(str(app.coinsTotal))
            app.bunny.shield = True


# SCREEN 6: PARKOUR
def parkour_redrawAll(app):
    app.game.drawParkour()
    app.item.drawLand()
    if app.gamestartCounter > 20:
        drawLabel('3', 600, 100, size=100, font='cinzel', 
                  fill='pink', bold=True, border='black', borderWidth=1)
    elif app.gamestartCounter > 10:
        drawLabel('2', 600, 100, size=100, font='cinzel', 
                  fill='pink', bold=True, border='black', borderWidth=1)
    elif app.gamestartCounter > 0:
        drawLabel('1', 600, 100, size=100, font='cinzel', 
                  fill='pink', bold=True, border='black', borderWidth=1)
    else:
        drawLabel(app.score, 600, 100, size=100, font='cinzel', 
                  fill='white', bold=True, border='black', borderWidth=1)
        drawLabel(f'Coins: {app.coinsEarned}', 1150, 40, fill='white',
                  size=25, font='cinzel', align='right')
    app.bunny.drawBunny()
    app.item.drawItems()

# the player can click the mouse to jump the bunny
def parkour_onMousePress(app, mouseX, mouseY):
    if 20 < mouseY < 83 and 20 < mouseX < 86:
        setActiveScreen('menu')
        app.gameMusic.pause()
        if not app.game.over:
            app.game.paused = True
    if app.game.paused:
        if 500 < mouseX < 700 and 250 < mouseY < 300:
            app.game.paused = False
    elif app.game.over:
        if 500 < mouseX < 700 and 250 < mouseY < 300:
            reset(app)

# the bunny can double jump (at most)
    elif not app.bunny.frozen:
        app.jumpSound.play(restart = True)
        if app.item.landscape != [] and app.landIndex != None:
            app.thisland = app.item.landscape[app.landIndex]
            if not app.bunny.isjumping and app.bunny.y == app.thisland['y']:
                app.bunny.isjumping = True
                app.bunny.speed = 30
                app.bunny.jumptimes = 1
                app.bunny.jumpCounter = 5
                bunnyJump(app)
            elif app.bunny.jumptimes == 1:
                app.bunny.isjumping = True
                app.bunny.speed = 30
                app.bunny.jumptimes = 2
                app.bunny.jumpCounter = 5
                bunnyJump(app)
            elif app.bunny.jumptimes == 2:
                pass

# the player can press "space" to jump the bunny
def parkour_onKeyPress(app, key):
        if key == 'space' and not app.bunny.frozen:
            app.jumpSound.play(restart = True)
            if app.item.landscape != [] and app.landIndex != None:
                app.thisland = app.item.landscape[app.landIndex]
                if not app.bunny.isjumping and app.bunny.y == app.thisland['y']:
                    app.bunny.isjumping = True
                    app.bunny.speed = 30
                    app.bunny.jumptimes = 1
                    app.bunny.jumpCounter = 5
                    bunnyJump(app)
                elif app.bunny.jumptimes == 1:
                    app.bunny.isjumping = True
                    app.bunny.speed = 30
                    app.bunny.jumptimes = 2
                    app.bunny.jumpCounter = 5
                    bunnyJump(app)
                elif app.bunny.jumptimes == 2:
                    pass

def parkour_onStep(app):
    # controlling the dynamic animations
    app.bunny.runCounter = (1 + app.bunny.runCounter) % 3
    if app.bunny.runCounter == 0:
        app.bunny.counter = (1 + app.bunny.counter) % 2
    app.bunny.shieldrunCounter = (1 + app.bunny.shieldrunCounter) % 3
    if app.bunny.shieldrunCounter == 0:
        app.bunny.shieldCounter = (1 + app.bunny.shieldCounter) % 2

    app.bunny.crazyCounter = (1 + app.bunny.crazyCounter) % 2
    app.item.coinCounter = (1 + app.item.coinCounter) % 5
    app.item.bombCounter = (1 + app.item.bombCounter) % 3

    if app.gamestartCounter > 0:
        app.countdownSound.play()
        app.gamestartCounter -= 1
        app.bunny.y += 10
    if app.gamestartCounter == 0:
        app.game.speed = 10
        app.gamestartCounter -= 1

    if not app.game.paused and not app.game.over:
        bunnyJump(app)
        app.item.timeToNextItem -= 1
        app.item.timeToNextLand -= 1
        checkForCollision(app)

        # randomly generating the items
        if app.item.timeToNextItem == 0:
            app.item.loadNextItem()
            app.item.timeToNextItem = random.randint(5, 15)
            app.game.speed += 0.3
            app.gamespeedHelper += 0.3

        if app.item.list != []:
            for item in app.item.list:
                item['x'] -= app.game.speed

        # randomly generating the landscape
        if app.item.timeToNextLand == 0:
            app.item.loadLandscape()
            app.item.timeToNextLand = 300//app.game.speed
      
        if app.item.landscape != []:
            for land in app.item.landscape:
                land['x'] -= app.game.speed
                # controlling the bunny to stay on landscape
                if land['x']-200 < app.bunny.x < land['x']+200:
                    app.landIndex = app.item.landscape.index(land)
                    if not app.bunny.isjumping:
                        app.bunny.y = land['y']
                # check if the bunny falls down the gap
                elif (app.landIndex != None and
                      len(app.item.landscape) > app.landIndex + 1):
                    app.thisland = app.item.landscape[app.landIndex]
                    app.nextland = app.item.landscape[app.landIndex+1]
                    if (app.bunny.x > app.thisland['x']+270 and
                        app.bunny.x < app.nextland['x']-250 and
                        not app.bunny.isjumping):
                        if app.bunny.y < 800:
                            app.bunny.y += 20
                        if app.bunny.y >= 800:
                            app.game.over = True
                            app.bunny.dies = True
                            app.game.overCounter = 10
                            app.gameMusic.pause()
                            app.gameoverSound.play()

    # controlling the frozen time of bunny
    if app.bunny.frozen:
        app.bunny.frozenCounter -= 1
        if app.bunny.frozenCounter == 0:
            app.bunny.frozen = False

    # controlling time before setting gameover screen
    if app.game.overCounter != 0:
        app.game.overCounter -= 1
        if app.game.overCounter == 0:
            recordBestScore(app)
    
    # controlling game speed when bunny jumps
    if app.bunny.isjumping:
        if app.bunny.jumpCounter == 5:
            app.game.speed += 30
        app.bunny.jumpCounter -= 1

        if app.bunny.jumpCounter == 0:
            app.bunny.isjumping = False
            app.gamespeedCounter = 3

    if app.gamespeedCounter > 0:
        app.gamespeedCounter -= 1
        if app.gamespeedCounter == 0:   
            app.game.speed = app.gamespeedHelper

    # controlling the vertical speed of bunny affected by gravity
    if not app.bunny.isOnLand:
        app.bunny.speed -= app.bunny.gravity

# check if the bunny is on land
def checkOnLand(app):
    if app.landIndex == None:
        app.bunny.isOnLand = False
    if app.item.landscape != [] and app.landIndex != None:
        app.thisland = app.item.landscape[app.landIndex]
        if app.bunny.y < app.thisland['y']:
            app.bunny.isOnLand = False
        else:
            app.bunny.isOnLand = True

# when the bunny jumps and falls, it stays on the landscape
def bunnyJump(app):
    if app.item.landscape != [] and app.landIndex != None:
        app.thisland = app.item.landscape[app.landIndex]
        if not app.bunny.frozen:
            if app.bunny.isjumping == True:
                app.bunny.y -= app.bunny.speed
                if app.bunny.y < app.thisland['y']-200:
                    app.bunny.y = app.thisland['y']-200
            if app.bunny.isjumping == False and app.bunny.y < app.thisland['y']:
                app.bunny.y -= app.bunny.speed
                if app.bunny.y > app.thisland['y']:
                    app.bunny.y = app.thisland['y']


# checking for collision between bunny and items
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def checkForCollision(app):
    if app.item.list != None:
        for item in app.item.list:
            d = distance(item['x'], item['y'], app.bunny.x, app.bunny.y)
            if d <= 80:
                i = app.item.list.index(item)
                app.item.list.pop(i)

                if item['name'] == app.item.coin:
                    app.coinSound.play(restart = True)
                    app.coinsEarned += 10
                    app.coinsTotal += 10
                    app.score += app.game.point
                elif item['name'] == app.item.bomb:
                    if app.bunny.shield:
                        app.bunny.shield = False
                    else:
                        app.gameMusic.pause()
                        app.gameoverSound.play()
                        app.game.over = True
                        app.bunny.dies = True
                        app.game.overCounter = 10
                elif item['name'] == app.item.ice and not app.bunny.antifreeze:
                    app.bunny.frozen = True
                    app.bunny.frozenCounter = 20
                elif item['name'] == app.item.coffee and not app.bunny.anticoffeine:
                    app.bunny.crazy = True
                    app.game.speed += 10
                    app.gamespeedHelper += 10
                else:
                    app.score += app.game.point

def main():
    runAppWithScreens('instruction', height=800, width=1200)

main()