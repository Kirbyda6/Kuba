from copy import deepcopy


class KubaGame:
    """
    This class represents a game called Kuba. The game is played by two players
    and the objective is to push 7 red marbles off the board before the other
    player
    """
    def __init__(self, player_1, player_2):
        """
        This method initializes the class with two players and will also
        initialize a board with red, white, and black marbles in their
        initial positions. Along with these, there will also be a player
        turn variable that will keep track of whose turn it is
        """
        self._players = {player_1[0]: player_1[1], player_2[0]: player_2[1]}
        self._players_storage = {player_1[0]: 0, player_2[0]: 0}
        self._board = [
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['G', 'W', 'W', 'X', 'X', 'X', 'B', 'B', 'G'],
            ['G', 'W', 'W', 'X', 'R', 'X', 'B', 'B', 'G'],
            ['G', 'X', 'X', 'R', 'R', 'R', 'X', 'X', 'G'],
            ['G', 'X', 'R', 'R', 'R', 'R', 'R', 'X', 'G'],
            ['G', 'X', 'X', 'R', 'R', 'R', 'X', 'X', 'G'],
            ['G', 'B', 'B', 'X', 'R', 'X', 'W', 'W', 'G'],
            ['G', 'B', 'B', 'X', 'X', 'X', 'W', 'W', 'G'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
            ]
        self._previous_boards = {
            player_1[0]: [
                ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                ['G', 'W', 'W', 'X', 'X', 'X', 'B', 'B', 'G'],
                ['G', 'W', 'W', 'X', 'R', 'X', 'B', 'B', 'G'],
                ['G', 'X', 'X', 'R', 'R', 'R', 'X', 'X', 'G'],
                ['G', 'X', 'R', 'R', 'R', 'R', 'R', 'X', 'G'],
                ['G', 'X', 'X', 'R', 'R', 'R', 'X', 'X', 'G'],
                ['G', 'B', 'B', 'X', 'R', 'X', 'W', 'W', 'G'],
                ['G', 'B', 'B', 'X', 'X', 'X', 'W', 'W', 'G'],
                ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
                ],
            player_2[0]: [
                ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
                ['G', 'W', 'W', 'X', 'X', 'X', 'B', 'B', 'G'],
                ['G', 'W', 'W', 'X', 'R', 'X', 'B', 'B', 'G'],
                ['G', 'X', 'X', 'R', 'R', 'R', 'X', 'X', 'G'],
                ['G', 'X', 'R', 'R', 'R', 'R', 'R', 'X', 'G'],
                ['G', 'X', 'X', 'R', 'R', 'R', 'X', 'X', 'G'],
                ['G', 'B', 'B', 'X', 'R', 'X', 'W', 'W', 'G'],
                ['G', 'B', 'B', 'X', 'X', 'X', 'W', 'W', 'G'],
                ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
                ]
            }
        self._turn = None
        self._winner = None

    def get_current_turn(self):
        """This method will return the player who's turn it is"""
        return self._turn

    def make_move(self, player, coord, direction):
        """
        This method takes, as parameters, the player's name, the position
        of the player's marble, and the direction of the desired move and
        then moves the marbles accordingly (if the move is valid)
        """
        players = [plyr for plyr in self._players.keys()]
        other_player = {players[0]: players[1], players[1]: players[0]}
        if self._winner is not None:
            return False
        if not 0 <= coord[0] <= 6 or not 0 <= coord[1] <= 6:
            return False
        if self._turn is None:
            self._turn = player
        if player != self._turn:
            return False
        if self._board[coord[0] + 1][coord[1] + 1] != self._players[player]:
            return False

        if direction == 'R':
            if self._board[coord[0] + 1][coord[1]] == 'X' or self._board[coord[0] + 1][coord[1]] == 'G':
                n = 1
                while self._board[coord[0] + 1][coord[1] + n] != 'X' and self._board[coord[0] + 1][coord[1] + n] != 'G':
                    n += 1
                for num in range(coord[1] + n, coord[1], -1):
                    if self._board[coord[0] + 1][num] == 'G':
                        if self._board[coord[0] + 1][num - 1] == 'R':
                            self._board[coord[0] + 1][num - 1] = 'X'
                            self._players_storage[player] += 1
                        elif self._board[coord[0] + 1][num - 1] == self._players[player]:
                            return False
                        else:
                            self._board[coord[0] + 1][num - 1] = 'X'
                    elif self._board[coord[0] + 1][num - 1] != 'G':
                        temp = self._board[coord[0] + 1][num]
                        self._board[coord[0] + 1][num] = self._board[coord[0] + 1][num - 1]
                        self._board[coord[0] + 1][num - 1] = temp
            else:
                return False

        if direction == 'L':
            if self._board[coord[0] + 1][coord[1] + 2] == 'X' or self._board[coord[0] + 1][coord[1] + 2] == 'G':
                n = 0
                while self._board[coord[0] + 1][coord[1] - n] != 'X' and self._board[coord[0] + 1][coord[1] - n] != 'G':
                    n += 1
                for num in range(coord[1] - n, coord[1] + 2):
                    if self._board[coord[0] + 1][num] == 'G':
                        if self._board[coord[0] + 1][num + 1] == 'R':
                            self._board[coord[0] + 1][num + 1] = 'X'
                            self._players_storage[player] += 1
                        elif self._board[coord[0] + 1][num + 1] == self._players[player]:
                            return False
                        else:
                            self._board[coord[0] + 1][num + 1] = 'X'
                    elif self._board[coord[0] + 1][num + 1] != 'G':
                        temp = self._board[coord[0] + 1][num]
                        self._board[coord[0] + 1][num] = self._board[coord[0] + 1][num + 1]
                        self._board[coord[0] + 1][num + 1] = temp
            else:
                return False

        if direction == 'F':
            if self._board[coord[0] + 2][coord[1] + 1] == 'X' or self._board[coord[0] + 2][coord[1] + 1] == 'G':
                n = 0
                while self._board[coord[0] - n][coord[1] + 1] != 'X' and self._board[coord[0] - n][coord[1] + 1] != 'G':
                    n += 1
                for num in range(coord[0] - n, coord[0] + 2):
                    if self._board[num][coord[1] + 1] == 'G':
                        if self._board[num + 1][coord[1] + 1] == 'R':
                            self._board[num + 1][coord[1] + 1] = 'X'
                            self._players_storage[player] += 1
                        elif self._board[num + 1][coord[1] + 1] == self._players[player]:
                            return False
                        else:
                            self._board[num + 1][coord[1] + 1] = 'X'
                    elif self._board[num + 1][coord[1] + 1] != 'G':
                        temp = self._board[num][coord[1] + 1]
                        self._board[num][coord[1] + 1] = self._board[num + 1][coord[1] + 1]
                        self._board[num + 1][coord[1] + 1] = temp
            else:
                return False

        if direction == 'B':
            if self._board[coord[0]][coord[1] + 1] == 'X' or self._board[coord[0]][coord[1] + 1] == 'G':
                n = 1
                while self._board[coord[0] + n][coord[1] + 1] != 'X' and self._board[coord[0] + n][coord[1] + 1] != 'G':
                    n += 1
                for num in range(coord[0] + n, coord[0], -1):
                    if self._board[num][coord[1] + 1] == 'G':
                        if self._board[num - 1][coord[1] + 1] == 'R':
                            self._board[num - 1][coord[1] + 1] = 'X'
                            self._players_storage[player] += 1
                        elif self._board[num - 1][coord[1] + 1] == self._players[player]:
                            return False
                        else:
                            self._board[num - 1][coord[1] + 1] = 'X'
                    elif self._board[num - 1][coord[1] + 1] != 'G':
                        temp = self._board[num][coord[1] + 1]
                        self._board[num][coord[1] + 1] = self._board[num - 1][coord[1] + 1]
                        self._board[num - 1][coord[1] + 1] = temp
            else:
                return False

        if self._board == self._previous_boards[player]:
            self._board = deepcopy(self._previous_boards[other_player[player]])
            return False
        else:
            self._previous_boards[player] = deepcopy(self._board)
        for num in self._players_storage.values():
            if num == 7:
                self._winner = player
        for name in self._players.keys():
            if name != player:
                self._turn = name
        return True

    def get_winner(self):
        """
        This method will return the winner of the game if there is one
        at this point
        """
        return self._winner

    def get_captured(self, player):
        """
        This method takes, as a parameter, the player's name and returns
        the numbers of red marbles that the player has moved off the board
        """
        return self._players_storage[player]

    def get_marble(self, coord):
        """
        This method takes, as a parameter, a coordinate of a space on the
        board. If there is a marble in this space, it will return the color
        of the marble. If there is no marble there, it will return 'X'
        """
        return self._board[coord[0] + 1][coord[1] + 1]

    def get_marble_count(self):
        """
        This method will return the number of marbles of each color there are
        remaining on the board. It will return these numbers as a tuple in the
        format (W,B,R)
        """
        marbles = {'W': 0, 'B': 0, 'R': 0}
        for sub_list in self._board:
            for element in sub_list:
                if element in marbles:
                    marbles[element] += 1
        return tuple([marbles['W'], marbles['B'], marbles['R']])

    def get_board(self):
        """
        Just a method to show the board when testing the program
        """
        return self._board


def main():
    game = KubaGame(('A', 'W'), ('B', 'B'))
    while game.get_winner() is None:
        print(game.get_board()[1][1:8])
        print(game.get_board()[2][1:8])
        print(game.get_board()[3][1:8])
        print(game.get_board()[4][1:8])
        print(game.get_board()[5][1:8])
        print(game.get_board()[6][1:8])
        print(game.get_board()[7][1:8])

        print("turn:" + str(game.get_current_turn()))
        if game.get_current_turn() is None:
            name = input("Name: ")
        else:
            name = game.get_current_turn()
        coord = [int(d) for d in input("Coordinate: ") if d.isdigit() is True]
        direction = input("Direction: ")

        print(game.get_marble(coord))
        game.make_move(name, coord, direction)
        print("winner:" + str(game.get_winner()))
        print("mar count:" + str(game.get_marble_count()))
        print("captured:" + str(game.get_captured(name)))


if __name__ == '__main__':
    main()
