height_house_x = float(input())  # височината на къщата – реално число в интервала [2...100]
length_house_y = float(input())  # дължината на страничната стена – реално число в интервала [2...100]
height_roof_h = float(input())   # височината на триъгълната стена на прокрива – реално число в интервала [2...100]

face_of_back_wall = height_house_x * height_house_x
face_of_front_wall = height_house_x * height_house_x - 1.2 * 2
face_of_the_front_and_back_walls = face_of_front_wall + face_of_back_wall

face_of_side_walls = 2 * (height_house_x * length_house_y) - 2 * (1.5 * 1.5)

total_house_face = face_of_the_front_and_back_walls + face_of_side_walls

green_paint = total_house_face / 3.4

rectangles_roof = 2 * height_house_x * length_house_y
triangles_roof = 2 * (height_house_x * height_roof_h / 2)

roof_face = rectangles_roof + triangles_roof

red_paint = roof_face / 4.3

print('%.2f' % green_paint)
print('%.2f' % red_paint)