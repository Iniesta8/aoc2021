#!/usr/bin/env python3

from heapq import heappush, heappop
from copy import deepcopy

costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

room_indices = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

chars = "ABCD"


#     -10123456789AB
#      #############
#   0  #...........#
#   1  ###B#C#B#D###
#   2    #A#D#C#A#
#        #########


def possible_next_states(top_row, rooms):
    possible_states = []

    room_size = len(rooms[0])

    # Outermost amphipod in a room moves to the top row
    for i in range(4):
        if all([c == chars[i] or c == '.' for c in rooms[i]]):
            continue

        # Find the index of the outermost amphipod
        for outer in range(room_size):
            if rooms[i][outer] != '.':
                break

        new_rooms = deepcopy(rooms)
        new_rooms[i][outer] = '.'
        amphipod = rooms[i][outer]

        # Value can be moved left or right in top row
        for direction in [-1, 1]:
            bound = -1 if direction == -1 else 11

            for j in range(room_indices[chars[i]], bound, direction):

                # Check if there is any other amphipod blocking the path
                if top_row[j] != '.':
                    break

                # Check if destination position is on the space immediately outside of any room
                if j in [2, 4, 6, 8]:
                    continue

                # Otherwise, amphipod can move to position j in top row
                new_top_row = deepcopy(top_row)
                new_top_row[j] = amphipod
                cost = (
                    outer + 1 + abs(room_indices[chars[i]] - j)) * costs[amphipod]
                possible_states.append((cost, new_top_row, new_rooms))

    # Amphipod from the top row moves into a room
    for i in range(11):
        if top_row[i] == '.':
            continue

        amphipod = top_row[i]
        target_idx = chars.index(amphipod)

        # Check that all the amphipods in the destination room are correct
        if not all([c == amphipod or c == '.' for c in rooms[target_idx]]):
            continue

        # Check if there is any other amphipod blocking the path to the room
        s = 1 if (room_indices[amphipod] - i) >= 0 else -1
        if any([top_row[j] != '.' for j in range(i + s, room_indices[top_row[i]] + s, s)]):
            continue

        # Find index of outermost amphipod (if any)
        for j in range(room_size):
            if rooms[target_idx][j] == amphipod:
                break
        else:
            j = room_size

        new_top_row = deepcopy(top_row)
        new_rooms = deepcopy(rooms)
        new_top_row[i] = '.'
        new_rooms[target_idx][j - 1] = amphipod

        cost = (abs(room_indices[amphipod] - i) + j) * costs[amphipod]
        possible_states.append((cost, new_top_row, new_rooms))

    return possible_states


def is_final_state(top_row, rooms):
    room_size = len(rooms[0])
    if any(rooms[i] != [chars[i]] * room_size for i in range(4)):
        return False

    if top_row != list("..........."):
        return False

    return True


def solve(initial_rooms):
    top_row = list("...........")

    pqueue = [(0, top_row, initial_rooms)]
    visited_states = set()

    while len(pqueue) > 0:
        energy, top_row, rooms = heappop(pqueue)

        state = "".join(top_row)
        for i in range(4):
            state += "".join(rooms[i])
        if state in visited_states:
            continue
        visited_states.add(state)

        if is_final_state(top_row, rooms):
            return energy

        new_states = possible_next_states(top_row, rooms)
        for new_cost, new_top_row, new_rooms in new_states:
            heappush(pqueue, (energy + new_cost, new_top_row, new_rooms))


if __name__ == "__main__":
    initial_rooms_p1 = [list("CD"), list("AD"), list("BB"), list("CA")]
    initial_rooms_p2 = [list("CDDD"), list("ACBD"), list("BBAB"), list("CACA")]

    print(f"part1: {solve(initial_rooms_p1)}")
    print(f"part2: {solve(initial_rooms_p2)}")
