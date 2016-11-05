adb pull /sdcard/download/$1 .
python decode.py $1 $1_decode
python load.py $1_decode
python wiki.py
mkdir -p data/orig
mv $1 data/orig
mv $1_decode data
