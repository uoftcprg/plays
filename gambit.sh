source plays.sh

declare -A games=(
	["myerson1991-fig2-1"]="books/myerson1991/fig2_1"
	["reiley2008-fig1"]="journals/other/reiley2008/fig1"
	["vonstengel2022-fig10-12"]="books/vonstengel2022/fig10.12"
	["vonstengelforges2008-fig6"]="journals/mor/vonstengelforges2008/fig6"
)

for name in ${!games[@]}; do
	run gambit $name ${games[$name]} $games_path/gambit/$name.efg $games_path/gambit/$name.jsonl
done
