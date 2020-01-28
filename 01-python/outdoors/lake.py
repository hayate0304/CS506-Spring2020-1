def draw_lake(width = 5, length = 20):
    if width == 0 or length == 0:
        raise ValueError("width and length must be greater 0")
        
    for i in range(width):
        draw_vertical(False)
        
        if i == 0 or i == width - 1:
            for j in range(length):
                draw_horizontal()
        else:    
            for k in range(length):
                draw_wave()
        
        draw_vertical(True)
    return


def draw_horizontal():
    print("=", end = '')
    
def draw_vertical(newline = False):
    if newline == False:
        print("||", end = '')
    else:
        print("||")
    
def draw_wave():
    print("~", end = '')