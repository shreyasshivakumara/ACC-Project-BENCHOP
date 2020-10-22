#!/bin/sh

sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing rabbitmq..."
sudo apt-get install -y rabbitmq-server
sudo rabbitmq-server -detached

echo "Configuring rabbitmq..."
sudo rabbitmqctl add_user group4 password
sudo rabbitmqctl add_vhost group4vhost
sudo rabbitmqctl set_permissions -p group4vhost group4 ".*" ".*" ".*"

echo "Adding the SSH private key..."
echo "PRIVATE_KEY" > /home/ubuntu/.ssh/id_rsa
echo "PUBLIC KEY" > /home/ubuntu/.ssh/id_rsa.pub

echo "Installing celery..."
sudo -H pip3 install celery

echo "Installing flower..."
sudo -H pip3 install flower

echo "Installing flask..."
sudo -H pip3 install Flask
sudo -H pip3 install pygal

echo "Installing Octave and converter.."
sudo -H apt-get install octave
sudo -H pip3 install oct2py



echo "Installing the code..."
cd /home/ubuntu
sudo git clone https://github.com/TabeaHaverkamp/ACC-Project-BENCHOP.git


echo "Add authorised keys, so every team member can access."
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDa47krRFOEXwiKN5Mb65OZhP5evImAH3zyhvWRQPoYYaXR5H8aPsKM/kNlyiVytQ66rhtLimk89j3KGBC1Yh8hbBGw14PPvDslwBaEONrLXVHp+DFW6+0vY9Q6WaHEsXcUtg92MuNc+HBFAd66/v3MBId0EW8OQuFtBxI7mv5UKRySPoG9toHKvn3lvkxvT+Mg4rSYWPrnI8E6Y/3UMjYpqhdRg7j4haIiVEMmUc0UM3EfbUSG6jniIt+jO+IuuYtiuzHhHAWlgwwev5hZLsmdRAnuBGqc0RTk6906zrOGLOGIgd46TFtt5605vIg8PoncJDGlc3rxFXpsE2teqi7v Generated-by-Nova' >> /home/ubuntu/.ssh/authorized_keys
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCr7ncZBdiq6QAlRPO3OlnEhL4UJdOs4caaqgWYE+cpfRSo0G821f38CX6rahkzWMwBgwWHPKGSJuDzk1erBTvGK7FL+/iZKnXSRCBEooVj7nirWpIO9Urd+bvfmGgTaYU/sIIXtDjCRvnOKt3/bPcaOq+7NDtG5Rm/FB0aJ435ZEC6REbQaCCuxeNS1z9aoRtc9lS6XgDv2Urk8SPIgE6KR5jo/QQfveNL9Xghbz0ytnZf1yY5EDApVq7tHVT/+RAVLb9/27Tmd8AV+koH5MADg9cu4eTWeHMk7EulNtBwsSxrF5HtirDbDRdUkz2Yey7jHT0TCFz/dVI+ocuL+Eq3 Generated-by-Nova'  >> /home/ubuntu/.ssh/authorized_keys
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1vpoU4XXSokLjtgZbNL6PDL04JiOGv2+ua8ooOJpNVSlbQYVD+yiVcV/aJmaxgINqR9gI6sZlRSb1cTw7yMSpWxa+uXTbtsEfxaiVM2pOEI1eTBARrfngO+mb5pt48eX5BaRWtFARei6IuBVU8F8O9fz44arwkdVWWCJmb8W/6fddSW0XybzgvwMYWDp2dHwtRTzA4VYk0HSgliv2kHUTjbkLkRW69taNCxmgB1UWLPBRPmB13OWIMkx733fhfox4yyOFK8U1ospl8QgYWKuzOIN/+r8Ws9e7HKme6xxL8Tk5QbNAeTnsymWekQxulU8oxUG63RvG6hqz04aNAzuj Generated-by-Nova'  >> /home/ubuntu/.ssh/authorized_keys
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCnWVYlcqttENjr1+OvBLX+bUfUxMpDi4PdzbxYt/nYOw0CNgUsnxQlpXgXQ4BGNI1dtwgOizqntt/8g+FY0QTUbV9tL8ko8nNOQe/g9BC11fkndQvLRR0NHypzK5Ofcvln5WMBN7oVLZJq89ekjZ/lSR0uOnykqEev4k0xBoi8DYN5cDgRkT0T2f6D/+2N0wKCZZruh20FvuithZ8p7Prg5al8LXVt/Zif7hf4NGZNZ7XOZXN0HlW1gWAjbFS00eV4TeDDS7agCh2mjZ4O4hfliW3TDKjAiHg3Srygc6wdvWuIKi8WWpunDd7vdBNUDp+C2LVXM0k9RtW4JpfR6vIF root@vm3'  >> /home/ubuntu/.ssh/authorized_keys
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDpxmIxwCnAM8EWAnJI7zvHhMVwg7rqHXZUzg9IUEt8EbYB3lSMOJqB4jTzhyd4+6mFdzTrXT8sFkopi3Xz3PtYtkvcZMmTye1ljlo5axn2Py2odMbSPdByB9Iw6/n7EQHbe1Hxov6akroEZfXXrItTOYK3HlcnUsvC8h7bQ2Yo2U5NeKo7KaFxTMjfS70Y6K9Pw6FfhvPFagP2XTaaC36arz5jCOfCNpFvdeol7iAA3pq6z4xenKG8dIwjc7l+S04chgYdA5d2vsf6GgZf7OFFJtUMScPWUjFng4a2UUulHXXZRFuTNT8aHwNsWEINMq9Rs0Iymo9kvAmDwPCwdhfp root-777@ubuntu' >> /home/ubuntu/.ssh/authorized_keys
echo "Setting permission"
sudo chown -R ubuntu.users /home/ubuntu/ACC-Project-BENCHOP
