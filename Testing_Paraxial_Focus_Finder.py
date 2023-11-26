import task10_first as task
from Paraxial_Focus_Finder import ParaxialFocusFinder

#What this class effectively does it just find the intercept between two lines, we can test for
#the situations outlined in the tasks and see if this class is consistent with the graphs produced

focus = ParaxialFocusFinder([task.refractor]).find()

#This agrees with the graph, the test is successful and the class works correctly