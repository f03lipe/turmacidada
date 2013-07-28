
sudo modprobe pcspkr # allow beep to work

trap "echo Ending the process; sudo modprobe -r pcspkr; exit 0" 2 # trap Ctrl

while true
do
	sleep .1
	echo $(date)
	lessc base.less base.css -x
	lessc home.less home.css -x
	if [[ $? != 0 ]]
	then
		beep -f 200
		sleep 2
	fi
done
