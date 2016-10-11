adb pull /sdcard/download/$1 .
python decode.py $1 $1_decode
python load.py $1_decode
python wiki.py
mkdir -p data
mv $1 $1_decode data
