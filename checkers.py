import pygame
import csv
import os, sys


WIN_WIDTH = 700
WIN_HEIGHT = 700


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0, 2, 0, 2, 0, 2, 0, 2],
                      [2, 0, 2, 0, 2, 0, 2, 0],
                      [0, 2, 0, 2, 0, 2, 0, 2],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0]]
        self.move_board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.draw = False
        self.pos = None
        self.streak = False

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        k = 0
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                if i % 2 == k:
                    pygame.draw.rect(screen, 'white', (self.left + i * self.cell_size + 1, self.top + j * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2), 0)
                elif i % 2 != k:
                    pygame.draw.rect(screen, 'black', (self.left + i * self.cell_size + 1, self.top + j * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2), 0)
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 0
        for i in range(self.width):
            for j in range(self.height):
                    if self.board[j][i] == 1:
                        pygame.draw.circle(screen, 'red', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 2.5)
                    elif self.board[j][i] == 2:
                        pygame.draw.circle(screen, 'blue', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 2.5)
                    elif self.board[j][i] == 3:
                        pygame.draw.circle(screen, 'red', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 2.5)
                        pygame.draw.circle(screen, 'yellow', (self.left + i * self.cell_size + self.cell_size // 2,
                                                            self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 4)
                    elif self.board[j][i] == 4:
                        pygame.draw.circle(screen, 'blue', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 2.5)
                        pygame.draw.circle(screen, 'yellow', (self.left + i * self.cell_size + self.cell_size // 2,
                                                            self.top + j * self.cell_size + self.cell_size // 2), self.cell_size // 4)
                    elif self.board[j][i] == 5:
                        pygame.draw.circle(screen, 'green', (self.left + i * self.cell_size + self.cell_size // 2,
                                                            self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 2.5)
                        pygame.draw.circle(screen, 'red', (self.left + i * self.cell_size + self.cell_size // 2,
                                                              self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 4)
                    elif self.board[j][i] == 6:
                        pygame.draw.circle(screen, 'green', (self.left + i * self.cell_size + self.cell_size // 2,
                                                            self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 2.5)
                        pygame.draw.circle(screen, 'blue', (self.left + i * self.cell_size + self.cell_size // 2,
                                                              self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 4)
                    elif self.board[j][i] == 7:
                        pygame.draw.circle(screen, 'green', (self.left + i * self.cell_size + self.cell_size // 2,
                                                             self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 2.5)
                        pygame.draw.circle(screen, 'red', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 4)
                        pygame.draw.circle(screen, 'yellow', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 6)
                    elif self.board[j][i] == 8:
                        pygame.draw.circle(screen, 'green', (self.left + i * self.cell_size + self.cell_size // 2,
                                                             self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 2.5)
                        pygame.draw.circle(screen, 'blue', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 4)
                        pygame.draw.circle(screen, 'yellow', (self.left + i * self.cell_size + self.cell_size // 2,
                                                           self.top + j * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 6)

        for i in range(self.width):
            for j in range(self.height):
                if self.move_board[j][i] == 1:
                    pygame.draw.circle(screen, 'gray', (self.left + i * self.cell_size + self.cell_size // 2,
                                                          self.top + j * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 5)

    def check_checker(self, cell):
        global on_click
        if curent_player == 0:
            if self.board[cell[0]][cell[1]] == 1 and 3 not in self.board:
                self.board[cell[0]][cell[1]] = 3
                self.checker_pos = (cell[0], cell[1])
                self.can_move(cell)
                on_click = True
            elif self.board[cell[0]][cell[1]] == 5 and 3 not in self.board:
                self.board[cell[0]][cell[1]] = 7
                self.checker_pos = (cell[0], cell[1])
                self.can_move(cell)
                on_click = True
        elif curent_player == 1:
            if self.board[cell[0]][cell[1]] == 2 and 4 not in self.board:
                self.board[cell[0]][cell[1]] = 4
                self.checker_pos = (cell[0], cell[1])
                self.can_move(cell)
                on_click = True
            elif self.board[cell[0]][cell[1]] == 6 and 4 not in self.board:
                self.board[cell[0]][cell[1]] = 8
                self.checker_pos = (cell[0], cell[1])
                self.can_move(cell)
                on_click = True

    def get_coord(self, position):
        global on_click
        cell = ((position[1] - self.top) // self.cell_size, (position[0] - self.left) // self.cell_size)
        if not on_click:
            self.check_checker(cell)
        elif on_click:
            if self.checker_pos != cell:
                if self.board[self.checker_pos[0]][self.checker_pos[1]] == 7 or self.board[self.checker_pos[0]][self.checker_pos[1]] == 8:
                    self.move_checker(cell, kon=True)
                else:
                    self.move_checker(cell)
            else:
                if self.board[cell[0]][cell[1]] == 3:
                    self.board[cell[0]][cell[1]] = 1
                elif self.board[cell[0]][cell[1]] == 7:
                    self.board[cell[0]][cell[1]] = 5
                elif self.board[cell[0]][cell[1]] == 4:
                    self.board[cell[0]][cell[1]] = 2
                elif self.board[cell[0]][cell[1]] == 8:
                    self.board[cell[0]][cell[1]] = 6
                on_click = False

    def get_click(self, position):
        if self.left <= position[0] <= self.left + self.width * self.cell_size and self.top <= position[1] <= self.top + self.height * self.cell_size:
            self.get_coord(position)

    def move_checker(self, cell, kon=False):
        global on_click, curent_player
        if on_click:
            if curent_player == 0 and self.can_move(cell):
                if not kon:
                    self.board[cell[0]][cell[1]] = 1
                if kon:
                    self.board[cell[0]][cell[1]] = 5
                self.board[self.checker_pos[0]][self.checker_pos[1]] = 0
                if cell[0] == 0 and self.board[cell[0]][cell[1]] != 5:
                    self.board[cell[0]][cell[1]] = 5
                on_click = False
                curent_player = 1
            elif curent_player == 1 and self.can_move(cell):
                if not kon:
                    self.board[cell[0]][cell[1]] = 2
                if kon:
                    self.board[cell[0]][cell[1]] = 6
                self.board[self.checker_pos[0]][self.checker_pos[1]] = 0
                if cell[0] == 7 and self.board[cell[0]][cell[1]] != 6:
                    self.board[cell[0]][cell[1]] = 6
                on_click = False
                curent_player = 0

    def can_move(self, cell):
        self.move_board = [[0] * self.width for _ in range(self.height)]
        if self.board[self.checker_pos[0]][self.checker_pos[1]] == 3:
            if self.checker_pos[0] - 1 >= 0 and self.checker_pos[1] - 1 >= 0:
                if self.board[self.checker_pos[0] - 1][self.checker_pos[1] - 1] == 0:
                    self.move_board[self.checker_pos[0] - 1][self.checker_pos[1] - 1] = 1
                elif self.board[self.checker_pos[0] - 1][self.checker_pos[1] - 1] == 2 or self.board[self.checker_pos[0] - 1][self.checker_pos[1] - 1] == 6:
                    if self.checker_pos[0] - 2 >= 0 and self.checker_pos[1] - 2 >= 0:
                        if self.board[self.checker_pos[0] - 2][self.checker_pos[1] - 2] == 0:
                            self.move_board[self.checker_pos[0] - 2][self.checker_pos[1] - 2] = 1
            if self.checker_pos[0] - 1 >= 0 and self.checker_pos[1] + 1 <= 7:
                if self.board[self.checker_pos[0] - 1][self.checker_pos[1] + 1] == 0:
                    self.move_board[self.checker_pos[0] - 1][self.checker_pos[1] + 1] = 1
                elif self.board[self.checker_pos[0] - 1][self.checker_pos[1] + 1] == 2 or self.board[self.checker_pos[0] - 1][self.checker_pos[1] + 1] == 6:
                    if self.checker_pos[0] - 2 >= 0 and self.checker_pos[1] + 2 <= 7:
                        if self.board[self.checker_pos[0] - 2][self.checker_pos[1] + 2] == 0:
                            self.move_board[self.checker_pos[0] - 2][self.checker_pos[1] + 2] = 1
        elif self.board[self.checker_pos[0]][self.checker_pos[1]] == 4:
            if self.checker_pos[0] + 1 <= 7 and self.checker_pos[1] + 1 <= 7:
                if self.board[self.checker_pos[0] + 1][self.checker_pos[1] + 1] == 0:
                    self.move_board[self.checker_pos[0] + 1][self.checker_pos[1] + 1] = 1
                elif self.board[self.checker_pos[0] + 1][self.checker_pos[1] + 1] == 1 or self.board[self.checker_pos[0] + 1][self.checker_pos[1] + 1] == 5:
                    if self.checker_pos[0] + 2 <= 7 and self.checker_pos[1] + 2 <= 7:
                        if self.board[self.checker_pos[0] + 2][self.checker_pos[1] + 2] == 0:
                            self.move_board[self.checker_pos[0] + 2][self.checker_pos[1] + 2] = 1
            if self.checker_pos[0] + 1 <= 7 and self.checker_pos[1] - 1 >= 0:
                if self.board[self.checker_pos[0] + 1][self.checker_pos[1] - 1] == 0:
                    self.move_board[self.checker_pos[0] + 1][self.checker_pos[1] - 1] = 1
                elif self.board[self.checker_pos[0] + 1][self.checker_pos[1] - 1] == 1 or self.board[self.checker_pos[0] + 1][self.checker_pos[1] - 1] == 5:
                    if self.checker_pos[0] + 2 <= 7 and self.checker_pos[1] - 2 >= 0:
                        if self.board[self.checker_pos[0] + 2][self.checker_pos[1] - 2] == 0:
                            self.move_board[self.checker_pos[0] + 2][self.checker_pos[1] - 2] = 1
        # проверка хода активированной красный дамки
        elif self.board[self.checker_pos[0]][self.checker_pos[1]] == 7:
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[0] + i <= 7 and self.checker_pos[1] + i <= 7:
                            if self.board[self.checker_pos[0] + i][self.checker_pos[1] + i] == 0:
                                self.move_board[self.checker_pos[0] + i][self.checker_pos[1] + i] = 1
                            elif self.board[self.checker_pos[0] + i][self.checker_pos[1] + i] == 2 or \
                                    self.board[self.checker_pos[0] + i][self.checker_pos[1] + i] == 6:
                                if self.checker_pos[0] + i + 1 <= 7 and self.checker_pos[1] + i + 1 <= 7:
                                    if self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] + i + 1] == 2 or \
                                    self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] + i + 1] == 6:
                                        self.move_board[self.checker_pos[0] + i + 1][self.checker_pos[1] + i + 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[0] - i >= 0 and self.checker_pos[1] - i >= 0:
                            if self.board[self.checker_pos[0] - i][self.checker_pos[1] - i] == 0:
                                self.move_board[self.checker_pos[0] - i][self.checker_pos[1] - i] = 1
                            elif self.board[self.checker_pos[0] - i][self.checker_pos[1] - i] == 2 or \
                                    self.board[self.checker_pos[0] - i][self.checker_pos[1] - i] == 6:
                                if self.checker_pos[0] - i - 1 >= 0 and self.checker_pos[1] - i - 1 >= 0:
                                    if self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] - i - 1] == 2 or \
                                    self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] - i - 1] == 6:
                                        self.move_board[self.checker_pos[0] - i - 1][self.checker_pos[1] - i - 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[1] + i <= 7 and self.checker_pos[1] - i >= 0:
                            if self.board[self.checker_pos[0] + i][self.checker_pos[1] - i] == 0:
                                self.move_board[self.checker_pos[0] + i][self.checker_pos[1] - i] = 1
                            elif self.board[self.checker_pos[0] + i][self.checker_pos[1] - i] == 2 or \
                                    self.board[self.checker_pos[0] + i][self.checker_pos[1] - i] == 6:
                                if self.checker_pos[0] + i + 1 <= 7 and self.checker_pos[1] - i - 1 >= 0:
                                    if self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] - i - 1] == 2 or \
                                    self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] - i - 1] == 6:
                                        self.move_board[self.checker_pos[0] + i + 1][self.checker_pos[1] - i - 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[1] - i >= 0 and self.checker_pos[1] + i <= 7:
                            if self.board[self.checker_pos[0] - i][self.checker_pos[1] + i] == 0:
                                self.move_board[self.checker_pos[0] - i][self.checker_pos[1] + i] = 1
                            elif self.board[self.checker_pos[0] - i][self.checker_pos[1] + i] == 2 or \
                                    self.board[self.checker_pos[0] - i][self.checker_pos[1] + i] == 6:
                                if self.checker_pos[0] - i - 1 >= 0 and self.checker_pos[1] + i + 1 <= 7:
                                    if self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] + i + 1] == 2 or \
                                    self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] + i + 1] == 6:
                                        self.move_board[self.checker_pos[0] - i - 1][self.checker_pos[1] + i + 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False

        # проверка хода активированной синей дамки
        elif self.board[self.checker_pos[0]][self.checker_pos[1]] == 8:
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[0] + i <= 7 and self.checker_pos[1] + i <= 7:
                            if self.board[self.checker_pos[0] + i][self.checker_pos[1] + i] == 0:
                                self.move_board[self.checker_pos[0] + i][self.checker_pos[1] + i] = 1
                            elif self.board[self.checker_pos[0] + i][self.checker_pos[1] + i] == 1 or self.board[self.checker_pos[0] + i][self.checker_pos[1] + i] == 5:
                                if self.checker_pos[0] + i + 1 <= 7 and self.checker_pos[1] + i + 1 <= 7:
                                    if self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] + i + 1] == 1 or self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] + i + 1] == 5:
                                        self.move_board[self.checker_pos[0] + i + 1][self.checker_pos[1] + i + 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[0] - i >= 0 and self.checker_pos[1] - i >= 0:
                            if self.board[self.checker_pos[0] - i][self.checker_pos[1] - i] == 0:
                                self.move_board[self.checker_pos[0] - i][self.checker_pos[1] - i] = 1
                            elif self.board[self.checker_pos[0] - i][self.checker_pos[1] - i] == 1 or self.board[self.checker_pos[0] - i][self.checker_pos[1] - i] == 5:
                                if self.checker_pos[0] - i - 1 >= 0 and self.checker_pos[1] - i - 1 >= 0:
                                    if self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] - i - 1] == 1 or self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] - i - 1] == 5:
                                        self.move_board[self.checker_pos[0] - i - 1][self.checker_pos[1] - i - 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[1] + i <= 7 and self.checker_pos[1] - i >= 0:
                            if self.board[self.checker_pos[0] + i][self.checker_pos[1] - i] == 0:
                                self.move_board[self.checker_pos[0] + i][self.checker_pos[1] - i] = 1
                            elif self.board[self.checker_pos[0] + i][self.checker_pos[1] - i] == 1 or self.board[self.checker_pos[0] + i][self.checker_pos[1] - i] == 5:
                                if self.checker_pos[0] + i + 1 <= 7 and self.checker_pos[1] - i - 1 >= 0:
                                    if self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] - i - 1] == 1 or self.board[self.checker_pos[0] + i + 1][self.checker_pos[1] - i- 1] == 5:
                                        self.move_board[self.checker_pos[0] + i + 1][self.checker_pos[1] - i - 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False
            try:
                if not stop:
                    for i in range(1, 8):
                        if self.checker_pos[1] - i >= 0 and self.checker_pos[1] + i <= 7:
                            if self.board[self.checker_pos[0] - i][self.checker_pos[1] + i] == 0:
                                self.move_board[self.checker_pos[0] - i][self.checker_pos[1] + i] = 1
                            elif self.board[self.checker_pos[0] - i][self.checker_pos[1] + i] == 1 or self.board[self.checker_pos[0] - i][self.checker_pos[1] + i] == 5:
                                if self.checker_pos[0] - i - 1 >= 0 and self.checker_pos[1] + i + 1 <= 7:
                                    if self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] + i + 1] == 1 or self.board[self.checker_pos[0] - i - 1][self.checker_pos[1] + i + 1] == 5:
                                        self.move_board[self.checker_pos[0] - i - 1][self.checker_pos[1] + i + 1] = 1
                                        stop = True
            except IndexError:
                pass
            stop = False

        if self.move_board[cell[0]][cell[1]] == 1:
            self.move_board = [[0] * self.width for _ in range(self.height)]
            if cell[0] - self.checker_pos[0] == -2 and cell[1] - self.checker_pos[1] == -2:
                self.board[self.checker_pos[0] - 1][self.checker_pos[1] - 1] = 0
            elif self.checker_pos[0] - cell[0] == -2 and self.checker_pos[1] - cell[1] == -2:
                self.board[self.checker_pos[0] + 1][self.checker_pos[1] + 1] = 0
            elif cell[0] - self.checker_pos[0] == -2 and self.checker_pos[1] - cell[1] == -2:
                self.board[self.checker_pos[0] - 1][self.checker_pos[1] + 1] = 0
            elif self.checker_pos[0] - cell[0] == -2 and cell[1] - self.checker_pos[1] == -2:
                self.board[self.checker_pos[0] + 1][self.checker_pos[1] - 1] = 0
            return True
        else:
            return False


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением {fullname} не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Игра Шашки",
                  "Классические шашки для двух играков"]

    fon = pygame.transform.scale(load_image('background.jpg'), (WIN_WIDTH, WIN_HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


def game_over_screen(winner, screen, cur_time):
    screen.fill((0, 0, 0))
    cur_time = round((cur_time / 15000), 2)
    name = ''
    if winner == 1:
        win = 'Красный'
    elif winner == 0:
        win = 'Синий'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    name += 'q'
                elif event.key == pygame.K_w:
                    name += 'w'
                elif event.key == pygame.K_e:
                    name += 'e'
                elif event.key == pygame.K_r:
                    name += 'r'
                elif event.key == pygame.K_t:
                    name += 't'
                elif event.key == pygame.K_y:
                    name += 'y'
                elif event.key == pygame.K_u:
                    name += 'u'
                elif event.key == pygame.K_i:
                    name += 'i'
                elif event.key == pygame.K_o:
                    name += 'o'
                elif event.key == pygame.K_p:
                    name += 'p'
                elif event.key == pygame.K_a:
                    name += 'a'
                elif event.key == pygame.K_s:
                    name += 's'
                elif event.key == pygame.K_d:
                    name += 'd'
                elif event.key == pygame.K_f:
                    name += 'f'
                elif event.key == pygame.K_g:
                    name += 'g'
                elif event.key == pygame.K_h:
                    name += 'h'
                elif event.key == pygame.K_j:
                    name += 'j'
                elif event.key == pygame.K_k:
                    name += 'k'
                elif event.key == pygame.K_l:
                    name += 'l'
                elif event.key == pygame.K_z:
                    name += 'z'
                elif event.key == pygame.K_x:
                    name += 'x'
                elif event.key == pygame.K_c:
                    name += 'c'
                elif event.key == pygame.K_v:
                    name += 'v'
                elif event.key == pygame.K_b:
                    name += 'b'
                elif event.key == pygame.K_n:
                    name += 'n'
                elif event.key == pygame.K_m:
                    name += 'm'
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN and bool(name):
                    save_result(name, cur_time)
                    return

        screen.fill((0, 0, 0))
        text = [f"{win} игрок выйграл",
                f"Время игры {cur_time}",
                f"Для сохранения результата",
                f"введите своё имя: {name}"]
        font = pygame.font.Font(None, 50)
        text_coord = 50
        for line in text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        clock.tick(60)


def save_result(name, score):
    with open('players.csv', mode='a', newline='', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=';', quotechar='"')
        writer.writerow([name, score])


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шашки')
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    board = Board(8, 8)
    board.set_view(100, 100, 50)
    curent_player = 0
    players = ['красный', 'синий']
    colors = ['red', 'blue']
    font = pygame.font.Font(None, 40)
    running = True
    on_click = False
    red = 0
    blue = 0
    time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    cur_time = 0
    win = -1
    start_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not on_click:
                    board.get_click(event.pos)
                elif on_click:
                    board.get_click(event.pos)
        for i in range(0, 8):
            for j in range(0, 8):
                if board.board[i][j] == 1 or board.board[i][j] == 3 or board.board[i][j] == 5 or board.board[i][j] == 7:
                    red = 1
                elif board.board[i][j] == 2 or board.board[i][j] == 4 or board.board[i][j] == 6 or board.board[i][j] == 8:
                    blue = 1
                if i == 7 and j == 7:
                    if red == 0:
                        win = 0
                        running = False
                    elif blue == 0:
                        win = 1
                        running = False
        red = 0
        blue = 0
        cur_time += time
        screen.fill((0, 0, 0))
        board.render(screen)
        string_rend = font.render(f'Ходит {players[curent_player]}', 1, pygame.Color(colors[curent_player]))
        screen.blit(string_rend, (200, 50))
        string_rend = font.render(f"Время - {(cur_time // 15000) // 60}:{(cur_time // 15000) % 60}", 1, pygame.Color('white'))
        screen.blit(string_rend, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    if win == 0:
        game_over_screen(win, screen, cur_time)
    elif win == 1:
        game_over_screen(win, screen, cur_time)
    pygame.quit()