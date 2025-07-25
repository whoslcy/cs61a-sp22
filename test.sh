#!/usr/bin/env bash
#
# Test the assignments of the discussion section in the course CS 61A.

press_any_key_to() {
  echo
  read -n 1 -s -r -p "Press any key to $1"
  clear
}

test_a_section() {
  echo "Start testing the $1 section."

  local old_pwd=$(pwd)
  for directory in "${@:2}"; do
    cd "${directory}"

    # `ok` is the CS 61A official assignment grader.
    # [The reference](https://cs61a.org/articles/using-ok/)
    # [The command generator](https://ok-help.cs61a.org/)
    python3 ok --local

    cd "${old_pwd}"
    press_any_key_to "test the next one if any."
  done
}

test_a_section homework hws/hw0{1..8}
test_a_section lab labs/lab{00,01,02,04,05,06,07,08,10,11,12,13}
test_a_section project projs/{ants,cats,hog,lambdaing}

echo "Start testing the discussion section."

press_any_key_to 'check the Python3 `doctest`s.'
DOCTEST='python3 -m doctest discs/disc{01,02,03,04,05,06,07,13}/*.py'
echo "${DOCTEST}"
bash -c "${DOCTEST}"
echo
echo 'All `doctest`s passed.'

press_any_key_to "test the Scheme functions."
test_scheme() {
  local SCHEME_INTERPRETER=labs/lab10/scheme

  for scheme_file in "$@"; do
    echo "${scheme_file}:"
    echo

    python3 "${SCHEME_INTERPRETER}" "${scheme_file}"

    press_any_key_to "test the next Scheme function if any."
  done
}
test_scheme discs/disc10/q{1,3,4,5}.scm discs/disc11/q{2,3}.scm
echo 'All Scheme function tests passed.'

press_any_key_to 'end the test.'
