answer = 0

with open('input.txt') as f:
    for line in f:
        game, draws = line.strip().split(':')
        game_id = int(game[4:])

        max_color = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for draw in draws.split(';'):
            cubes = draw.split(',')
            for cube in cubes:
                nb, color = cube.strip().split(' ')
                if int(nb) > max_color[color]:
                    max_color[color] = int(nb)
        answer += max_color['red'] * max_color['green'] * max_color['blue']

print(answer)
