#!/bin/bash
echo "Пользователь: $(whoami)"
echo "Время: $(date +"%H:%M:%S")"
echo "Путь $(pwd)"
echo "Аргументов: $#"
