#!/usr/bin/env python3
"""
Ultimate (Super) Tic-Tac-Toe - Pygame GUI Version
Uses the same backend logic as the CLI version, with a graphical interface.
"""

import sys
import pygame
import numpy as np

# ---------- Backend: Ultimate Tic-Tac-Toe logic (from CLI version) ----------
def winner_of_board(board3x3: np.ndarray) -> int:
    """Returns 1 if X wins, -1 if O wins, 2 if draw, 0 if ongoing."""
    assert board3x3.shape == (3, 3)
    lines = []
    lines.extend(board3x3.sum(axis=0))
    lines.extend(board3x3.sum(axis=1))
    lines.append(board3x3.trace())
    lines.append(np.fliplr(board3x3).trace())
    if 3 in lines:
        return 1
    if -3 in lines:
        return -1
    if not (board3x3 == 0).any():
        return 2
    return 0


class UltimateTicTacToe:
    def __init__(self):
        self.grid = np.zeros((3, 3, 3, 3), dtype=np.int8)
        self.meta = np.zeros((3, 3), dtype=np.int8)
        self.current = 1          # 1 = X, -1 = O
        self.next_sub = None      # (bi, bj) or None for free move
        self.game_over = False
        self.meta_winner = 0

    @staticmethod
    def _to_symbol(v: int) -> str:
        return 'X' if v == 1 else ('O' if v == -1 else '.')

    def _subgrid(self, bi, bj) -> np.ndarray:
        return self.grid[bi, bj]

    def _subgrid_full_or_closed(self, bi, bj) -> bool:
        st = self.meta[bi, bj]
        if st != 0:
            return True
        sg = self._subgrid(bi, bj)
        return not (sg == 0).any()

    def legal_moves(self):
        moves = []
        def collect(bi, bj):
            if self.meta[bi, bj] != 0:
                return
            sg = self._subgrid(bi, bj)
            empties = np.argwhere(sg == 0)
            for ci, cj in empties:
                moves.append((bi, bj, ci, cj))

        if self.game_over:
            return moves

        if self.next_sub is not None:
            bi, bj = self.next_sub
            if not self._subgrid_full_or_closed(bi, bj):
                collect(bi, bj)
                return moves

        for bi in range(3):
            for bj in range(3):
                collect(bi, bj)
        return moves

    def _update_sub_status(self, bi, bj):
        self.meta[bi, bj] = winner_of_board(self._subgrid(bi, bj))

    def _update_meta_status(self):
        meta_for_win = self.meta.copy()
        meta_for_win = np.where(meta_for_win == 2, 0, meta_for_win)
        winner = winner_of_board(meta_for_win)
        if winner in (1, -1):
            self.meta_winner = winner
            self.game_over = True
            return
        if not (self.meta == 0).any():
            self.meta_winner = 2
            self.game_over = True
        else:
            self.meta_winner = 0
            self.game_over = False

    def make_move(self, bi, bj, ci, cj) -> bool:
        if self.game_over:
            return False
        if (bi, bj, ci, cj) not in self.legal_moves():
            return False
        if self.grid[bi, bj, ci, cj] != 0:
            return False

        self.grid[bi, bj, ci, cj] = self.current
        self._update_sub_status(bi, bj)
        self._update_meta_status()

        self.next_sub = (ci, cj)
        if self._subgrid_full_or_closed(ci, cj):
            self.next_sub = None

        if not self.game_over:
            self.current *= -1
        return True

    def get_cell(self, bi, bj, ci, cj):
        """Return 1 for X, -1 for O, 0 empty."""
        return self.grid[bi, bj, ci, cj]


# ---------- Pygame GUI ----------
# Constants
WINDOW_SIZE = 720          # 720x720 pixels
SUB_SIZE = WINDOW_SIZE // 3   # 240
CELL_SIZE = SUB_SIZE // 3     # 80
LINE_WIDTH_THIN = 2
LINE_WIDTH_THICK = 6

