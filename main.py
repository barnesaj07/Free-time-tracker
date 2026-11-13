from bakery import assert_equal
from dataclasses import dataclass
from drafter import *

hide_debug_information()
set_website_style("water")
set_website_title("Free time tracker")
set_site_information(author="Aiden Barnes",
                     description="Takes user input and calculates their available freetime. They can select the time frame as a week,weekdays, or one day",
                     sources="The drafter documentation website for the coding. ChatGPT for the initial brainstorming",  
                     planning=["https://docs.google.com/document/d/1aNg5OmOhiuRS4wbjnKiMoYYXGoxC-HfWyLgY_2smsDs/edit?usp=sharing","https://chatgpt.com/","https://docs.google.com/document/d/1yOqP-8_TI6w-DdZMSAkkSecCFEsnKct0xN5w5sjXZqo/edit?usp=sharing"], 
                     links="https://barnesaj07.github.io/Free-time-tracker/"
                    )
set_website_framed(False)
   
    
@dataclass
class Day:
    """
    Represents a Day item with its name and times.

    Attributes:
        day_of_week (str): The day of the week.
        sleep (float): The amount of time in hours spent sleeping.
        eating (float): The amount of time in hours spent eating.
        personal_care (float): The amount of time in hours spent on personal_care.
        chores (float): The amount of time in hours spent doing chores.
        social (float): The amount of time in hours spent socializing.
        work (float): The amount of time in hours spent working.
        classes (float): The amount of time in hours spent attending classes.
        club (float): The amount of time in hours spent attending clubs.
        commuting (float): The amount of time in hours spent commuting.
        exercise (float): The amount of time in hours spent exercising.
        study (float): The amount of time in hours spent studying.
        other (float): The amount of time in hours spent doing other tasks.
    """
    day_of_week:str
    sleep: float
    eating:float
    personal_care:float
    chores:float
    social:float
    work:float
    classes:float
    club:float
    commuting:float
    exercise:float
    study:float
    other:float
@dataclass
class State:
    """
    Represents the state of the free time tracker application.

    Attributes:
        is_week (bool): Whether the user is tracking free time for a week.
        is_weekday (bool): Whether the user is tracking free time for the weekdays.
        is_day (bool): Whether the user is tracking free time for a day.
        busy_time (float): The total time spent on tasks.
        week_time (list[Day]): A list of Day items that represent the 7 days of the week.
    """
    is_week:bool
    is_weekday: bool
    is_day: bool
    busy_time:float
    week_time: list[Day]

    

place_holder=Day("",0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)   
@route
def index(state:State)->Page:
    '''
        The introduction for the website. Prompts the user about if they want
        to track free time for the day, weekdays or whole week.

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Returns a page with three buttons for input and a title.
    '''
    return Page(state,
                [
                    change_text_size(bold("Freetime Tracker\n"), "50px"),
                    Button("One Day","one_day"),
                    Button("Weekdays","weekdays"),
                    Button("Whole Week","whole_week")
                ],
            )
assert_equal(index(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                [
                    change_text_size(bold("Freetime Tracker\n"), "50px"),
                    Button("One Day","one_day"),
                    Button("Weekdays","weekdays"),
                    Button("Whole Week","whole_week")
                ]
                                                                   )
             )
