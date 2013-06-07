sudo modprobe pcspkr # allow beep to work

while true
do
	sleep .1
	echo $(date)
	lessc base.less base.css -x
	lessc home.less home.css -x
	if [[ $? != 0 ]]
	then beep -f 200 -l 5
		sleep 1
	fi
done
 ]]
