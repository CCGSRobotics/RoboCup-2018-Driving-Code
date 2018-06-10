import evdev

gamepads = []
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
count = False

# controllers is a set for faster access.
controllers = {"Logitech Gamepad F310",
               "Logitech Gamepad F710",
               "Microsoft X-Box 360 pad",
               "Logitech Logitech Cordless RumblePad 2",
               "Logitech Logitech Dual Action"}

gamepad = None
for i in devices:
    if i.name in controllers:
        gamepad = i
        break

assert gamepad # Ensure that the gamepad is assigned

print("your gamepad is:",gamepad)


