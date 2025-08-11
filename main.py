import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen_turtle = turtle.shape(image)
move_t = turtle.Turtle()
move_t.speed(0)
move_t.hideturtle()
move_t.penup()

correct_guess = []
score = 0 
for i in range(51):
    answer_state = screen.textinput(title=f"Guess the state {len(correct_guess)}/50", prompt="What is another states name?").title()
    data = pandas.read_csv("50_states.csv")
    if answer_state == "Exit":
        break
    elif answer_state in data.state.tolist():
        loc = data[data.state == answer_state]
        move_t.goto(loc.x.item(), loc.y.item())
        move_t.write(answer_state, False, align="center", font=("Arial", 8, "normal"))
        score += 1
        correct_guess.append(answer_state)
            
turtle.mainloop()
 
states_missed = data.state.to_list()
for i in states_missed[:]:
    if (i in correct_guess):
        states_missed.remove(i)

missed_dict = { 
    "State": states_missed
}

print(missed_dict)
        
pandas.DataFrame(missed_dict).to_csv("MissedStates.csv")
