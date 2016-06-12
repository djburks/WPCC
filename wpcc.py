import sys
from math import sqrt

# Make sure the input data is numerical and mappable to floats.
# Also ensure that all vectors are equal length.

def wpearson(vec_1, vec_2, weights, r = 4):
	
	list_length = len(vec_1)

	try:
		weights = list(map(float,weights))
	except:
		print('Invalid weights.')
		sys.exit(1)
	
	try:
		vec_1 = list(map(float,vec_1))
		vec_2 = list(map(float,vec_2))
		if any(len(x) != list_length for x in [vec_2,weights]):
			print('Vector/Weight sizes not equal.')
			sys.exit(1)
	except:
		print('Invalid vectors.')
		sys.exit(1)


# Find total weight sum.

	w_sum = sum(weights)

# Calculate the weighted average relative value of vector 1 and vector 2.
	vec1_sum = 0.0
	vec2_sum = 0.0

	for x in range(len(vec_1)):
		vec1_sum += (weights[x] * vec_1[x])
		vec2_sum += (weights[x] * vec_2[x])
	
	vec1_avg = (vec1_sum / w_sum)
	vec2_avg = (vec2_sum / w_sum)

# Calculate wPCC

	sum_top = 0.0
	sum_bottom1 = 0.0
	sum_bottom2 = 0.0

	
	for x in range(len(vec_1)):
		dif_1 = (vec_1[x] - vec1_avg)
		dif_2 = (vec_2[x] - vec2_avg)
		sum_top += (weights[x] * dif_1 * dif_2)
		sum_bottom1 += (dif_1**2)*(weights[x])
		sum_bottom2 += (dif_2**2)*(weights[x])

	cor = sum_top / (sqrt(sum_bottom1 * sum_bottom2))

	return round(cor,r)


