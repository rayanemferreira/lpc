from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

for x in range(3):
    print(f'{3 - x}...')
    time.sleep(1)

for x in range(3):
    keyboard.type(f'''test{x}
    According to all known laws 
of aviation,


there is no way a bee
should be able to fly.

Its wings are too small to get
its fat little body off the ground.


The bee, of course, flies anyway


because bees don't care
what humans think is impossible.


Yellow, black. Yellow, black.
Yellow, black. Yellow, black.


Ooh, black and yellow!
Let's shake it up a little.


Barry! Breakfast is ready!


Ooming!


Hang on a second.


Hello?


- Barry?
- Adam?


- Oan you believe this is happening?
- I can't. I'll pick you up.


Looking sharp.


Use the stairs. Your father
paid good money for those.


Sorry. I'm excited.


Here's the graduate.
We're very proud of you, son.


A perfect report card, all B's.


Very proud.


Ma! I got a thing going here.


- You got lint on your fuzz.
- Ow! That's me!


- Wave to us! We'll be in row 118,000.
- Bye!


Barry, I told you,
stop flying in the house!


- Hey, Adam.
- Hey, Barry.


- Is that fuzz gel?
- A little. Special day, graduation.


Never thought I'd make it.


Three days grade school,
three days high school.


Those were awkward.


Three days college. I'm glad I took
a day and hitchhiked around the hive.


You did come back different.


- Hi, Barry.
- Artie, growing a mustache? Looks good.


- Hear about Frankie?
- Yeah.


- You going to the funeral?
- No, I'm not going.


Everybody knows,
sting someone, you die.


Don't waste it on a squirrel.
Such a hothead.


I guess he could have
just gotten out of the way.


I love this incorporating
an amusement park into our day.


That's why we don't need vacations.


Boy, quite a bit of pomp...
under the circumstances.


- Well, Adam, today we are men.
- We are!


- Bee-men.
- Amen!


Hallelujah!


Students, faculty, distinguished bees,


please welcome Dean Buzzwell.


Welcome, New Hive Oity
graduating class of...


...9:15.


That concludes our ceremonies.


And begins your career
at Honex Industries!


Will we pick ourjob today?


I heard it's just orientation.


Heads up! Here we go.


Keep your hands and antennas
inside the tram at all times.


- Wonder what it'll be like?
- A little scary.


Welcome to Honex,
a division of Honesco


and a part of the Hexagon Group.


This is it!


Wow.


Wow.


We know that you, as a bee,
have worked your whole life


to get to the point where you
can work for your whole life.


Honey begins when our valiant Pollen
Jocks bring the nectar to the hive.


Our top-secret formula


is automatically color-corrected,
scent-adjusted and bubble-contoured''')

# from pynput.mouse import Button, Controller
# import time

# mouse = Controller()

# for x in range(5):
#     print(f'{5-x}...')
#     time.sleep(1)

# for x in range(500):
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     time.sleep(0.01)