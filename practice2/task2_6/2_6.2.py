donor = int(input(" введите группу крови донора"))
pacient = int(input( " введите группу крови пациента"))
if donor == pacient or donor == 1 or pacient==4:
    print("Можно")
else:
    print(" нельзя")