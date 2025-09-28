# Character definitions
define m = Character("[player_name]")
define a = Character("Ashleigh", colour="#5032a8")
define l = Character("Luke", color="#8EB700")
define t = Character("Teacher", color="#FF0000")
define n = Character(None)  # Narrator

#Friendship level
default ashleigh_friendship_level = 50
default luke_friendship_level = 50


# Image backgrounds
image bg_highschool = im.Scale("bg highschool.jpeg", 1920, 1080)
image bg_classroom = im.Scale("bg classroom.jpeg", 1920, 1080)
image bg_hallway = im.Scale("bg hallway.jpeg", 1920, 1080)
image bg_park = im.Scale("bg park.jpeg", 1920, 1080)
image bg_carcrash = im.Scale("bg carcrash.jpeg", 1920, 1080)

#Character sprites
image ashleigh normal = im.Scale("ashleigh normal.png", 1100, 1080)
image luke normal = im.Scale("luke normal.png", 1100, 1080)

transform ashleigh_left:
    xalign 0.0
    yalign 1.0

transform luke_right:
    xalign 1.0
    yalign 1.0

# Optional splash/prologue
label splashscreen:
    n "There are moments when the world asks you to choose..."
    n "This is one of them..."
    n "Choose wisely..."
    return

# The game starts here
label start:

    $ player_name = renpy.input("What is your name?", length=20)
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "Me"

    # Show a background
    scene bg_highschool
    show screen friendship_bar
    with fade

    # Dialogue sequence
    n "You arrive at school early, waiting for your friends Ashleigh and Luke to show up."
    m "Where are they?"
    m "*Sigh*"
    n "You check your watch. They're late."

    menu:
        "Wait for them":
            $ waited = True
            jump wait_for_them_scene

        "Ditch them and go to class":
            $ waited = False
            jump ditch_them_scene

# Scene: Waiting for them
label wait_for_them_scene:
    m "Guess I'll wait for them."
    n "After several hours, Ashleigh and Luke arrive."
    show ashleigh normal at ashleigh_left
    show luke normal at luke_right
    a "*Glares at Luke*"
    l "What? I didn't do anything!"
    a "Sorry we're late. Somebody took too long..."
    n "*Ashleigh glares at Luke again*"
    l "Hey! It wasn't my fault!"
    n "The two bicker back and forth." 
    m "*Laughs*" 
    m "You two never change, do you?"
    m "Come on, let's head inside before we're late for class."

    n "Your choices impact your character"

    menu:
        "Walk with Ashleigh to class":
            $ walked_with_ashleigh = True
            $ walked_with_luke = False
            jump walk_with_ashleigh_scene

        "Walk with Luke to class":
            $ walked_with_luke = True
            $ walked_with_ashleigh= False
            jump walk_with_luke_scene
            

# Scene: Walking with Asheigh
label walk_with_ashleigh_scene:
    scene bg_hallway
    show ashleigh normal at ashleigh_left
    show luke normal at luke_right
    $ ashleigh_friendship_level += 2
    n "Your friendship level with Ashleigh is now [ashleigh_friendship_level]."
    n "Ashleigh chats happily as you walk together."
    n "*Luke follows silently trailing behind*"
    n "*Ashleigh talks about the class project and her plans*"
    n "You tune out"
    m "*Lost in your thoughts*"
    m "*Ashleigh can be so full of herself sometimes...*"
    n "Ashleigh interrupts your thoughts"
    a "Sorry about Luke, [player_name]. He can be such a pain sometimes."
    m "*Huh?* Oh... Yeah he can be sometimes.."
    n "You desperately wish for an awkward situation"
    n "You arrive at class."
    scene bg_classroom
    m "*Finally. A way to get out of that conversation.*"
    n "You enter the classroom."
    hide ashleigh
    m "Who do I sit with?"
    n "Your choices impact your character"

    menu:
        "Sit with Ashleigh":
            $ sit_with_ashleigh = True
            $ sit_with_luke= False
            jump sit_with_ashleigh_scene

        "Sit with Luke":
            $ sit_with_luke = True
            $ sit_with_ashleigh = False
            jump sit_with_luke_scene

# Scene: Sitting with Ashleigh
label sit_with_ashleigh_scene:
    scene bg_classroom
    show ashleigh normal at ashleigh_left
    show luke normal at luke_right
    $ ashleigh_friendship_level += 2
    n "Your friendship level with Ashleigh is now [ashleigh_friendship_level]."
    n "You sit with Ashleigh."
    n "Luke seems jealous."
    l "*Looks away*"
    n "*Ashleigh nudges you*"
    n "You ignore her"
    a "I know you're ignoring me, don't bother trying."
    m "What do you want Ashleigh?"
    a "If you didn't want to sit with me, you should've just sat with my brother instead."
    m "Fine, do you want the truth?"
    m "I never like you anyways."
    m "I like spending time with your brother over you."
    a "DON'T EVER TALK WITH ME EVER AGAIN!"
    a "*Storms outside angrily"
    hide ashleigh
    l "Well, that was... dramatic."
    $ ashleigh_friendship_level -= 55
    hide luke
    scene black
    n "Wow, you ended a friendship over a stupid argument."
    n "At least you got Luke."
    return

