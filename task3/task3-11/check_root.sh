#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "ОШИБКА: Скрипт должен быть запущен от имени суперпользователя (root)!"
        echo "Текущий UID: $EUID"
        echo "Используйте: sudo $0"
        return 1
    else
        echo "Проверка пройдена: скрипт запущен от root (UID: $EUID)"
        return 0
    fi
}

