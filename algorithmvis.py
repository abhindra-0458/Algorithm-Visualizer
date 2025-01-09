import pygame
import random
pygame.init()

class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    BACKGROUND_COLOR = WHITE
    side_padding = 100
    top_padding = 200
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont('sans-serif', 30)
    LARGE_FONT = pygame.font.SysFont('sans-serif', 40)
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width = round((self.width - self.side_padding) / len(lst))
        self.block_height = round((self.height - self.top_padding) / (self.max_val - self.min_val))
        self.start_x = self.side_padding // 2

def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}",1,draw_info.RED)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))

    controls = draw_info.FONT.render("R - Reset | Space - Start Sorting | A - Ascending | D - Descending " , 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 35))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | M - Merge Sort" , 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 65))

    drawlist(draw_info)
    pygame.display.update()



def drawlist(draw_info, colorpositions={}, clear_bg = False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.side_padding//2, draw_info.top_padding, draw_info.width - draw_info.side_padding, draw_info.height - draw_info.top_padding)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]

        if i in colorpositions:
            color = colorpositions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg: 
        pygame.display.update()

def generate_unsorted_list(n, min_val, max_val):
    lst = []
    for i in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]

            if(num1> num2 and ascending) or (num1< num2 and not ascending):
                lst[j],lst[j+1]=lst[j+1],lst[j]
                drawlist(draw_info, {j:draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1,len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i>0 and lst[i-1]>current and ascending
            descending_sort = i>0 and lst[i-1]>current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i]=lst[i-1]
            i = i-1
            lst[i]=current
            drawlist(draw_info,{i-1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def merge(lst, left, mid, right):
        L = lst[left:mid+1]
        R = lst[mid+1:right+1]

        i = 0  
        j = 0 
        k = left  


        while i < len(L) and j < len(R):
            if (L[i] <= R[j] and ascending) or (L[i] >= R[j] and not ascending):
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            drawlist(draw_info, {k:draw_info.GREEN}, True)
            yield True
            k+=1


        while i < len(L):
            lst[k] = L[i]
            drawlist(draw_info, {k:draw_info.RED}, True)
            yield True
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            drawlist(draw_info, {k:draw_info.RED}, True)
            yield True
            j += 1
            k += 1

    def mergesort(lst, left, right):
        if left >= right:
            return 

        mid = (left + right) // 2
        yield from mergesort(lst, left, mid)
        yield from mergesort(lst, mid + 1, right)
        yield from merge(lst, left, mid, right)

    yield from mergesort(lst, 0, len(lst) - 1)



def main():
    run = True
    clock = pygame.time.Clock()
    n = 50
    min_val = 0
    max_val = 100
    lst = generate_unsorted_list(n, min_val, max_val)
    draw_info = DrawInfo(800, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None


    while run:
        clock.tick(40)
        draw(draw_info,sorting_algo_name,ascending)

        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info,sorting_algo_name,ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_unsorted_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algo_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and sorting == False:
                ascending = True
            elif event.key == pygame.K_i and sorting == False:
                sorting_algo_name = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and sorting == False:
                sorting_algo_name = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_d and sorting == False:
                ascending = False
            elif event.key == pygame.K_m:
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"



    pygame.quit()

if __name__ == "__main__":
    main()
