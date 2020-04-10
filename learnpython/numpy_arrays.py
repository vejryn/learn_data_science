# even though i ever worked on numpy let's re-learn!
import numpy as np

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

i = 1
for x in bmi:
    print("%s %s" % (i,x))
    i = i+1

#subsetting bmi

bmi > 24
print(bmi[bmi>24])