@route
def get_activity_time(state:State)->Page:
    '''
        The website prompts users for the amount of time they spend on certain activities.
        Depending on the time frame selected, the select_day box will be altered.

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Depending on the button pressed, a hour logging page for one day/week or weekdays.
                If the button was pressed, the save_day page will be displayed.
    '''
    if state.is_day or state.is_week:
        return Page(state,
                    [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                                  "Sunday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                        
                        
                    ],
                )
    else:
        return Page(state,
                [
                    change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Monday","Tuesday","Wednesday","Thursday","Friday"],
                                  "Monday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                ],
            )
                    
assert_equal(get_activity_time(State(False,True,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(False,True,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                [
                    change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Monday","Tuesday","Wednesday","Thursday","Friday"],
                                  "Monday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                ],
            )

                
                                                            )
assert_equal(get_activity_time(State(False,False,True,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(False,False,True,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                                  "Sunday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                ],
            )

                
                                                            )

assert_equal(get_activity_time(State(True,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(True,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                                  "Sunday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                ],
            )

                
                                                            )


@route
def one_day(state:State)->Page:
    '''
        Sets the is_day state to true. 

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Returns the activity_time page.
    '''
    state.is_day=True
    return get_activity_time(state)

assert_equal(one_day(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(False,False,True,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                    [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                                  "Sunday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                        
                        
                    ]
             )
             )

@route
def whole_week(state:State)->Page:
    '''
        Sets the is_week state to true. 

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Returns the activity_time page.
    '''
    state.is_week=True
    return get_activity_time(state)

assert_equal(whole_week(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(True,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                    [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                                  "Sunday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                        
                        
                    ]
             )
             )
@route
def weekdays(state:State)->Page:
    '''
        Sets the is_weekday state to true. 

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Returns the activity_time page.
    '''
    state.is_weekday=True
    return get_activity_time(state)

assert_equal(weekdays(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(False,True,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                    [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Monday","Tuesday","Wednesday","Thursday","Friday"],
                                  "Monday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                        
                        
                    ]
             )
             )
@route
def calculate_free_time(state:State)->Page:
    '''
        Calculates the available free time if any of the requirements are met. 

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Returns the activity_time page if the requirments aren't met.
            Returns a page that displays the total free time and a reset button if the requirements are met.
    '''
    days = 0
    for day in state.week_time:
        if day.day_of_week in ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]:
            days += 1
  
                
            
    if state.is_day or (state.is_week and days == 7) or (state.is_weekday and days ==5):
        for day in state.week_time:
            state.busy_time +=(day.sleep+day.eating+day.personal_care+day.chores+day.social+
                                day.work+day.classes+day.club+day.commuting+day.exercise+day.study+day.other)
        free_time = (days*24.0)- state.busy_time
        if free_time < 0.0:
            free_time = 0.0
        return Page(state,
            [
                change_text_size(bold('Total Free time\n'), "50px"),
                free_time," hours\n",
                Button("Reset","reset")
            ]
        )
    return get_activity_time(state)

assert_equal(calculate_free_time(State(False,False,True,0.0,[place_holder,Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                                             place_holder,place_holder,place_holder,place_holder,place_holder])),
             Page(State(False,False,True,8.0,[place_holder,Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                                             place_holder,place_holder,place_holder,place_holder,place_holder]),
               [
                change_text_size(bold('Total Free time\n'), "50px"),
                16.0," hours\n",
                Button("Reset","reset")
               ]
             
             
             )
             )
assert_equal(calculate_free_time(State(True,False,False,0.0,[
                                              Day("Sunday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Saturday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)])),
             Page(State(True,False,False,56.0,[Day("Sunday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Saturday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)]),
               [
                change_text_size(bold('Total Free time\n'), "50px"),
                112.0," hours\n",
                Button("Reset","reset")
               ]
             
             
             )
             )
assert_equal(calculate_free_time(State(False,True,False,0.0,[
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)])),
             Page(State(False,True,False,40.0,[Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)]),
               [
                change_text_size(bold('Total Free time\n'), "50px"),
                80.0," hours\n",
                Button("Reset","reset")
               ]
             
             
             )
             )             
             
assert_equal(calculate_free_time(State(False,True,False,0.0,[
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)])),
                         Page(State(False,True,False,0.0,[Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)]),

                     [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Monday","Tuesday","Wednesday","Thursday","Friday"],
                                  "Monday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                        
                        
                    ]
             )
            )                                            
                                                             
                                                             

@route
def save_day(state:State,select_day:str,sleep:str,eating:str,personal_care:str,
                                         chores:str,social:str,work:str,classes:str,club:str,
                                         commuting:str,exercise:str,study:str,other:str)->Page:
    '''
        Saves the current day/task that was inputed in the week_time state as a Day object.
        Saves based on correponding day in week_time state. Try and except checks to see
        if the given code displays an error. If it throws the error it will prompt the user
        to input a new day. If theres no error the code will continue as expected

        Args:
            state (State): The current state the file is in.
            select_day (str): The day of the week.
            sleep (str): The amount of time in hours spent sleeping.
            eating (str): The amount of time in hours spent eating.
            personal_care (str): The amount of time in hours spent on personal_care.
            chores (str): The amount of time in hours spent doing chores.
            social (str): The amount of time in hours spent socializing.
            work (str): The amount of time in hours spent working.
            classes (str): The amount of time in hours spent attending classes.
            club (str): The amount of time in hours spent attending clubs.
            commuting (str): The amount of time in hours spent commuting.
            exercise (str): The amount of time in hours spent exercising.
            study (str): The amount of time in hours spent studying.
            other (str): The amount of time in hours spent doing other tasks.
        Returns:
            Page: Returns the calculate_free_time page.
    '''
    if (not sleep or not eating or not personal_care or not chores
        or not social or not work or not classes or not club
        or not commuting or not exercise or not study or not other ):
        return get_activity_time(state)
    #This will try to set the task to a proper Day
    try: 
        task =Day(select_day,float(sleep),float(eating),float(personal_care),
                                         float(chores),float(social),float(work),float(classes),float(club),
                                         float(commuting),float(exercise),float(study),float(other))
    #If one of the strings can't turn into a float it will prompt the user again and not save the day
    except ValueError:
        return get_activity_time(state)
    #If it passes the code continues as intended
    else:
        
        if select_day == "Sunday":
            state.week_time[0] = task
        if select_day == "Monday":
            state.week_time[1] = task
        if select_day == "Tuesday":
            state.week_time[2] = task
        if select_day == "Wednesday":
            state.week_time[3] = task
        if select_day == "Thursday":
            state.week_time[4] = task
        if select_day == "Friday":
            state.week_time[5] = task
        if select_day == "Saturday":
            state.week_time[6] = task
        return calculate_free_time(state)


assert_equal(save_day(State(False,False,True,0.0,[place_holder,place_holder,
                                                             place_holder,place_holder,place_holder,place_holder,place_holder]),
                      "Monday","4.0","4.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0"),
             Page(State(False,False,True,8.0,[place_holder,Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                                             place_holder,place_holder,place_holder,place_holder,place_holder]),
               [
                change_text_size(bold('Total Free time\n'), "50px"),
                16.0," hours\n",
                Button("Reset","reset")
               ]
             
             
             )
             )
assert_equal(save_day(State(True,False,False,0.0,[
                                              Day("Sunday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              place_holder]),
             "Saturday","4.0","4.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0"),
             Page(State(True,False,False,56.0,[Day("Sunday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Saturday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)]),
               [
                change_text_size(bold('Total Free time\n'), "50px"),
                112.0," hours\n",
                Button("Reset","reset")
               ]
             
             
             )
             )
assert_equal(save_day(State(False,True,False,0.0,[place_holder,
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              place_holder,place_holder]),
                      "Friday","4.0","4.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0"),
             Page(State(False,True,False,40.0,[place_holder,
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Friday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                               place_holder]),
               [
                change_text_size(bold('Total Free time\n'), "50px"),
                80.0," hours\n",
                Button("Reset","reset")
               ]
             
             
             )
             )             
             
assert_equal(save_day(State(False,True,False,0.0,[place_holder,
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)]),
                      "Thursday","4.0","4.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0","0.0"),
                         Page(State(False,True,False,0.0,[place_holder,
                                              Day("Monday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Tuesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Wednesday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("Thursday",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0),
                                              Day("",4.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0)]),

                     [
                        change_text_size(bold('Input answers as "#.#"\n'), "50px"),
                        change_text_size(bold('Day of the week\n'), "25px"),
                        SelectBox("select_day", ["Monday","Tuesday","Wednesday","Thursday","Friday"],
                                  "Monday"),"Hours spent sleeping",
                        TextBox("sleep"),"Hours spent eating",
                        TextBox("eating"),"Hours spent on personal care",
                        TextBox("personal_care"),"Hours spent on chores",
                        TextBox("chores"),"Hours spent socializing",
                        TextBox("social"),"Hours spent at work",
                        TextBox("work"),"Hours spent at classes",
                        TextBox("classes"),"Hours spent at clubs",
                        TextBox("club"),"Hours spent commuting",
                        TextBox("commuting"),"Hours spent exercising",
                        TextBox("exercise"),"Hours spent studying",
                        TextBox("study"),"Hours spent on other tasks",
                        TextBox("other"),
                        Button("Save Day","save_day")
                        
                        
                    ]
             )
            )       

@route
def reset(state:State)->Page:
    '''
        Restarts the application. 

        Args:
            state (State): The current state the file is in.
        Returns:
            Page: Returns the index page.
    '''
    state.is_week = False
    state.is_day = False
    state.is_weekday = False
    state.busy_time = 0.0
    state.week_time = [place_holder,place_holder,place_holder,place_holder,
                                          place_holder,place_holder,place_holder]
    return index(state)
    
assert_equal(reset(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder])),
             Page(State(False,False,False,0.0,
                   [place_holder,place_holder,place_holder,place_holder,
                    place_holder,place_holder,place_holder]),
                [
                    change_text_size(bold("Freetime Tracker\n"), "50px"),
                    Button("One Day","one_day"),
                    Button("Weekdays","weekdays"),
                    Button("Whole Week","whole_week")
                ]
                                                                   )
             )



start_server(State(False,False,False,0.0,[place_holder,place_holder,place_holder,place_holder,
                                        place_holder,place_holder,place_holder]))

