import requests


class Participant:
    def __init__(self, tag, day_1_battles, day_1_cards, day_2_battles, day_2_played, day_2_wins):
        self.tag = tag
        self.day_1_battles = day_1_battles
        self.day_1_cards = day_1_cards
        self.day_2_battles = day_2_battles
        self.day_2_played = day_2_played
        self.day_2_wins = day_2_wins


class Member:
    def __init__(self, tag, name, participants):
        self.tag = tag
        self.name = name
        self.participants = participants

    def win_rate(self):
        pass


class ServerManager:
    def __init__(self, tag):
        self.members = []
        # check is it player or clan tag
        # get clan info
        pass

    def request_clan_info(self, clan_tag):
        pass

    def request_clan_war_info(self, clan_tag):
        # request war log, iterate for each war, iterate for each participant and fill Participant object
        # put Participant object to related Member object
        pass

    def request_player_info(self, player_tag):
        pass


def main():
    tag = '2UJ2GJ'
    server_manager = ServerManager(tag)
    members = server_manager.members
    for member in members:
        print(member.name + " " + member.win_rate())


if __name__ == "__main__":
    main()
