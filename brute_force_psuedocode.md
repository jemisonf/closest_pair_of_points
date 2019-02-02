Psuedocode for brute force algorithm:

```
Create empty list of pairs
For each pair:
	for each pair after the current pair:
		if distance between pairs is less than the current smallest distance,
			Update list of pairs to only have the current pair
			Update current smallest distance
		if distance between pairs is equal to the current smallest distance,
			Add current pairs to the list of closest pairs
return list of pairs and current closest distance 
```
