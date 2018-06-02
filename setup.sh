mkdir /opt/simpletracker
mkdir /opt/simpletracker/log/
cp -f simpletracker.py /opt/simpletracker/simpletracker.py
cp -f simpletracker.service /lib/systemd/system/simpletracker.service
systemctl daemon-reload
