#!/usr/bin/env bash
# convert markdown to notebook (or vice versa) using jupytext
md2nb() {
  # exit if no args or $1 is empty
  if [[ $# -eq 0 ]] || [[ -z "$1" ]] ; then
    echo "mdnb: no arguments passed"
    return 1
  fi

  # get the extension and base name
  local ext="${1##*.}"
  local base="${1%.*}"

  # exit if ext is not md or ipynb
  if [[ "$ext" != "md" ]] && [[ "$ext" != "ipynb" ]] ; then
    echo "mdnb: file must be markdown or notebook"
    return 1
  fi

  # if the ext is md and is empty create an empty notebook
  if [[ "$ext" == "md" ]] && [[ ! -s "$1" ]] ; then
    echo '{"cells":[],"metadata":{}}' | tee "${base}.ipynb" > /dev/null
    return 0
  fi

  # convert
  if [[ "$ext" == "md" ]] ; then
    jupytext --opt=split_at_heading=true --from=md:markdown --to=ipynb "$1"
  else
    jupytext --from=ipynb --to=md:markdown "$1"
  fi
} ; md2nb "$@"
