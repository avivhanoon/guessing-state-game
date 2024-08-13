import pandas as pd
import turtle
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("50_states.csv")
state_list = df.state.to_list()
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/ {len(state_list)} "
                                    f"Guess The State",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
screen.exitonclick()
