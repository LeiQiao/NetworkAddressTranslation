kill -9 `ps -ef | grep "uwsgi_nat.ini" | grep -v "grep" | awk '{print   $2}'`
sleep 1
nohup uwsgi --ini uwsgi_nat.ini &
