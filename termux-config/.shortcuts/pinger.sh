#!/data/data/com.termux/files/usr/bin/bash

### Configuration
SITE="ya.ru"                    # hostname to ping
INTERVAL=7                      # ping interval in seconds
LED_ON_MS=800                   # milliseconds for the LED to be on while it's flashing
LED_OFF_MS=600                  # milliseconds for the LED to be off while it's flashing
LED_UP_COLOR="00ff00"           # color of the blinking LED when there is connection as RRGGBB (green)
LED_DOWN_COLOR="ff0000"         # color of the blinking LED when there is no connection as RRGGBB (red)
VIBRATE_UP_PAT=300              # vibrate pattern when connection is established, comma separated
VIBRATE_DOWN_PAT=150,150,150    # vibrate pattern when connection is lost, comma separated
TITLE_UP="Internet is UP"           # notification title when connection is established
TITLE_DOWN="Internet is DOWN"       # notification title when connection is lost
NOTIFY_ID=666                   # notification ID

### Job
BTN_NAME="Stop pinging"
BTN_ACTION="termux-notification-remove '${NOTIFY_ID}' && kill $$"
NOTIFY_ARGS_COMMON="--id '${NOTIFY_ID}' --priority max --on-delete '${BTN_ACTION}' --action '${BTN_ACTION}' --button1 '${BTN_NAME}' --button1-action '${BTN_ACTION}' --led-on '${LED_ON_MS}' --led-off '${LED_OFF_MS}'"
NOTIFY_ARGS_UP="--led-color '${LED_UP_COLOR}' --sound --vibrate '${VIBRATE_UP_PAT}' --title '${TITLE_UP}'"
NOTIFY_ARGS_DOWN="--led-color '${LED_DOWN_COLOR}' --sound --vibrate '${VIBRATE_DOWN_PAT}' --title '${TITLE_DOWN}'"
PREV_STATUS=-1

while true
do
    PING_MSG=`ping -c 1 "${SITE}" 2>&1 | tail -n 2 ; exit ${PIPESTATUS[0]}`
    PING_STATUS=$?
    NOTIFY_ARGS_CONTENT="--content '${PING_MSG}'"
    if [[ ${PING_STATUS} -eq 0 ]]
    then
        if [[ ${PREV_STATUS} -ne 0 ]]
        then eval termux-notification ${NOTIFY_ARGS_COMMON} ${NOTIFY_ARGS_CONTENT} ${NOTIFY_ARGS_UP}
        fi
    else
        if [[ ${PREV_STATUS} -le 0 ]]
        then eval termux-notification ${NOTIFY_ARGS_COMMON} ${NOTIFY_ARGS_CONTENT} ${NOTIFY_ARGS_DOWN}
        fi
    fi
    PREV_STATUS=${PING_STATUS}
    sleep $INTERVAL
done
