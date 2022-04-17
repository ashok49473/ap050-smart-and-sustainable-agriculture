#!/bin/bash
export IOTHUB_DEVICE_SECURITY_TYPE='DPS'
export IOTHUB_DEVICE_DPS_ID_SCOPE='0ne00564BCA'
export IOTHUB_DEVICE_DPS_DEVICE_ID='DE10Nano'
export IOTHUB_DEVICE_DPS_DEVICE_KEY='OcKGd7imbHlIuUxksKcIXTnrDYRrA1DtwyLwnnZRrpbiMYNZTvTk/xiriIN11364hmgdEVnsv1BLMHkpW9+PHA=='

overlay_dir="/sys/kernel/config/device-tree/overlays/socfpga_1"
overlay_dtbo="rfs-overlay.dtbo"
overlay_rbf="Module5_Sample_HW.rbf"

if [ -d $overlay_dir ];then
    rmdir $overlay_dir
fi

cp $overlay_dtbo /lib/firmware/
cp $overlay_rbf /lib/firmware/

mkdir $overlay_dir

#echo $overlay_dtbo > $overlay_dir/path

cd ../
python3.7 -u ./main.py
