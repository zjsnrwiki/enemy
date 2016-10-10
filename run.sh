adb pull /sdcard/download/d$1 .
python dump.py d$1 $1
python load.py $1
python wiki.py
mv d$1 $1 data
