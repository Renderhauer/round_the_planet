from time import sleep

frame_count = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print('\u001b[31m')
def clear_screen():
  sleep(0.5)
  print('\033[2J')
  print('\u001b[25A')
  return 0

def turn_planet():
  print('\u001b[32m')
  for i in frame_count:
    current_frame = 'frame' + str(i) + '.txt'
    frame = open(current_frame, 'r')
    clear_screen()
    print(frame.read())
  sleep(1)
  clear_screen()
  print('\u001b[0m')
  current_frame = open('the_end.txt', 'r')
  print(current_frame.read())

turn_planet()