#To import particular variable from another file
from constants import CURRENT_STUDENT_COUNT, CURRENT_MENTOR_COUNT 

print('There are currently' , CURRENT_STUDENT_COUNT , 'number of participants')
print('There are currently' , CURRENT_MENTOR_COUNT, 'number of mentors')

#To import the whole module
import constants

print(f'There are currently {constants.CURRENT_STUDENT_COUNT} number of participants')
print('There are currently',constants.CURRENT_MENTOR_COUNT, 'number of mentors')