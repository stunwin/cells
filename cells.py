import pygame

width = 1200
height = 600
cwidth = width / 4 # TODO calculate these in controls function 
cheight = height / 4 # calculate these in controls function 
con_x = width - cwidth # calculate these in controls function 
w = 5 #TODO rename this is cell width 
rule_number = 182
rules_int = bin(rule_number)[2:].zfill(8)
rules = []
for i in rules_int:
    rules.append(int(i))


def main():
    
    #TODO make some kind of init function for these
    gen = 0
    current = []    
    
    for i in range(0, int(width / w)):
        current.append(0)
    current[int(len(current) / 2)] = 1
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill("white")
    clock = pygame.time.Clock()
    running = True

    # /init function go here

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.flip()    
        clock.tick(60)
        
        pygame.draw.rect(screen, "black", (con_x, 0, cwidth, cheight), width = 3)
        buttons(cwidth, cheight, screen, con_x, cheight * .25, 3, 1, 2)
        b_buttons(cwidth, cheight, screen, con_x, cheight, 8, .5)
        draw_current(current, screen, gen)
        current = update_generation(current)
        gen += 1
        
# ------- THIS IS THE END OF THE MAIN FUNCTION -----------#

def draw_current(current, screen, generation):
    for (i, j) in enumerate(current):
        if j == 1:
            pygame.draw.rect(screen, "black", (i * w, generation * w, w, w))
        
def update_generation(current):
    next = []
    for (i, j) in enumerate(current):
        if i == 0:
            left = str(current[-1])
            center = str(j)
            right = str(current[i + 1])
            
        elif i == len(current) - 1:    
            left = str(current[i - 1])
            center = str(j)
            right = str(current[0])
                        
        else:
            left = str(current[i - 1])
            center = str(j)
            right = str(current[i + 1])
            
        result = int(left + center + right, 2)
        next.append(int(rules[7-result]))
    return next
    
def buttons(cwidth, cheight, screen, con_x, y_offset, button_count, padding, width):
    button_width = cwidth / (button_count + padding)
    button_height = button_width
    button_space = (cwidth - button_width * button_count) / (button_count + 1)
    
    for i in range (1, button_count + 1):
        pygame.draw.rect(screen, "black", (con_x + button_space * i + button_width * (i - 1), y_offset, button_width, button_height), width)
            
def b_buttons(cwidth, cheight, screen, con_x, y_offset, button_count, padding):
    button_width = cwidth / (button_count + padding)
    button_height = button_width
    button_space = (cwidth - button_width * button_count) / (button_count + 1)
    
    for (i, j) in enumerate(rules):
        width = 1 - j
        pygame.draw.rect(screen, "black", (con_x + button_space * (i + 1) + button_width * (i), y_offset, button_width, button_height), width)
        if mousey(con_x + button_space * (i + 1) + button_width * (i), y_offset, button_width, button_height) and pygame.mouse.get_pressed()[0]:
            rules[i] = width
            
        
def mousey(button_x, button_y, button_w, button_h):
    if (pygame.mouse.get_pos()[0] > button_x and pygame.mouse.get_pos()[0] < button_x + button_w and pygame.mouse.get_pos()[1] > button_y and pygame.mouse.get_pos()[1] < button_y + button_h):
        return True
    else:
        return False 
            
        
        









main()