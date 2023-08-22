import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coordinates(x, y):
    """ Method to get X and Y coordinates from turtle screen"""
    print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)


def get_coordinates(state: pandas.DataFrame):
    """ Method to get X, and Y coordinates from dataframe"""
    x, y = state_data.x.iloc[0], state_data.y.iloc[0]
    return x, y


# Variables
states_df = pandas.read_csv("50_states.csv")
states_df.state.to_list()
states = states_df.state.to_list()
tim = turtle.Turtle()
number_of_states = len(states)
guessed = 0

while number_of_states > guessed:
    # Prompt window
    answer_state = screen.textinput(title=f"{guessed}/{number_of_states} Guess the State",
                                    prompt="Give me a state's name?").title()
    # If exit
    if answer_state == 'Exit':
        to_learn_data = pandas.DataFrame(states)
        to_learn_data.to_csv('states_to_learn.csv')
        print(to_learn_data)
        break

    # If correct
    if answer_state in states:
        states.remove(answer_state)
        guessed += 1
        tim.pu()
        state_data = states_df[states_df.state == answer_state]
        tim.goto(get_coordinates(state_data))
        tim.write(answer_state)
