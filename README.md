# The Lost Kingdom 2 — ET 2100 Assignment 10

A terminal RPG with 14 meaningful Python modules, TinyDB save files, colored output, quests, five NPCs, five regular monster types plus a boss, two maps, and monster/skill inheritance.

## Playthrough guide

- Register with R, then use `map` and W/A/S/D to walk. NPCs are marked N. Stand next to them and type `talk`.
- Village NPCs: Elder (3,4), Merchant (10,2), Healer (6,6). Talk to Elder to begin the main quest.
- `travel` switches between village and forest. `explore` starts a random fight in forest (so you don't need to wait for encounters).
- Defeat two Goblins; return to Elder. Go to forest and talk to Sage (6,6). You receive a Sun Crystal.
- Side quests: talk to Healer and bring 3 Herbs; talk to Ranger (9,2) and defeat 2 Wolves. Return to each NPC for rewards.
- Gain XP to level up; `learn` Heal at level 2 and Fireball at level 3. Use `skills` to see energy/cooldowns.
- Use `rest` in the village to restore HP and energy. Buy supplies by talking to Merchant. Equipment bonuses work automatically.
- Once you have the crystal and the main quest is on its final step, type `boss` in forest to fight the Shadow King. Defeat him to win.
- `save` saves manually; every completed command also autosaves. `quit` saves and exits. Login again with L to resume.

## Files

- `main.py`: program entry
- `auth.py`: registration and login
- `database.py`: TinyDB account/save persistence
- `player.py`: player stats and level progression
- `game.py`: command loop and game flow
- `map.py`: two maps, obstacles and NPC coordinates
- `monster.py`: monster inheritance and drops
- `skill.py`: skill inheritance and effects
- `combat.py`: turn-based battles
- `item.py`: item definitions
- `inventory.py`: item management
- `quest.py`: main/side quest state
- `npc.py`: NPC dialogue and interaction
- `shop.py`: item purchases

`pyproject.toml` and `saves.json` are generated locally by uv and TinyDB respectively. Do not commit `saves.json` to a public repository because it contains account records. Passwords are salted and hashed, but this is an educational demo, not production-grade authentication.

## GitHub / recording

Create your own GitHub repository, upload the source files (not `saves.json`), and submit the repository URL as instructed. Record a full playthrough from registration to boss victory. If a demo takes too long, use `explore` repeatedly and `rest` in the village; the game's level and quest requirements still apply.
