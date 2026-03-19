#!/bin/bash

echo "=== Создание файлов ==="

for i in {1..10}; do
    filename="test${i}.txt"
    touch "$filename"
    echo "Создан файл: $filename"
done

echo "=== Проверка созданных файлов ==="
ls -la test*.txt 2>/dev/null || echo "Файлы не найдены"

echo -e "\n=== Удаление файлов в обратном порядке ==="

counter=10
while [ $counter -ge 1 ]; do
    filename="test${counter}.txt"
    
    if [ -f "$filename" ]; then
        rm "$filename"
        echo "Удален файл: $filename"
    else
        echo "Файл $filename не найден"
    fi
    
    counter=$((counter - 1))
done

echo "=== Проверка после удаления ==="
ls -la test*.txt 2>/dev/null || echo "Файлы успешно удалены, ни одного не осталось"

echo "Скрипт завершен."
