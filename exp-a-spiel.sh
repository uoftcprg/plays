source plays.sh

declare -A games=(
	["abrupt-dark-hex-3"]="AbruptDh"
	["abrupt-phantom-tic-tac-toe"]="AbruptPttt"
	["corner-dark-hex-3"]="CornerDh"
	["dark-hex-3"]="Dh"
	["phantom-tic-tac-toe"]="Pttt"
)

for name in ${!games[@]}; do
	run exp-a-spiel $name ${games[$name]} $games_path/exp-a-spiel/$name.efg $games_path/exp-a-spiel/$name.jsonl
done
