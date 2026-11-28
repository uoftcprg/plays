source plays.sh

declare -A games=(
	["d24"]="LiteEFG/LiteEFG/game_instances/D24.game"
	["kuhn"]="LiteEFG/LiteEFG/game_instances/kuhn.game"
	["leduc"]="LiteEFG/LiteEFG/game_instances/leduc.game"
	["liars-dice"]="LiteEFG/LiteEFG/game_instances/liars_dice.game"
)

for name in ${!games[@]}; do
	run lite-efg $name ${games[$name]} $games_path/lite-efg/$name.efg $games_path/lite-efg/$name.jsonl
done
