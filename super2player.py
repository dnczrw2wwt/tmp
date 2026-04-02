#!/usr/bin/env python3
# Ultimate (Super) Tic-Tac-Toe in Python + NumPy
# CLI, two players (X and O). Indices are 1..3 for both big and small boards.

import sys
import numpy as np

# Cell values: 1 = X, -1 = O, 0 = empty
# Meta values: 1 = X won, -1 = O won, 2 = draw/closed, 0 = ongoing

def winner_of_board(board3x3: np.ndarray) -> int:
    """
    Returns 1 if X wins, -1 if O wins, 2 if draw (full, no win), 0 if ongoing.
    board3x3: shape (3,3) with values in {-1,0,1}
    """
    assert board3x3.shape == (3, 3)
    # Check lines via sums
    lines = []
    lines.extend(board3x3.sum(axis=0))     # columns
    lines.extend(board3x3.sum(axis=1))     # rows
    lines.append(board3x3.trace())         # main diagonal
    lines.append(np.fliplr(board3x3).trace())  # anti-diagonal
    if 3 in lines:
        return 1
    if -3 in lines:
        return -1
    if not (board3x3 == 0).any():
        return 2  # draw/closed
    return 0  # ongoing


class UltimateTicTacToe:
    def __init__(self):
        # Full grid as (big_row, big_col, cell_row, cell_col)
        self.grid = np.zeros((3, 3, 3, 3), dtype=np.int8)
        self.meta = np.zeros((3, 3), dtype=np.int8)  # status of each small board
        self.current = 1  # X starts
        self.next_sub = None  # (bi, bj) or None for free move
        self.game_over = False
        self.meta_winner = 0  # 1, -1, 2(draw), 0 ongoing

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
        """Return list of legal moves as tuples (bi,bj,ci,cj) in 0-based indices."""
        moves = []
        def collect_moves_for_sub(bi, bj):
            if self.meta[bi, bj] != 0:
                return
            sg = self._subgrid(bi, bj)
            empties = np.argwhere(sg == 0)
            for ci, cj in empties:   # ci, cj are already integers
                moves.append((bi, bj, ci, cj))

        if self.game_over:
            return moves

        if self.next_sub is not None:
            bi, bj = self.next_sub
            if not self._subgrid_full_or_closed(bi, bj):
                collect_moves_for_sub(bi, bj)
                return moves
            # target is closed/full -> free move

        # Free to play in any open sub-board
        for bi in range(3):
            for bj in range(3):
                collect_moves_for_sub(bi, bj)
        return moves

    def _update_sub_status(self, bi, bj):
        sg = self._subgrid(bi, bj)
        self.meta[bi, bj] = winner_of_board(sg)

    def _update_meta_status(self):
        # Meta winner ignores 2 (draw/closed) as 0 for line detection
        meta_for_win = self.meta.copy()
        meta_for_win = np.where(meta_for_win == 2, 0, meta_for_win)

        # Compute winner on the meta grid by treating draws as 0
        winner = winner_of_board(meta_for_win)
        if winner in (1, -1):
            self.meta_winner = winner
            self.game_over = True
            return

        # Full meta (no open subboards) -> overall draw
        if not (self.meta == 0).any():
            self.meta_winner = 2
            self.game_over = True
        else:
            self.meta_winner = 0
            self.game_over = False

    def make_move(self, bi, bj, ci, cj) -> bool:
        """
        bi,bj,ci,cj are 0-based. Returns True if move accepted, else False.
        """
        if self.game_over:
            return False

        # Check legality
        legal = self.legal_moves()
        if (bi, bj, ci, cj) not in legal:
            return False

        # Apply move
        if self.grid[bi, bj, ci, cj] != 0:
            return False
        self.grid[bi, bj, ci, cj] = self.current

        # Update sub-board status and meta-board
        self._update_sub_status(bi, bj)
        self._update_meta_status()

        # Determine next target sub-board (based on cell just played)
        self.next_sub = (ci, cj)
        if self._subgrid_full_or_closed(ci, cj):
            self.next_sub = None  # free move next turn

        # Swap player if game not over
        if not self.game_over:
            self.current *= -1
        return True

    def meta_status_string(self):
        if self.meta_winner == 1:
            return "X wins the meta board!"
        if self.meta_winner == -1:
            return "O wins the meta board!"
        if self.meta_winner == 2:
            return "Draw (meta board closed)!"
        return "Game ongoing."

    def render(self) -> str:
        """Pretty string of the whole 9x9 board with thick borders between sub-boards."""
        rows = []
        hdr = []
        if self.next_sub is not None:
            bi, bj = self.next_sub
            hdr.append(f"Target sub-board: ({bi+1},{bj+1})")
        else:
            hdr.append("Target sub-board: any open board")

        hdr.append(f"Turn: {'X' if self.current == 1 else 'O'}")
        rows.extend(hdr)

        # Build 9 visible rows, grouping every 3 with a thick border
        for big_r in range(3):
            for cell_r in range(3):
                line_cells = []
                for big_c in range(3):
                    sg = self._subgrid(big_r, big_c)
                    three = ''.join(self._to_symbol(v) for v in sg[cell_r])
                    line_cells.append(three)
                rows.append(' || '.join(line_cells))
            if big_r < 2:
                rows.append('=================')  # 17 '=' matches row width
        rows.append(self.meta_status_string())
        return '\n'.join(rows)

    def print_meta_grid(self):
        # For debugging: show meta board statuses
        def m(v):
            return {1: 'X', -1: 'O', 2: '#', 0: '.'}[int(v)]
        meta_str = '\n'.join(' '.join(m(x) for x in row) for row in self.meta)
        print("Meta (X/O won, # closed, . open):")
        print(meta_str)


