from os import system, name
import keyboard

# u see my ass? 🍑

def clear_screen() -> None:
    system('cls' if name == 'nt' else 'clear')
    
def rgb(text: str, clr) -> str:
    if type(clr) == str:
        r, g, b = clr[4:-1].replace(',', '').split()
    else:
        r, g, b = clr
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def play(dx: int, dy: int):
    global pos_x, pos_y
    board[pos_y][pos_x] = piece
    pos_x = (pos_x + dx) % board_size[0]
    pos_y = (pos_y + -dy) % board_size[1]
    board[pos_y][pos_x] = player
    display_board()

def display_board() -> None:
    clear_screen()
    for row in board:
        for i in row:
            if i == player:
                print(rgb(i, 'rgb(230, 185, 166)'), end=' ')
            else:
                print(rgb(i, 'rgb(47, 54, 69)'), end=' ')
        print()

def display_menu(step: int) -> None:
    clear_screen()
    print(rgb("\tWelcome!", 'rgb(54, 186, 152)'))
    global pos_menu
    pos_menu = (pos_menu - step) % len(menu)
    for i in range(len(menu)):
        if i == pos_menu:
            print(rgb(f'-> {menu[i]}', 'rgb(233, 196, 106)'))
        else:
            print(rgb(f'{menu[i]}', 'rgb(231, 111, 81)'))

def menu_choice() -> None:
    if pos_menu == 0:
        global start; start = not start
        display_board()
    elif pos_menu == 1:
        clear_screen()
        print(rgb("Arindam gender reveal hole or pole??? (⊙o⊙) ??: ", 'rgb(228, 155, 255)'), rgb('g', 'rgb(255, 0, 0)'), rgb('a', 'rgb(0, 255, 0)'), rgb('y', 'rgb(0, 0, 255)'), sep='')
        from time import sleep
        sleep(2)
        display_menu(pos_menu)
    elif pos_menu == 2:
        pass
    elif pos_menu == 3:
        quit()

def get_key() -> None:
    event: keyboard.KeyboardEvent = keyboard.read_event(suppress=True)
    if event.event_type == keyboard.KEY_UP:
        key: str = event.name.lower()
    else: return

    global start
    if start:
        if key in ['esc', 'x', 'q']:
            start = not start
            global pos_x, pos_y
            board[pos_y][pos_x] = piece
            pos_x = pos_y = 0
            display_menu(pos_menu)
        elif key in ['up', 'w']:
            play(0, 1)
        elif key in ['left', 'a']:
            play(-1, 0)
        elif key in ['down', 's']:
            play(0, -1)
        elif key in ['right', 'd']:
            play(1, 0)
    else:
        if key in ['esc', 'x', 'q']:
            quit()
        elif key in ['up', 'w']:
            display_menu(1)
        elif key in ['down', 's']:
            display_menu(-1)
        elif key == 'enter':
            menu_choice()

def main() -> None:
    clear_screen()
    display_menu(0)
    game: bool = True
    while game:
        get_key()

if __name__ == "__main__":
    start: bool = False
    menu: list[str] = ['Start', 'About', 'Settings maybe', 'Exit [esc, x, q]']
    pos_menu: int = 0; pos_x: int = 0; pos_y: int = 0
    board_size: tuple[int, int] = (9, 9)
    piece: str = '📦'; player: str = ' ψ'
    board: list[list] = [[piece for _ in range(board_size[0])] for _ in range(board_size[1])]
    board[pos_y][pos_x] = player
    main()
