#!/usr/bin/env bash

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

PROFILE_LINE="alias benchmark=\"${SCRIPTPATH}/benchmark\""

eval "$PROFILE_LINE"
echo $PROFILE_LINE

if grep -Fxq "$PROFILE_LINE" ~/.zshrc
then
    echo "benchmark is already installed."
else
    echo ${PROFILE_LINE} >> ~/.zshrc
fi