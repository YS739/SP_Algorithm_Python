# 2019년 상반기 LINE 인턴 채용 코딩테스트_나 잡아 봐라
from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    return


print(catch_me(c, b))  # 5가 나와야 합니다!


#020 카카오 신입 개발자 블라인드 채용 1차 코딩테스트_문자열 압축
input = "abcabcabcabcdededededede"


def string_compression(string):
    return


print(string_compression(input))  # 14 가 출력되어야 합니다!


#2020 카카오 신입 개발자 블라인드 채용 1차 코딩테스트 - 2_올바른 괄호 문자열 만들기
from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!



#삼성 역량 테스트 - 1_새로운 게임 2
k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    return


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다


#삼성 역량 테스트 - 2_구슬 탈출
from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]


def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    return


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다


#삼성 역량 테스트 - 3_치킨 배달
import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    return


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
