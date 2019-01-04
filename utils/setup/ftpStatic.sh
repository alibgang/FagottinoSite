#!/bin/bash

# Load Utils
pushd ../
source ./utils.sh
popd

ENV=$1
ENV_MESSAGE=""
FTP_CONFIG_DIR=../../config/ftp
FTP_CONFIG_FILE="../../config/ftp/$ENV"



main() {
    #format var
    ENV=$(strToLower $ENV)
    # init
}

main

######## GET ENVARS ########
if [[ "$ENV" == "prod" ]]; 
then
    #prod(VPS)variabls
    FTP_CONFIG_FILE=../../config/ftp/.prod_env
else
    #Staging(VPS)variabls
    FTP_CONFIG_FILE=../../config/ftp.vps_env
fi

echo $FTP_CONFIG_DIR
echo $FTP_CONFIG_FILE


setupEnvFile() {
    # Check if an .env file exist if not lets create it
    if [ ! -f "${FTP_CONFIG_FILE}" ]; then
        printf "\n.env not found.  Lets generate it...\n\n"
        mkdir -p $FTP_CONFIG_DIR

        read -p "Enter ftp username: " -r user
        read -p "Enter ftp password: " -r password
        read -p "Enter ftp ip: " -r ftpip

        printf "Writing to .env ->\n\nuser: ${user}\npassword: ${password}\nftpip ${ftpip} \n"
        printf "To config dir @: ${FTP_CONFIG_DIR}\n\n"
        sleep 1
        touch $FTP_CONFIG_FILE
        printf "Changing ownership of dir ${FTP_CONFIG_DIR}\nYou might need to enter your user (${USER}) password\n" 
        sudo chown -R $USER $FTP_CONFIG_DIR

        echo "export USER=${user}" >>  $FTP_CONFIG_FILE 
        echo "export PASS=${password}" >> $FTP_CONFIG_FILE 
        echo "export FTPIP=${ftpip}" >> $FTP_CONFIG_FILE
    fi

    if [ -f "${FTP_CONFIG_FILE}" ]; then
        source $FTP_CONFIG_FILE
    fi
}

zipup() {
    read -p "Enter full path to directory or file to upload " -r FILE_PATH
    
    TARNAME=$(basename "$FILE_PATH")
    TARNAME+=".tar.gz"

    res=$(tar -czvf $TARNAME $FILE_PATH)
    echo $res
    
    printf "Launch SFTP Session....\n\n"
    sleep 2

    printf "Uploading ${TARNAME} to VPS@ ${FTPIP} /data/${TARNAME}\n\n\n"
    res=$(lftp sftp://$USER:$PASS@$FTPIP -e "put ${TARNAME}; bye")

    checkFTPTransfer $res

    tryCleanUp $TARNAME
}

checkFTPTransfer() {
    ftpRes=$(echo "$@")
    transferred=$(echo $ftpRes | grep "[1-9]* bytes transferred")
    echo $transferred
    if [[ -n $transferred ]];
    then
        echo "SFTP Succesfull uploaded ${transferred}"
    else
        echo "SFTP failed!"
    fi
}

init() {
    printf "\n************ WELCOME TO FTP MANAGER ************\n\n"
    printf  "Currently running in a $ENV_MESSAGE"
    printf  "The purpose of this script is to compress and upload files the to a specified server.\n"
    printf  "This will compress the file or directory and sftp it the the server.\n"
    printf  "The script requires a .env file to run.  \nIf it does not exist it will be created for you.\nJust follow the on screen prompts.\n\n"

    read -p "Do you want to continue choose y/n? " -n 1 -r
 
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        printf "\n"
        setupEnvFile
    fi
    zipup
}


