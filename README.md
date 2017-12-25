________________________________
# ShellBot
________________________________

### для запуска на платформах armhf и amd64 потребуется:
    если в системе стоит 2 версии python, а именно 2.7 и 3.5 , то нужды устанавливать 3.6 нет. пропускаем следующие пункты до симлинка..
    wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz
    tar -xpJf Python-3.6.0.tar.xz
    cd Python-3.6.0
    ./configure
    make
    sudo make install
    ln -s /usr/local/bin/python3 /usr/bin/python3 если терминал выплюнул вам что уже есть такой файл но версия python по умолчанию всё равно 2.7 то попробуйте сделать симлинк вот так sudo ln -sf python3 /usr/bin/python. это принудительно поменяет версию на python 3.6 или python 3.5
    sudo apt-get install python3-pip
    $ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
    $ cd python-telegram-bot
    $ python setup.py install
    pip install --upgrade pip
    pip install setuptools
    pip install telepot
    pip install --upgrade pip
    далее идем в папку с ботом и запускаем ./botssh.sh
________________________________
### для i386
    sudo apt-get install build-essential
    sudo apt-get install libssl-dev
    sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libsqlite3-dev
    если в системе стоит 2 версии python, а именно 2.7 и 3.5 , то нужды устанавливать 3.6 нет. пропускаем следующие пункты до симлинка..
    wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz (если 3.6.0 не устанавливается в i386)
    tar -xpJf Python-3.5.0.tar.xz
    cd Python-3.5.0
    ./configure
    make
    sudo make install
    ln -s /usr/local/bin/python3 /usr/bin/python3 если терминал выплюнул вам что уже есть такой файл но версия python по умолчанию всё равно 2.7 то попробуйте сделать симлинк вот так sudo ln -sf python3 /usr/bin/python. это принудительно поменяет версию на python 3.6 или python 3.5
    sudo apt-get install python3-pip
    $ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
    $ cd python-telegram-bot
    $ python setup.py install
    pip install --upgrade pip
    pip install setuptools
    pip install telepot
    pip install --upgrade pip
    далее идем в папку с ботом и запускаем ./botssh.sh
________________________________
### добавляем в автозагрузку

    # пихаем shell-bot.service в /etc/systemd/system/
    # задаем права chmod + X /etc/systemd/system/shell-bot.service
    # запускаем systemctl start shell-bot.service
    # добавляем в автозагрузку systemctl enable shell-bot.service
    # проверяем статус приложения systemctl status shell-bot.service
________________________________
