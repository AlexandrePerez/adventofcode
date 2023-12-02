answer = 0
max_color = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open('input.txt') as f:
    for line in f:
        game, draws = line.strip().split(':')
        game_id = int(game[4:])

        is_possible = True
        for draw in draws.split(';'):
            cubes = draw.split(',')
            for cube in cubes:
                nb, color = cube.strip().split(' ')
                if int(nb) > max_color[color]:
                    is_possible = False
        if is_possible:
            answer += game_id


print(answer)
