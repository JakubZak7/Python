import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")



# Side length
side_length = 50
triangle_lenght = 100
lenght_a = 40
lenght_b = 60

figures.draw_square(side_length)
figures.draw_triangle(triangle_lenght)
figures.draw_rectangle(lenght_a,lenght_b)

# Hide the turtle and finish

window.mainloop()