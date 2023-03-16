import pyautogui as pag
import sys
import multiprocessing as mp

# https://pyautogui.readthedocs.io/en/latest/mouse.html#mouse-movement
# dual monitors: https://pypi.org/project/screeninfo/
# or use pypi mss

print(f'Location {pag.position()}')
print(f'Screen Size {pag.size()}')
print(type(pag.size()))

SECONDS = 1
screen = pag.size()

x_start = screen.width/4
x_end = screen.width/4 * 3

y = screen.height/2

def look_active():
    while True:
        mouse = pag.position()
        if mouse.x == x_start:
            pag.moveTo(x_end, y, SECONDS)
        elif mouse.x == x_end:
            pag.moveTo(x_start, y, SECONDS)

def check_active():
    while True:
        mouse = pag.position()
        if mouse.y != y:
            break

# https://superfastpython.com/kill-a-thread-in-python/
def main():
    pag.moveTo(x_start, y, 1)
    fake = mp.Process(target=look_active)
    fake.start()

    # Program will check mouse position until it moves up or down
    check_active()
    fake.terminate()
    
if __name__ == '__main__':
    main()
    print('Hello again!')
    sys.exit()