# Scene: Sitting with Luke  
label sit_with_luke_scene:
    scene bg_classroom
    $ luke_friendship_level += 2
    n "Your friendship level with Luke is now [luke_friendship_level]."
    n "You sit with Luke."
    n "Ashleigh seems annoyed."
    n "*Ashleigh mutters something under her breath*"
    l "Wana to go to the park after school?"
    m "Can Ashleigh go?"
    l "*Deadpans* She's my sister we go eveywhere."
    m "Right..."
    m "Sure, lets go after school."
    n "Class starts"
    t "Yap, yap, yap, yapping all class isn't going to get you anywhere."
    n "You try to focus on the lesson but your mind wanders."
    n "Finally, class ends."
    n "Everybody leaves class chattering excitedly."
    n "Magically spawns at the park"
    scene bg_park
    show luke normal at luke_right  
    show ashleigh normal at ashleigh_left
    n "You arrive at the park with Luke and Ashleigh."
    a "Why do you always get to spend time with [player_name]?"
    l "Maybe if you weren't so annoying, [player_name] would want to spend more time with you."
    a "Shut up Luke."
    n "The two bicker back and forth."
    m "*Sigh*"
    m "Can we just enjoy the park?"
    n "The two stop bickering for a moment."
    n "Ashleigh and Luke ask at the same time. Who do you like better?"
    n "Your choices impact your character"

    menu:
        "Side with Ashleigh":
            $ side_with_ashleigh = True
            $ side_with_luke = False
            jump side_with_ashleigh_scene

        "Side with Luke":   
            $ side_with_luke = True
            $ side_with_ashleigh = False
            jump side_with_luke_scene


# Scene: Side with Ashleigh 
label side_with_ashleigh_scene:

    n "You side with Ashleigh." 
    $ ashleigh_friendship_level += 2
    $ luke_friendship_level -= 5    
    a "Thank you [player_name], I knew you were a good person."
    n "Luke looks disappointed."
    l "Whatever..."
    n "The two bicker back and forth."
    m "*Sigh*"
    m "Can't we just all get along"
    n "In unison: NO!"
    n "The two continue bickering."
    scene black
    n "You leave the park feeling like a mediator."
    n "At least Ashleigh likes you more now"
    return

# Scene: Side with Luke
label side_with_luke_scene:
    n "You side with Luke." 
    $ luke_friendship_level += 2
    $ ashleigh_friendship_level -= 2    
    l "Thanks [player_name]. *Flushes*"
    n "Ashleigh glares once more."
    a "Whatever..."
    n "Ashleigh storms off"
    hide ashleigh
    m "*Sigh*"
    m "Now what?Y our sister just stormed off"
    l "She'll be fineeeeee. I guess we'll just enjoy the park?"
    n "You and Luke enjoy the park."
    n "Suddenly, you hear a bloodcurdling scream from the distance."
    n "*Screaming heard in the distance*"
    a "AHHHHHHHHHHHHHHHHHHHHHHHH!!!"
    l "ASHLEIGH?!!!!!"
    n "You and Luke run towards the scream."
    n "A car is coming towards Ashleigh."
    scene bg_carcrash
    show ashleigh normal at ashleigh_left
    n "You are presented with a choice"
    
    menu:
        "You sacrifice yourself and push Ashleigh out of the way":
            $push_ashleigh_out_of_the_way = True
            $ luke_pushes_ashleigh_out_of_the_way = False
            
            jump push_ashleigh_out_of_the_way_scene
    
        "Luke sacrifices himself and pushes Ashleigh out of the way":
            $ luke_pushes_ashleigh_out_of_the_way = True
            $ push_ashleigh_out_of_the_way = False
            jump luke_pushes_ashleigh_out_of_the_way_scene

# Scene: Sacrifice yourself
label push_ashleigh_out_of_the_way_scene:
    scene black
    n "You push Ashleigh out of the way, but you get hit by the car."
    n "You end up in hospital, but you don't know if you survive or not."
    n "To be contuined..."
    return

# Scene: Luke sacrifices himself
label luke_pushes_ashleigh_out_of_the_way_scene:
    scene black
    n "Luke pushes Ashleigh out of the way, but he gets hit by the car."
    n "He ends up in hospital, but you don't know if he survives or not."
    n "All because of a stupid argument, you end up in this predicument."
    n "To be contuined..."
    return


    

# Scene: Walking with Luke
label walk_with_luke_scene:
    scene bg_hallway
    show luke normal at luke_right
    show ashleigh normal at ashleigh_left
    $ luke_friendship_level += 2
    n "Your friendship level with Luke is now [luke_friendship_level]."
    n "You walk with Luke."
    n "Ashleigh seems annoyed."
    a "I'm going to go to class, meet you guys there..."
    a "*Walks away*"
    hide ashleigh
    m "*Sigh*"
    l "C'mon let's get to class."
    n "You and Luke arrive at class."
    scene bg_classroom
    m "Who do I sit with?"
    n "Your choices impact your character"

    menu:
        "Sit with Ashleigh":
            $ sit_with_ashleigh = True
            $ sit_with_luke= False
            jump sit_with_ashleigh_scene

        "Sit with Luke":
            $ sit_with_luke = True
            $ sit_with_ashleigh = False
            jump sit_with_luke_scene
    

# Scene: Ditching them
label ditch_them_scene:
    m "I can't wait around all day. I'm going to class."
    n "You head to class alone."
    n "You ditched your friends."
    n " Wow, you really are a piece of work."
    return
