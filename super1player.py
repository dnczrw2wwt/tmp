#!/usr/bin/env python3
# Ultimate (Super) Tic-Tac-Toe in Python + NumPy
# 1-player mode: human (X) vs computer (O)
# Computer uses heuristic: win, block, first-move strategy, else random.

import sys
import numpy as np
import random

# Cell values: 1 = X, -1 = O, 0 = empty
# Meta values: 1 = X won, -1 = O won, 2 = draw/closed, 0 = ongoing

def winner_of_board(board3x3: np.ndarray) -> int:
    """
    Returns 1 if X wins, -1 if O wins, 2 if draw (full, no win), 0 if ongoing.
    board3x3: shape (3,3) with values in {-1,0,1}
    """
    assert board3x3.shape == (3, 3)
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
        return 2
    return 0


class UltimateTicTacToe:
    def __init__(self):
        self.grid = np.zeros((3, 3, 3, 3), dtype=np.int8)
        self.meta = np.zeros((3, 3), dtype=np.int8)
        self.current = 1  # X starts (human)
        self.next_sub = None
        self.game_over = False
        self.meta_winner = 0
        # For computer AI: random seed for reproducibility
        random.seed(42)

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
        def collect_moves_for_sub(bi, bj):
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
                collect_moves_for_sub(bi, bj)
                return moves

        for bi in range(3):
            for bj in range(3):
                collect_moves_for_sub(bi, bj)
        return moves

    def _update_sub_status(self, bi, bj):
        sg = self._subgrid(bi, bj)
        self.meta[bi, bj] = winner_of_board(sg)

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
        legal = self.legal_moves()
        if (bi, bj, ci, cj) not in legal:
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

    def meta_status_string(self):
        if self.meta_winner == 1:
            return "X wins the meta board!"
        if self.meta_winner == -1:
            return "O wins the meta board!"
        if self.meta_winner == 2:
            return "Draw (meta board closed)!"
        return "Game ongoing."

    def render(self) -> str:
        rows = []
        hdr = []
        if self.next_sub is not None:
            bi, bj = self.next_sub
            hdr.append(f"Target sub-board: ({bi+1},{bj+1})")
        else:
            hdr.append("Target sub-board: any open board")
        hdr.append(f"Turn: {'X' if self.current == 1 else 'O'}")
        rows.extend(hdr)
        for big_r in range(3):
            for cell_r in range(3):
                line_cells = []
                for big_c in range(3):
                    sg = self._subgrid(big_r, big_c)
                    three = ''.join(self._to_symbol(v) for v in sg[cell_r])
                    line_cells.append(three)
                rows.append(' || '.join(line_cells))
            if big_r < 2:
                rows.append('=================')
        rows.append(self.meta_status_string())
        return '\n'.join(rows)

    # ------------------------------------------------------------------
    # Computer AI (plays as O = -1)
    # ------------------------------------------------------------------
    def _subboard_winning_move(self, board: np.ndarray, player: int) -> tuple or None:
        """Return (ci,cj) if player has a winning move on this 3x3 board, else None."""
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    board[i, j] = player
                    if winner_of_board(board) == player:
                        board[i, j] = 0
                        return (i, j)
                    board[i, j] = 0
        return None

    def _choose_move_in_subboard(self, bi, bj, computer= -1, human=1) -> tuple:
        """
        Given a specific sub-board (bi,bj) that is open,
        choose a cell (ci,cj) using heuristic:
        1. Win if possible
        2. Block human win
        3. First-move heuristic (center, corners)
        4. Random
        """
        board = self._subgrid(bi, bj).copy()
        # 1. Can computer win?
        move = self._subboard_winning_move(board, computer)
        if move:
            return move
        # 2. Block human win?
        move = self._subboard_winning_move(board, human)
        if move:
            return move
        # 3. Heuristic based on empty cells
        empty = list(zip(*np.where(board == 0)))
        # Prefer center
        if (1, 1) in empty:
            return (1, 1)
        # Prefer corners
        corners = [(0,0), (0,2), (2,0), (2,2)]
        for c in corners:
            if c in empty:
                return c
        # 4. Random
        return random.choice(empty)

    def computer_move(self):
        """Return a legal move (bi,bj,ci,cj) for computer (O)."""
        moves = self.legal_moves()
        if not moves:
            return None

        # If forced sub-board, choose within it
        if self.next_sub is not None:
            bi, bj = self.next_sub
            ci, cj = self._choose_move_in_subboard(bi, bj)
            return (bi, bj, ci, cj)

        # Free move: choose best sub-board and then best cell
        # First, collect all possible (bi,bj) that are open
        open_subs = [(bi, bj) for bi in range(3) for bj in range(3) if self.meta[bi, bj] == 0]
        # Priority: sub-boards where computer can win immediately
        for bi, bj in open_subs:
            board = self._subgrid(bi, bj)
            if self._subboard_winning_move(board, -1):  # computer = -1
                ci, cj = self._choose_move_in_subboard(bi, bj)
                return (bi, bj, ci, cj)
        # Next, sub-boards where human can win (block)
        for bi, bj in open_subs:
            board = self._subgrid(bi, bj)
            if self._subboard_winning_move(board, 1):  # human = 1
                ci, cj = self._choose_move_in_subboard(bi, bj)
                return (bi, bj, ci, cj)
        # Prefer center sub-board
        center_sub = (1, 1)
        if center_sub in open_subs:
            bi, bj = center_sub
            ci, cj = self._choose_move_in_subboard(bi, bj)
            return (bi, bj, ci, cj)
        # Prefer corner sub-boards
        corner_subs = [(0,0), (0,2), (2,0), (2,2)]
        for sub in corner_subs:
            if sub in open_subs:
                bi, bj = sub
                ci, cj = self._choose_move_in_subboard(bi, bj)
                return (bi, bj, ci, cj)
        # Any open sub-board
        bi, bj = random.choice(open_subs)
        ci, cj = self._choose_move_in_subboard(bi, bj)
        return (bi, bj, ci, cj)


def parse_move(s: str):
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
        " - You play as X, computer as O.\n"
        " - Your move sends computer to the sub-board that matches the cell you just played.\n"
        " - If that target sub-board is already won or full, computer may play in any open sub-board.\n"
        " - Win by taking 3 sub-boards in a row on the meta board.\n"
    )


def main():
    game = UltimateTicTacToe()
    print("Ultimate (Super) Tic-Tac-Toe — 1-player vs Computer")
    print_help()
    print()
    print(game.render())

    while not game.game_over:
        # Human turn (X)
        if game.current == 1:
            prompt = "[X] Enter move (bi bj ci cj) or 'm'/'h'/'q': "
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
        else:
            # Computer turn (O)
            print("\nComputer is thinking...")
            move = game.computer_move()
            if move is None:
                print("No legal moves for computer. Game might be stuck.")
                break
            bi, bj, ci, cj = move
            print(f"Computer plays: ({bi+1},{bj+1}) -> ({ci+1},{cj+1})")
            ok = game.make_move(bi, bj, ci, cj)
            if not ok:
                print("Computer attempted illegal move! Something is wrong.")
                break

        print()
        print(game.render())
        print()

    # Game over
    if game.meta_winner == 1:
        print("🎉 You win!")
    elif game.meta_winner == -1:
        print("🤖 Computer wins!")
    else:
        print("🤝 Draw!")


if __name__ == "__main__":
    main()
