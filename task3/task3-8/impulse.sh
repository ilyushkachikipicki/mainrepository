#!/bin/bash
read -p "Имя гена: " name
read -p "Уровень его экспрессии: " exp
if [[ -z "$name" ]] || [[ -z "$exp" ]]; then
    echo "Ошибка: недостаточно данных"
else
    echo "Экспрессия гена $name составляет $exp единиц"
fi
