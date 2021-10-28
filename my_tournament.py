import sys


class Tournament:
    def __init__(self, file_name):
        self.file_name = file_name
        self.games = []
        self.players = []
        self.player_scores = []

    def read_results(self, file_name):
        with open(file_name) as file:
            rows = 0
            columns = 0
            for line in file:
                if rows == 0:
                    games = line.strip().split()[1:]
                    for game in games:
                        self.games.append(Game(game))
                else:
                    player = line.strip().split()[:1]
                    player_scores = line.strip().split()[1:]
                    player_x = Player(player)
                    for score in player_scores:
                        score = self.get_score_value(int(score))
                        player_x.update_scores(score)
                        game_x = self.games[columns]
                        game_x.update_scores(score)
                        columns += 1
                    columns = 0
                    self.players.append(player_x)
                rows += 1

    def display_results(self):
        for player in self.players:
            self.player_scores.append(player.get_scores())
        no_players = len(self.player_scores)
        no_games = len(self.player_scores[0])
        print()
        print("     ", end="")
        for n in range(no_games):
            print(" | ", end=" ")
            print(self.games[n].game_id, end="")
        print()
        print("------", end="")
        for n in range(no_games):
            print("|------", end="")
        print()
        for m in range(no_players):
            print(self.players[m].player_id[0], end=" ")
            for score in self.players[m].get_scores():
                print(" | ", end=" ")
                print(score, end="  ")
            print()
        print("------", end="")
        for n in range(no_games):
            print("|------", end="")
        print()
        print(f"There are {no_players} players and {no_games} games")
        total_scores = [m.count(1) for m in self.player_scores]
        total_loses = [m.count("--") for m in self.player_scores]
        max_value = max(total_scores)
        max_index = total_scores.index(max_value)
        print(f"The top player is {self.players[max_index].player_id[0]} with {total_loses[max_index]} loses.")

    @staticmethod
    def get_score_value(raw_score):
        if raw_score == -1:
            return " "

        elif raw_score == 503:
            return "--"

        else:
            return raw_score


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.scores = []

    def update_scores(self, score):
        self.scores.append(score)

    def get_scores(self):
        return self.scores


class Game:
    def __init__(self, game_id):
        self.game_id = game_id
        self.scores = []

    def update_scores(self, score):
        self.scores.append(score)

    def get_scores(self):
        return self.scores


def main():
    try:
        file_name = sys.argv[1]
        tournament = Tournament(file_name)
        tournament.read_results(file_name)
        tournament.display_results()
    except IndexError:
        raise SystemExit(f"[Usage:] {sys.argv[0]} <results file>")


if __name__ == "__main__":
    main()
