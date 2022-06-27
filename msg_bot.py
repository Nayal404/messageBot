import pyautogui as pg 
import time 
# lets put these all in a function
def loopIt():
    # you can have fun by removing times too
    time.sleep(3)
    # let's see the cursor position in submit logo
    # So, the position is Point(x=989, y=697)
    # print(pg.position())
    cursor = pg.moveTo(989, 697)
    msg = 'Hello, This is a sample message for you!'
    pg.typewrite(msg)
    time.sleep(2)
    pg.click(cursor)
    # let's see if it submits the msg or not
    # Now to irritate our friend lets
    # do a loop and you can also remove the timing too!
while True:
    if __name__ == "__main__":
        loopIt()
        # Press CTRL+C to quit program