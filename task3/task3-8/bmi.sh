#!/bin/bash
read -p "Введите свою массу в кг: " mass
read -p "Введите сой рост в м: " height
echo $"scale=2; $mass / ( $height * $height )" | bc
