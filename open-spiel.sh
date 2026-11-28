source plays.sh

declare -A games=(
	["abrupt-dark-hex-2"]="dark_hex(gameversion=adh,num_cols=2,num_rows=2)"
	["battleship-2x2-1-1-2-nr"]="battleship(board_width=2,board_height=2,ship_sizes=[1],ship_values=[1.0],num_shots=2,allow_repeated_shots=False)"
	["battleship-2x2-2-1-3"]="battleship(board_width=2,board_height=2,ship_sizes=[2],ship_values=[1.0],num_shots=3)"
	["battleship-2x2-2-2-3-nr"]="battleship(board_width=2,board_height=2,ship_sizes=[2],ship_values=[2.0],num_shots=3,allow_repeated_shots=False)"
	["battleship-3x2-2-1-3-nr"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[1.0],num_shots=3,allow_repeated_shots=False)"
	["battleship-3x2-2-1-3"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[1.0],num_shots=3)"
	["battleship-3x2-2-1-4-nr"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[1.0],num_shots=4,allow_repeated_shots=False)"
	["battleship-3x2-2-2-3-nr"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[2.0],num_shots=3,allow_repeated_shots=False)"
	["battleship-3x2-2-4-3-nr"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[4.0],num_shots=3,allow_repeated_shots=False)"
	["battleship-3x2-2-4-3"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[4.0],num_shots=3)"
	["battleship-3x2-2-4-4-nr"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[4.0],num_shots=4,allow_repeated_shots=False)"
	["battleship-3x2-2-4-4"]="battleship(board_width=2,board_height=3,ship_sizes=[2],ship_values=[4.0],num_shots=4)"
	["battleship-3x2-22-11-3-nr"]="battleship(board_width=2,board_height=3,ship_sizes=[2;2],ship_values=[1.0;1.0],num_shots=3,allow_repeated_shots=False)"
	["battleship-3x2-22-44-3"]="battleship(board_width=2,board_height=3,ship_sizes=[2;2],ship_values=[4.0;4.0],num_shots=3)"
	["battleship-3x3-12-11-2"]="battleship(board_width=3,board_height=3,ship_sizes=[1;2],ship_values=[1.0;1.0],num_shots=2)"
	["battleship-4x3-2-1-2-nr"]="battleship(board_width=3,board_height=4,ship_sizes=[2],ship_values=[1.0],num_shots=2,allow_repeated_shots=False)"
	["battleship-4x4-1-1-2"]="battleship(board_width=4,board_height=4,ship_sizes=[1],ship_values=[1.0],num_shots=2)"
	["battleship-5x2-2-1-2-nr"]="battleship(board_width=2,board_height=5,ship_sizes=[2],ship_values=[1.0],num_shots=2,allow_repeated_shots=False)"
	["big-leduc"]="universal_poker(numPlayers=2,betting=limit,stack=100 100,blind=1 1,raiseSize=2 4,numRounds=2,firstPlayer=1 1,maxRaises=6 6,numSuits=2,numRanks=12,numHoleCards=1,numBoardCards=0 1)"
	["coordinated-mp"]="coordinated_mp"
	["goofspiel-3-random"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=3,points_order=random))"
	["goofspiel-3"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=3,points_order=descending))"
	["goofspiel-4-random"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=4,points_order=random))"
	["goofspiel-4"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=4,points_order=descending))"
	["goofspiel-5-egocentric-point-difference"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,egocentric=True,num_cards=5,points_order=descending,returns_type=point_difference))"
	["goofspiel-5-random"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=5,points_order=random))"
	["goofspiel-5"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=5,points_order=descending))"
	["goofspiel-6-ascending"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=6,points_order=ascending))"
	["goofspiel-6"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=6,points_order=descending))"
	["goofspiel-7"]="turn_based_simultaneous_game(game=goofspiel(imp_info=True,num_cards=7,points_order=descending))"
	["kuhn-poker-13"]="universal_poker(numPlayers=2,betting=limit,blind=1 1,raiseSize=1 ,numRounds=1,firstPlayer=1 ,maxRaises=1 ,numSuits=1,numRanks=13,numHoleCards=1,numBoardCards=0 )"
	["kuhn-poker"]="kuhn_poker"
	["latent-ttt"]="latent_ttt"
	["leduc-poker-13"]="universal_poker(numPlayers=2,betting=limit,blind=1 1,raiseSize=2 4,numRounds=2,firstPlayer=1 1,maxRaises=2 2,numSuits=2,numRanks=13,numHoleCards=1,numBoardCards=0 1)"
	["leduc-poker-5"]="universal_poker(numPlayers=2,betting=limit,blind=1 1,raiseSize=2 4,numRounds=2,firstPlayer=1 1,maxRaises=2 2,numSuits=2,numRanks=5,numHoleCards=1,numBoardCards=0 1)"
	["leduc-poker-9"]="universal_poker(numPlayers=2,betting=limit,blind=1 1,raiseSize=2 4,numRounds=2,firstPlayer=1 1,maxRaises=2 2,numSuits=2,numRanks=9,numHoleCards=1,numBoardCards=0 1)"
	["leduc-poker"]="leduc_poker"
	["liars-dice-1-10"]="liars_dice(numdice=1,dice_sides=10)"
	["liars-dice-1-4"]="liars_dice(numdice=1,dice_sides=4)"
	["liars-dice-1-5"]="liars_dice(numdice=1,dice_sides=5)"
	["liars-dice-1-7"]="liars_dice(numdice=1,dice_sides=7)"
	["liars-dice-1-8"]="liars_dice(numdice=1,dice_sides=8)"
	["liars-dice-1-9"]="liars_dice(numdice=1,dice_sides=9)"
	["liars-dice-2-3"]="liars_dice(numdice=2,dice_sides=3)"
	["liars-dice-2-4"]="liars_dice(numdice=2,dice_sides=4)"
	["liars-dice-2-5"]="liars_dice(numdice=2,dice_sides=5)"
	["liars-dice"]="liars_dice"
	["oshi-zumo-4-1-6"]="turn_based_simultaneous_game(game=oshi_zumo(coins=4,size=1,horizon=6))"
	["oshi-zumo-7-2-7"]="turn_based_simultaneous_game(game=oshi_zumo(coins=7,size=2,horizon=7))"
)

for name in ${!games[@]}; do
	run open-spiel $name "${games[$name]}" $games_path/open-spiel/$name.efg $games_path/open-spiel/$name.jsonl
done

games=(
	["libratus-endgames-subgame-1"]="$(<LibratusEndgames/open-spiel-subgame1.txt)"
	["libratus-endgames-subgame-2"]="$(<LibratusEndgames/open-spiel-subgame2.txt)"
	["libratus-endgames-subgame-3"]="$(<LibratusEndgames/open-spiel-subgame3.txt)"
	["libratus-endgames-subgame-4"]="$(<LibratusEndgames/open-spiel-subgame4.txt)"
)

for name in ${!games[@]}; do
	run open-spiel $name "${games[$name]}" $games_path/open-spiel/$name.efg $games_path/open-spiel/$name.jsonl
done
