source plays.sh

declare -A games=(
	["kuhn-poker"]="KuhnPoker"
	["leduc-holdem"]="LeducHoldem"
	["numeral211-holdem"]="Numeral211Holdem"
	["rhode-island-holdem"]="RhodeIslandHoldem"
	["royal-rhode-island-holdem"]="RoyalRhodeIslandHoldem"
)

for name in ${!games[@]}; do
	run huflhe $name ${games[$name]} $games_path/huflhe/$name.efg $games_path/huflhe/$name.jsonl
done
