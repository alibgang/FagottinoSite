#!/bin/bash

tryCleanUp() {
    toBeDeleted=("$@")

    printf "\nDo you want clean up the following file(s)? "
    printf '%s\n' "${toBeDeleted}"
    read -p "y/n? " -n 1 -r

    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        deleteItems "${toBeDeleted[@]}"
    fi


}

deleteItems() {
    toBeDeleted=("$@")

    for item in "${toBeDeleted[@]}"; do
        printf "\nDeleting: $item"
        rm $item
    done
    printf "\nFinished cleanup!"
}