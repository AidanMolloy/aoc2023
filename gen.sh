#! /bin/bash
read -p "Day: " day

echo "Creating directory..."
day_length=${#day}
if [ $day_length -eq 1 ]
then
    formatted_day="0$day"
else
    formatted_day="$day"
fi
mkdir $formatted_day

echo "Copying template..."
cp template.py $formatted_day.py
touch $formatted_day/sample.txt
touch $formatted_day/input.txt

echo "Done!"