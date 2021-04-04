"""
Nathan Yeo
Simple timing program for HIIT workouts
"""
import time
from playsound import playsound


def user_interface():
    default = input("Would you like to use default values? (n_sets = 3, n_exercises = 6, workout_interval_duration = "
                    "45, rest_duration = 15, rest_between_sets_duration = 20) [y/n]: ")
    if default == "n":
        n_sets = int(input("Input number of sets ('quit' to quit): "))                 # number of rounds
        n_exercises = int(input("Input number of exercises per set ('quit' to quit): "))  # number of exercises
        wid = int(input("Input workout interval duration ('quit' to quit): "))         # workout interval duration
        rd = int(input("Input rest duration ('quit' to quit): "))                      # rest duration
        rbsd = int(input("Input rest between sets duration ('quit' to quit): "))       # rest between sets duration
        print(f"You are doing {n_sets} sets of {n_exercises} exercises with {rd} seconds of rest in between each "
              f"exercise. There are {rbsd} seconds of rest between sets.")
    else:
        print(f"You are doing 3 sets of 6 exercises with 15 seconds of rest in between each exercise. "
              f"There are 20 seconds of rest between sets.")
        n_sets = 3

    # 15 second timer before starting
    print("15 seconds before starting workout timer")
    timer(15)

    for i in range(n_sets):
        print(f"SET {i}")
        set_timer(wid, rd, n_exercises)
        rest_set_timer(rbsd)


def set_timer(wid=45, rd=15, n_exercises=6):
    playsound('start.mp3')
    timer(wid)
    for i in range(n_exercises-1):
        # rest timer
        playsound('rest.mp3')
        timer(rd)

        # workout timer
        playsound('start.mp3')
        timer(wid)


def rest_set_timer(rbsd=20):
    playsound('rest.mp3')
    timer(rbsd)


def timer(seconds):
    start = time.time()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        #print(elapsed)
        time.sleep(1)



if __name__ == '__main__':
    user_interface()
    playsound('censor-beep-2.mp3')