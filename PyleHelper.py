import resources
import pygame
import os

class Scene():
    def __init__(self, columns, rows):
        self.cols = columns
        self.rows = rows
        self.grid = []
        for row in range(self.rows):
            self.grid.append(self.add_row(self.cols))

    def edit_tile(self, column, row, item):
        self.grid[row][column] = item

    def add_row(self, size):
        row = []
        for space in range(size):
            row.append("X")
        return row

    def save(self):
        fname = input("File name: ")
        file = open(fname + ".txt", 'w')

        for row in self.grid:
            line = ""

            for char in row:
                line += char

            file.write(line + "\n")

        file.close()

    def clear(self):
        for row in range(len(self.grid)):
            for item in range(len(self.grid[row])):
                self.grid[row][item] = "X"

class Sidebar():
    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        
        self.sbutton = "Save"
        self.ibutton = "Import"
        self.ebutton = "Exit"
        
        self.textbuttons1 = [self.ebutton, self.ibutton, self.sbutton]

        self.save = resources.AllSprites["SmallActiveMenu.png"]
        self.imp = resources.AllSprites["SmallMenu.png"]
        self.exit = resources.AllSprites["SmallMenu.png"]
        
        self.buttons1 = [self.exit, self.imp, self.save]

        self.cbutton = "Clear"
        self.embutton = "Empty"
        self.embutton2 = "Empty"

        self.textbuttons2 = [self.embutton2, self.embutton, self.cbutton]

        self.clear = resources.AllSprites["SmallMenu.png"]
        self.empty = resources.AllSprites["SmallMenu.png"]
        self.empty2 = resources.AllSprites["SmallMenu.png"]
        
        self.buttons2 = [self.empty2, self.empty, self.clear]

        self.menubarw = 170
        self.menubarh = 51

        self.bfontsize = 14
        self.bfont = pygame.font.Font(pygame.font.match_font('comicsansms'), self.bfontsize)

        self.previous = 2
        self.place = 2
        self.column = 0
        self.pcolumn = 0

        self.grid = []
        for column in range(10):
            self.grid.append([])
            for row in range(24):
                self.grid[column].append("X")

        for tile in resources.AllSprites.keys():
            self.fill_grid(tile)

    def fill_grid(self, tile):
        if ("block" in tile):
            for i in range(len(self.grid)):
                for n in range(len(self.grid[i])):
                    if (self.grid[i][n] == "X"):
                        self.grid[i][n] = tile
                        return

    def get_griditem(self, column, row):
        return self.grid[column][row]

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(166, 166, 166, 166), (resources.width, 0, self.width-resources.width, self.height))

        for button in range(len(self.buttons1)):
            self.screen.blit(self.buttons1[button], (resources.width, self.height -  self.menubarh * (button + 1)))
            self.screen.blit(self.bfont.render(self.textbuttons1[button], True, pygame.Color(255,255,255)), (resources.width + 5, 5 + self.height -  self.menubarh * (button + 1)))

        for button in range(len(self.buttons2)):
            self.screen.blit(self.buttons2[button], (resources.width + self.menubarw, self.height -  self.menubarh * (button + 1)))
            self.screen.blit(self.bfont.render(self.textbuttons2[button], True, pygame.Color(255,255,255)), (resources.width + 5 + self.menubarw, 5 + self.height -  self.menubarh * (button + 1)))

        for column in range(len(self.grid)):
            for row in range(len(self.grid[column])):
                if self.grid[column][row] != "X":
                    self.screen.blit(resources.AllSprites[self.grid[column][row]], (resources.width + (32 * column), 32 * row))

    def switch_button(self, direction):
        self.previous = self.place

        if direction == pygame.K_UP:
            self.pcolumn = self.column
            if self.place == len(self.buttons1) - 1:
                self.place = 0
            else:
                self.place += 1

        elif direction == pygame.K_DOWN:
            self.pcolumn = self.column
            if self.place == 0:
                self.place = len(self.buttons1) - 1
            else:
                self.place -= 1

        elif direction == pygame.K_LEFT:
            if self.column == 0:
                self.column = 1
                self.pcolumn = 0
            else:
                self.column = 0
                self.pcolumn = 1

        elif direction == pygame.K_RIGHT:
            if self.column == 0:
                self.column = 1
                self.pcolumn = 0
            else:
                self.column = 0
                self.pcolumn = 1
        
        if self.column != self.pcolumn:
            if self.column == 0:
                self.buttons1[self.place] = resources.AllSprites["SmallActiveMenu.png"]
                self.buttons2[self.place] = resources.AllSprites["SmallMenu.png"]
            else:
                self.buttons2[self.place] = resources.AllSprites["SmallActiveMenu.png"]
                self.buttons1[self.place] = resources.AllSprites["SmallMenu.png"]

        else:
            if self.column == 0:
                self.buttons1[self.place] = resources.AllSprites["SmallActiveMenu.png"]
                self.buttons1[self.previous] = resources.AllSprites["SmallMenu.png"]
            else:
                self.buttons2[self.place] = resources.AllSprites["SmallActiveMenu.png"]
                self.buttons2[self.previous] = resources.AllSprites["SmallMenu.png"]
