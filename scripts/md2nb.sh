#!/usr/bin/env bash
# convert markdown to notebook using jupytext
md2nb() {
  # exit if no args or $1 is empty
  if [[ $# -eq 0 ]] || [[ -z "$1" ]] ; then
    echo "md2nb: no arguments passed"
    return 1
  fi

  # exit if not md
  if [[ ! "$1" =~ \.md$ ]] ; then
    echo "md2nb: $1 is not a markdown file"
    return 1
  fi

  # get the base name of the file
  local base="${1%.*}"

  # if the file is empty, create an empty notebook
  if [[ ! -s "$1" ]] ; then
    echo '{"cells":[],"metadata":{}}' | tee "${base}.ipynb" > /dev/null
    return 0
  fi

  # remove previous notebook if it exists
  rm -f "${base}.ipynb"

  # convert
  jupytext --opt=split_at_heading=true --from=md:markdown --to=ipynb "$1"
} ; md2nb "$@"
