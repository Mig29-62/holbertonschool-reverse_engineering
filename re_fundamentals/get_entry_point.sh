#!/bin/bash
source ./messages.sh
file_name=$1
magic_number=$(readelf -h $1 | grep Magic | awk '{print $2,$3,$4,$5,$6,$7,$8,$9,$10}')
class=$(readelf -h $1 | grep Class | awk '{print $2}')
byte_order=$(readelf -h $1 | grep Data | awk '{print $2,$3,$4,$5}')
entry_point_address=$(readelf -h $1 | grep Entry | awk '{print $4}')
display_elf_header_info
