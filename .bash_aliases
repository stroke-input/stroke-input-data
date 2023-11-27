alias extract_post_tab='grep -Po "(?<=\t).*"'

stroke_input_search()
{
  grep -P "^$1\\t" sequence-characters.txt | extract_post_tab
}

stroke_input_search_prefix()
{
  grep -P "^$1" sequence-characters.txt | extract_post_tab
}

stroke_input_search_suffix()
{
  grep -P "$1\\t" sequence-characters.txt | extract_post_tab
}

alias s='stroke_input_search'
alias sp='stroke_input_search_prefix'
alias ss='stroke_input_search_suffix'
