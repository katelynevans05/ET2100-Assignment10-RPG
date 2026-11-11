MAPS = {
 "village": [
  "###############",
  "#.....#.......#",
  "#.....#...N...#",
  "#.............#",
  "#..N....###...#",
  "#.............#",
  "#.....N.......#",
  "#.............#",
  "###############"],
 "forest": [
  "###################",
  "#....#............#",
  "#....#...N........#",
  "#...........###....#",
  "#..###............#",
  "#.................#",
  "#.....N.....###...#",
  "#.................#",
  "#...###...........#",
  "#.................#",
  "###################"]}
NPC_POSITIONS = {"village": {(3,4): "elder", (10,2): "merchant", (6,6): "healer"},
                 "forest": {(9,2): "ranger", (6,6): "sage"}}

def draw(player, color):
    for y, line in enumerate(MAPS[player.map_name]):
        out = ""
        for x, cell in enumerate(line):
            if (x, y) == (player.x, player.y):
                out += color.GREEN + "@" + color.RESET
            elif cell == "#":
                out += color.BLUE + "#" + color.RESET
            elif cell == "N":
                out += color.YELLOW + "N" + color.RESET
            else:
                out += cell
        print(out)
    print("@ = you | N = NPC | # = wall")

def move(player, direction):
    dx, dy = {"w": (0,-1), "a": (-1,0), "s": (0,1), "d": (1,0)}[direction]
    x, y = player.x + dx, player.y + dy
    if MAPS[player.map_name][y][x] == "#":
        print("A wall blocks your path.")
        return False
    player.x, player.y = x, y
    return True

def nearby_npc(player):
    for (x, y), npc in NPC_POSITIONS[player.map_name].items():
        if abs(x - player.x) + abs(y - player.y) <= 1:
            return npc
    return None
