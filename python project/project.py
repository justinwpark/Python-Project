import greg
import justin

set_tiles,your_tiles=justin.input_list()

word_list=greg.list_of_words()

possibilities=justin.possible_combos(set_tiles,your_tiles)

plays=justin.possible_plays(word_list,possibilities)

justin.best_word(plays)



