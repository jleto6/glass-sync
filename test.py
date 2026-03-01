import win32gui


def enum_windows():
    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:  # ignore empty titles
                print(f"HWND: {hwnd} | Title: {title}")

    win32gui.EnumWindows(callback, None)


if __name__ == "__main__":
    enum_windows()