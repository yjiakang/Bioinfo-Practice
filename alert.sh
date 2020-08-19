#!/bin/sh
alert () {
if [ $1 -ne 0 ]
then
	echo "$2 not complete successfully"
	exit $1
else
	echo "$2 complete successfully"
fi
}
cd nm
alert $? "cd nm"
