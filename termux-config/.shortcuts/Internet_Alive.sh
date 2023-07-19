 

PING_MSG=`ping -c 1 8.8.8.8 2 >&1 | tail -n 2 ; exit $?`
stat=$?

SETTING='-b "black" -c "white"';
ACT_MESSAGE="Internet Active";
INACT_MSG="Internet not active!";
if [ "${stat}" != "0" ]
then
	eval termux-toast ${SETTING} ${INACT_MSG}
else
	eval termux-toast ${SETTING} ${ACT_MSG}
fi
