from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

windows = CGWindowListCopyWindowInfo(
    0,
    kCGNullWindowID
)

for w in windows:
    print("Owner:", w.get("kCGWindowOwnerName"))
    print("Name:", w.get("kCGWindowName"))
    print("---")