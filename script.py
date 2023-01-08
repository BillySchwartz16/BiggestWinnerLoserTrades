import os

os.system('touch ./test.txt')

##open the file
file = open('test.txt', 'w')
instance_name = os.environ["instance_name"]
##write to the file
file.write(f'this instance is {instance_name}')
##close the file
file.close()