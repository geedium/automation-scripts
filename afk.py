import ctypes, time, datetime, random

mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001
# MOUSEEVENTF_LEFTDOWN = 0x0002
# MOUSEEVENTF_LEFTUP = 0x0004
print("press ctrl-c to end mouse shaker")
print("BE RIGHT BACK...")
try:
    while True:
        mouse_event(MOUSEEVENTF_MOVE,25,0,0,0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE,0,25,0,0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE,-25,0,0,0)
        time.sleep(1)
        mouse_event(MOUSEEVENTF_MOVE,0,-25,0,0)
        time.sleep(1)
        # wait randomly
        # delay = random.randint(0,5)
        # time.sleep(delay)
        # mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        # time.sleep(2)
        # mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0)
        # time.sleep(2)
except KeyboardInterrupt:
    pass
