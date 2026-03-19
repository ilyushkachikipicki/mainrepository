#!/bin/bash

echo "Сумма всех оценок:"
awk '{sum += $2} END {print "   " sum}' students.txt
echo ""

echo "Средняя оценка:"
awk '{sum += $2; count++} END {print "   " sum/count}' students.txt
echo ""

echo "Максимальная оценка:"
awk 'NR==1{max=$2} $2>max{max=$2} END{print "   " max}' students.txt
echo ""
