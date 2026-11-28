games_path=${GAMES_PATH:?}

run() {
	local source=$1
	local name=$2
	local solution=$games_path/solutions/$source/$name.txt

	shift 2
	./$source.py 1000000 "$@" --seed 42 < $solution > plays/$source/$name.jsonl
}
