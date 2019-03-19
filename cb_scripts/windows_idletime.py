#!/usr/bin/env python3

"""Windows Idletime - move mouse on idle time.

Program to move and click mouse to keep computer session alive.
Group policy for Screensaver/Locking of workstation.

"""
import platform
import sys

if platform.system().lower() == 'windows':
    from ctypes import Structure, windll, c_uint, sizeof, byref
    from time import sleep
else:
    print("This script is intended for Windows OS.")
    sys.exit(0)


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


class IdleWatcher:
    """Idle time watcher."""

    def __init__(self, idle_time: int):
        self.IDLETIME = idle_time

    def idle_duration(self):
        """Get the idle time in seconds."""
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0

    def move_mouse_and_click(self):
        """Move mouse to top left corner and click."""
        windll.user32.SetCursorPos(0, 0)
        windll.user32.mouse_event(2, 0, 0, 0, 0)
        windll.user32.mouse_event(4, 0, 0, 0, 0)
        print("Mouse Moved.")


def main():
    """Run the idle watcher and move mouse when needed."""
    idle_time = 600  # 10 minutes
    idle_watcher = IdleWatcher(idle_time=idle_time)
    try:
        while 1:
            if idle_watcher.idle_duration() >= idle_watcher.IDLETIME:
                idle_watcher.move_mouse_and_click()
            sleep(1)
    except KeyboardInterrupt:
        print("Exited.")
    return 0


if __name__ == "__main__":
    main()
