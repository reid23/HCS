#!/usr/bin/env bash

#This script "installs" the benchmark command line tool.
# all it does is download the binary from github and make
# an alias to it in your ~/.zshrc file.
# After it runs, you can just run `benchmark [options]`
# to use benchmark.
# This only works on macs with the exact same architecture as mine
# because it's not a product and I don't think you have a different computer

#! to revert the changes made by this script:
#! 1. delete the benchmark file (it's in the same directory as this script)
#! 2. delete the line from ~/.zshrc that says
#!    `alias benchmark="/path/to/here/benchmark"`
#! then when you restart your terminal it won't have the alias
#! anymore and will be back to normal



SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

PROFILE_LINE="alias benchmark=\"${SCRIPTPATH}/benchmark\""

download_fail () {
    echo "Download failed, quitting."
    exit 1
}

echo $PROFILE_LINE


if [ "$1" == "--update" ]
then
    echo "downloading most current binary..."
    curl --silent -L https://raw.githubusercontent.com/reid23/HCS/Lab10/Lab10/benchmark --output "$SCRIPTPATH/benchmark" || download_fail
    echo "update complete"
    chmod +x "$SCRIPTPATH/benchmark"
    $PROFILE_LINE
    exit 0
fi

if grep -Fxq "$PROFILE_LINE" ~/.zshrc
then
    echo "benchmark is already installed."
else
    echo "Dowloading..."
    curl --silent -L https://raw.githubusercontent.com/reid23/HCS/Lab10/Lab10/benchmark --output "$SCRIPTPATH/benchmark" || download_fail
    echo "Download finished."
    chmod +x "$SCRIPTPATH/benchmark"
    $PROFILE_LINE
    echo ${PROFILE_LINE} >> ~/.zshrc
    echo "benchmark successfully installed!"
fi