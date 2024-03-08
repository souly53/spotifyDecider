def	chooseArtist(DataFrame):
	i = 0
	x = 1
	count = 0
	print("what kinda mood are you feeling today?")
	mood = input()
	print('thank you')
	while (count == 0):
		while (i < len(DataFrame)):
			while (x < len(DataFrame.iloc[i])):
				if (DataFrame.iloc[i, x] == mood):
					print('You should listen to ' + DataFrame.iloc[i, 0])
					count = count + 1
					break 
				x = x + 1
			i = i + 1
			x = 0
		if (count == 0):
			print("Sorry we couldnt find any Artists that match your mood... "
					"do you mind specifying your mood?")
			mood = input()
			i = 0