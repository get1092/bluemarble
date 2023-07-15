import random

class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.is_bankrupt = False
        self.owned_properties = []
        self.position = 0

class Spectator:
    def __init__(self, name):
        self.name = name

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
        self.buildings = 0

class GameRoom:
    def __init__(self, name, max_players, price, rent, special_price_range, special_rent_range):
        self.name = name
        self.max_players = max_players
        self.players = []
        self.spectators = []
        self.is_game_started = False
        self.current_player_index = 0
        self.properties = [

            # 첫 번째 줄
            Property("출발", 0, 0),
            Property("칸1", price, rent),
            Property("칸2", price, rent),
            Property("칸3", price, rent),
            Property("칸4", price, rent),
            Property("특별한 칸5", random.randint(*special_price_range), random.randint(*special_rent_range)),
            Property("칸6", price, rent),
            Property("칸7", price, rent),
            Property("칸8", price, rent),

            # 두 번째 줄
            Property("무인도", 0, 0),
            Property("칸9", price, rent),
            Property("칸10", price, rent),
            Property("칸11", price, rent),
            Property("칸12", price, rent),
            Property("특별한 칸13", random.randint(*special_price_range), random.randint(*special_rent_range)),
            Property("칸14", price, rent),
            Property("칸15", price, rent),
            Property("칸16", price, rent),
            Property("칸17", price, rent),

            # 세 번째 줄
            Property("사회복지기금", 0, 0),
            Property("칸18", price, rent),
            Property("칸19", price, rent),
            Property("칸20", price, rent),
            Property("칸21", price, rent),
            Property("특별한 칸22", random.randint(*special_price_range), random.randint(*special_rent_range)),
            Property("칸23", price, rent),
            Property("칸24", price, rent),
            Property("칸25", price, rent),

            # 네 번째 줄
            Property("우주여행", 0, 0),
            Property("칸26", price, rent),
            Property("칸27", price, rent),
            Property("칸28", price, rent),
            Property("칸29", price, rent),
            Property("특별한 칸30", random.randint(*special_price_range), random.randint(*special_rent_range)),
            Property("칸31", price, rent),
            Property("칸32", price, rent),
            Property("칸33", price, rent),
            Property("칸34", price, rent),
            Property("칸35", price, rent)
        ]

 

    def perform_special_action(self, player, property):
        # 특별한 칸에 도착했을 때 수행할 동작을 구현합니다.
        if property.name == "특별한 칸5":
            print("칸 5: 특별한 동작 수행")
            amount = random.randint(100000, 1000000)  # 10만원부터 100만원까지 랜덤한 금액을 얻습니다.
            if amount >= 0:
                player.points += amount
                print(f"{player.name}님이 {amount}원을 얻었습니다.")
            else:
                if player.points >= abs(amount):
                    player.points += amount
                    print(f"{player.name}님이 {abs(amount)}원을 잃었습니다.")
                else:
                    player.is_bankrupt = True
                    print(f"{player.name}님이 파산했습니다.")
        elif property.name == "특별한 칸13":
            print("칸 13: 특별한 동작 수행")
            amount = random.randint(100000, 1000000)  # 10만원부터 100만원까지 랜덤한 금액을 얻습니다.
            if amount >= 0:
                player.points += amount
                print(f"{player.name}님이 {amount}원을 얻었습니다.")
            else:
                if player.points >= abs(amount):
                    player.points += amount
                    print(f"{player.name}님이 {abs(amount)}원을 잃었습니다.")
                else:
                    player.is_bankrupt = True
                    print(f"{player.name}님이 파산했습니다.")
        elif property.name == "특별한 칸21":
            print("칸 21: 특별한 동작 수행")
            amount = random.randint(100000, 1000000)  # 10만원부터 100만원까지 랜덤한 금액을 얻습니다.
            if amount >= 0:
                player.points += amount
                print(f"{player.name}님이 {amount}원을 얻었습니다.")
            else:
                if player.points >= abs(amount):
                    player.points += amount
                    print(f"{player.name}님이 {abs(amount)}원을 잃었습니다.")
                else:
                    player.is_bankrupt = True
                    print(f"{player.name}님이 파산했습니다.")
        elif property.name == "특별한 칸29":
            print("칸 29: 특별한 동작 수행")
            amount = random.randint(100000, 1000000)  # 10만원부터 100만원까지 랜덤한 금액을 얻습니다.
            if amount >= 0:
                player.points += amount
                print(f"{player.name}님이 {amount}원을 얻었습니다.")
            else:
                if player.points >= abs(amount):
                    player.points += amount
                    print(f"{player.name}님이 {abs(amount)}원을 잃었습니다.")
                else:
                    player.is_bankrupt = True
                    print(f"{player.name}님이 파산했습니다.")


    def add_player(self, player):
        if len(self.players) < self.max_players:
            self.players.append(player)
        else:
            print("이미 최대 참가 인원에 도달했습니다.")

    def add_spectator(self, spectator):
        self.spectators.append(spectator)

    def remove_spectator(self, spectator):
        self.spectators.remove(spectator)

    def start_game(self):
        if len(self.players) < 2:
            print("플레이어가 부족하여 게임을 시작할 수 없습니다.")
            return

        self.is_game_started = True
        print("게임을 시작합니다!")

        # 게임 턴 진행
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            print(f"\n=== {current_player.name}의 차례 ===")
            self.play_turn(current_player)
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def is_game_over(self):
        active_players = [player for player in self.players if not player.is_bankrupt]
        return len(active_players) <= 1

    def play_turn(self, current_player):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total_dice = dice1 + dice2

        print(f"{current_player.name}님이 주사위를 던졌습니다. ({dice1}, {dice2})")
        print(f"{current_player.name}님이 {total_dice}만큼 이동합니다.")

        current_player.position = (current_player.position + total_dice) % len(self.properties)
        current_property = self.properties[current_player.position]

        if current_property.name == "출발":
            # 출발 칸에 도착한 경우, 10만원을 받음
            current_player.points += 100000
            print(f"{current_player.name}님이 출발 칸에 도착하여 10만원을 받았습니다.")

        elif current_property.name.startswith("특별한 칸"):
            # 특별한 칸에 도착한 경우, 특별한 동작 수행
            print(f"{current_player.name}님이 특별한 칸에 도착하였습니다.")
            self.perform_special_action(current_player, current_property)

        elif isinstance(current_property, Property):
            if current_property.owner is None:
                # 아무도 소유하지 않은 땅인 경우, 구매 여부 결정
                print(f"{current_property.name} 칸은 소유되지 않았습니다.")
                choice = input("구매하시겠습니까? (y/n): ")
                if choice.lower() == "y":
                    self.buy_property(current_player, current_property)

            else:
                if current_property.owner == current_player:
                    # 소유한 땅에 도착한 경우, 건물 구매 결정
                    print(f"{current_property.name} 칸은 {current_player.name}님의 소유입니다.")
                    choice = input("건물을 구매하시겠습니까? (y/n): ")
                    if choice.lower() == "y":
                        self.buy_building(current_player, current_property)
                else:
                    # 다른 플레이어가 소유한 땅에 도착한 경우, 통행료 지불
                    rent = self.calculate_rent(current_property)
                    self.pay_rent(current_player, current_property.owner, rent)
                if current_property.name.startswith("특별한 칸"):
                    current_property.perform_special_action(current_player)

        if dice1 == dice2:
            print(f"{current_player.name}님이 주사위 눈금이 같아 한 번 더 이동합니다.")
            self.play_turn(current_player)

    def buy_property(self, player, property):
        if player.points >= property.price:
            player.points -= property.price
            property.owner = player
            player.owned_properties.append(property)
            print(f"{player.name}님이 {property.name} 칸을 {property.price}원에 구매했습니다.")
        else:
            print(f"{player.name}님의 돈이 부족하여 {property.name} 칸을 구매할 수 없습니다.")

    def calculate_rent(self, property):
        if property.buildings == 0:
            return property.rent
        elif property.buildings <= 3:
            return property.rent * property.buildings
        else:
            return property.rent * 4

    def pay_rent(self, payer, landlord, amount):
        if payer.points >= amount:
            payer.points -= amount
            landlord.points += amount
            print(f"{payer.name}님이 {landlord.name}님에게 통행료 {amount}원을 지불했습니다.")
        else:
            print(f"{payer.name}님의 돈이 부족하여 통행료를 지불할 수 없습니다.")

    def perform_special_action(self, player, property):
        # 특별한 칸에 도착했을 때 수행할 동작을 구현합니다.
        if property.name == "특별한 칸5":
            print("칸 5: 특별한 동작 수행")
        elif property.name == "특별한 칸13":
            print("칸 13: 특별한 동작 수행")
        elif property.name == "특별한 칸21":
            print("칸 21: 특별한 동작 수행")
        elif property.name == "특별한 칸29":
            print("칸 29: 특별한 동작 수행")
        # ...

# 특별한 칸의 가격 범위와 임대료 범위 정의
special_price_range = (100000, 1000000)
special_rent_range = (100000, 1000000)

# GameRoom 객체 생성 시 특별한 칸의 가격 범위와 임대료 범위 전달
game = GameRoom("부루마블 게임", 4, 200, 50, special_price_range, special_rent_range)
game.add_player(Player("게임오리1", 10000))
game.add_player(Player("게임오리2", 10000))
game.add_player(Player("게임오리3", 10000))
game.add_player(Player("게임오리4", 10000))
game.add_spectator(Spectator("구경오리1"))
game.add_spectator(Spectator("구경오리2"))
game.add_spectator(Spectator("구경오리3"))
game.add_spectator(Spectator("구경오리4"))
# 게임 시작
game.start_game()
