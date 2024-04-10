import paramiko
import time

host = '77.238.231.249'
port = 22
username = 'root'
password = 'eK3b2y87gTv8CJrM'

# Устанавливаем SSH-соединение
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

start_time_ = time.time()
1
requests = ['ab -n 1000 -c 10 https://mail.ru/', #
            'ab -n 1000 -c 10 https://vk.com/feed',
            'stress --cpu 4 --timeout 60s',
            'iperf -c server_ip -t 60',
            'ping -c 100 remote_host'
            ]

for request in requests:
    start_time = time.time()
    try:
        ssh.connect(host, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(request)
        for line in stdout.readlines():
            print(line.strip())
    finally:
        ssh.close()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Время выполнения отдельного процесса: ", execution_time)

end_time_ = time.time()
execution_time_ = end_time_ - start_time_
print("Общее время выполнения: ", execution_time_)
