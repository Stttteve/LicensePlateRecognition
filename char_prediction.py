import os
import segmentation
import joblib
from lpr_locate import characters

from lpr_locate import column_list

current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, 'models/svc/svc.pkl')
model = joblib.load(model_dir)


classification_result = []

for each_character in characters:
    each_character = each_character.reshape(1,-1)
    result = model.predict(each_character)
    classification_result.append(result)

print(classification_result)

plate_string = ''
for each_prediction in classification_result:
    plate_string+= each_prediction[0]

print(plate_string)

column_list_copy = column_list[:]
column_list.sort()
correct_plate_string = ''

for each in column_list:
    correct_plate_string+= plate_string[column_list_copy.index(each)]

print(correct_plate_string)
