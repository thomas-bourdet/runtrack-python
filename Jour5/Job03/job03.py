height = int(input("Define height: "))

def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == height - 1:
  
            print('/' + '_' * (2 * i ) + '\\')
        else:

            print(spaces + '/' + ' ' * (2 * i ) + '\\')

draw_triangle(height)