# Colors
BG_COLOR = (30, 30, 40)
LINE_COLOR = (200, 200, 200)
THICK_LINE_COLOR = (255, 255, 255)
X_COLOR = (100, 200, 255)
O_COLOR = (255, 180, 100)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (80, 80, 120)

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")
font = pygame.font.SysFont("Arial", CELL_SIZE // 2, bold=True)
small_font = pygame.font.SysFont("Arial", 24)

def draw_board(game, highlight_sub=None):
    """Draw the full 9x9 grid with sub-board borders."""
    screen.fill(BG_COLOR)

    # Draw thin cell lines
    for i in range(1, 9):
        pos = i * CELL_SIZE
        # vertical
        pygame.draw.line(screen, LINE_COLOR, (pos, 0), (pos, WINDOW_SIZE), LINE_WIDTH_THIN)
        # horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, pos), (WINDOW_SIZE, pos), LINE_WIDTH_THIN)

    # Draw thick sub-board borders
    for i in range(1, 3):
        pos = i * SUB_SIZE
        pygame.draw.line(screen, THICK_LINE_COLOR, (pos, 0), (pos, WINDOW_SIZE), LINE_WIDTH_THICK)
        pygame.draw.line(screen, THICK_LINE_COLOR, (0, pos), (WINDOW_SIZE, pos), LINE_WIDTH_THICK)

    # Highlight target sub-board if any
    if highlight_sub is not None and not game.game_over:
        bi, bj = highlight_sub
        rect = pygame.Rect(bj * SUB_SIZE, bi * SUB_SIZE, SUB_SIZE, SUB_SIZE)
        s = pygame.Surface((SUB_SIZE, SUB_SIZE), pygame.SRCALPHA)
        s.fill((255, 255, 100, 50))   # semi-transparent yellow
        screen.blit(s, rect)

    # Draw X and O marks
    for bi in range(3):
        for bj in range(3):
            for ci in range(3):
                for cj in range(3):
                    val = game.get_cell(bi, bj, ci, cj)
                    if val == 0:
                        continue
                    x = bj * SUB_SIZE + cj * CELL_SIZE + CELL_SIZE // 2
                    y = bi * SUB_SIZE + ci * CELL_SIZE + CELL_SIZE // 2
                    if val == 1:   # X
                        # Draw two lines
                        offset = CELL_SIZE // 3
                        pygame.draw.line(screen, X_COLOR, (x - offset, y - offset), (x + offset, y + offset), 6)
                        pygame.draw.line(screen, X_COLOR, (x + offset, y - offset), (x - offset, y + offset), 6)
                    else:          # O
                        pygame.draw.circle(screen, O_COLOR, (x, y), CELL_SIZE // 3, 6)

    # Draw status text
    status = []
    if game.game_over:
        if game.meta_winner == 1:
            status.append("X wins the meta board!")
        elif game.meta_winner == -1:
            status.append("O wins the meta board!")
        else:
            status.append("Draw!")
    else:
        turn = "X" if game.current == 1 else "O"
        status.append(f"Turn: {turn}")
        if game.next_sub:
            bi, bj = game.next_sub
            status.append(f"Play in sub-board: ({bi+1},{bj+1})")
        else:
            status.append("Play in any open sub-board")
    text_surface = small_font.render(" | ".join(status), True, TEXT_COLOR)
    screen.blit(text_surface, (10, WINDOW_SIZE - 30))

def get_cell_from_pos(pos):
    """Convert mouse pixel position to (big_r, big_c, cell_r, cell_c) or None if outside."""
    x, y = pos
    if x < 0 or x >= WINDOW_SIZE or y < 0 or y >= WINDOW_SIZE:
        return None
    big_c = x // SUB_SIZE
    big_r = y // SUB_SIZE
    cell_c = (x % SUB_SIZE) // CELL_SIZE
    cell_r = (y % SUB_SIZE) // CELL_SIZE
    return (big_r, big_c, cell_r, cell_c)

def main():
    game = UltimateTicTacToe()
    clock = pygame.time.Clock()
    running = True

    while running:
        draw_board(game, highlight_sub=game.next_sub)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                pos = pygame.mouse.get_pos()
                move = get_cell_from_pos(pos)
                if move is not None:
                    bi, bj, ci, cj = move
                    if game.make_move(bi, bj, ci, cj):
                        # move accepted
                        pass
                    else:
                        # illegal move: flash red or just ignore
                        pass

        # If game over, show final board and wait for key or quit
        if game.game_over:
            draw_board(game, highlight_sub=None)
            # Show game over message
            if game.meta_winner == 1:
                msg = "X wins! Press any key to quit."
            elif game.meta_winner == -1:
                msg = "O wins! Press any key to quit."
            else:
                msg = "Draw! Press any key to quit."
            text = small_font.render(msg, True, TEXT_COLOR)
            screen.blit(text, (WINDOW_SIZE//2 - text.get_width()//2, WINDOW_SIZE//2))
            pygame.display.flip()
            # Wait for keypress or quit
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False
                        running = False
            break

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