def parse_move(s: str):
    """
    Parse user input "bi bj ci cj" with indices 1..3.
    Returns 0-based tuple (bi,bj,ci,cj) or None on failure.
    """
    parts = s.strip().split()
    if len(parts) != 4:
        return None
    try:
        bi, bj, ci, cj = (int(x) for x in parts)
    except ValueError:
        return None
    for v in (bi, bj, ci, cj):
        if v < 1 or v > 3:
            return None
    return (bi-1, bj-1, ci-1, cj-1)


def print_help():
    print(
        "\nCommands:\n"
        "  move:        bi bj ci cj   (each 1..3). Example: 2 1 3 2\n"
        "  m / moves:   list all legal moves\n"
        "  h / help:    show this help\n"
        "  q / quit:    quit the game\n"
        "\nRules summary:\n"
        " - You play on a 3x3 grid of 3x3 boards.\n"
        " - Your move sends your opponent to the sub-board that matches the cell you just played.\n"
        " - If that target sub-board is already won or full, your opponent may play in any open sub-board.\n"
        " - Win by taking 3 sub-boards in a row on the meta board.\n"
    )


def main():
    game = UltimateTicTacToe()
    print("Ultimate (Super) Tic-Tac-Toe — NumPy Edition")
    print_help()
    print()
    print(game.render())

    while not game.game_over:
        prompt = f"[{'X' if game.current==1 else 'O'}] Enter move (bi bj ci cj) or 'm'/'h'/'q': "
        try:
            s = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return

        if s.lower() in ('q', 'quit', 'exit'):
            print("Goodbye!")
            return
        if s.lower() in ('h', 'help', '?'):
            print_help()
            continue
        if s.lower() in ('m', 'moves'):
            moves = game.legal_moves()
            if not moves:
                print("No legal moves.")
            else:
                pretty = ', '.join(f"({bi+1}{bj+1}|{ci+1}{cj+1})"
                                   for (bi, bj, ci, cj) in moves)
                # format (BigRowBigCol|CellRowCellCol) with 1-based indices
                print(f"Legal moves: {pretty}")
            continue

        mv = parse_move(s)
        if mv is None:
            print("Could not parse move. Use four numbers 1..3, e.g. '2 1 3 2'.")
            continue

        ok = game.make_move(*mv)
        if not ok:
            print("Illegal move for the current position. Type 'm' to list legal moves.")
            continue

        print()
        print(game.render())
        print()

    # Game over
    if game.meta_winner == 1:
        print("🎉 X wins!")
    elif game.meta_winner == -1:
        print("🎉 O wins!")
    else:
        print("🤝 Draw!")


if __name__ == "__main__":
    main()
