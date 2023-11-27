height = int(input("Define height: "))
width = int(input("Define width: "))

def draw_rectangle(width, height):
    print("|" + "-" * (width - 2) + "|")
    for i in range(height - 2):
        print("|" + " " * (width - 2) + "|")
    print("|" + "-" * (width - 2) + "|")

draw_rectangle(width, height)