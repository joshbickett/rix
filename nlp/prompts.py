import datetime


# I was considering using prepare_filter_signature() on each conversation element, but decided not to.
# These is actually an exceedingly hard problem, because each element of the conversation is parsed repeatedly
# with each new message appended to the conversation. I think I would ultimately need to save each conversation
# in the database and keep a separate version to reference.
# For the time being I think I'll just use prepare_filter_signature() on messages for other functions to get
# clearer and simplier message prompts
def prepare_to_converse(conversation):
    prepared_conversation = conversation + conversation + ">Your assistant says:"
    prompt = prepared_conversation
    return prompt

def prepare_is_calendar_related(message):
    prompt = is_calendar_related + '"' + message + '"'
    return prompt

def prepare_is_calendar_request(message):
    prompt = is_calendar_request + '"' + message + '"'
    return prompt

def prepare_is_it_related(message):
    prompt = is_it_related + '"' + message + '"'
    return prompt

def prepare_is_project_related(message):
    prompt = is_project_related + '"' + message + '"'
    return prompt

def get_week():
    week = ""
    for i in range(0,7):
        date = datetime.date.today() + datetime.timedelta(days=i)
        date_str = date.strftime("%m/%d")
        dow = date.strftime('%A')
        if i == 0:
            week += dow + " " + date_str + " (today)\n"
        else:
            week += dow + " " + date_str + "\n"

    week += "\n"
    return week

def append_week(prompt):
    prompt = prompt + get_week()
    return prompt

def prepare_get_date_dow(message):
    prompt = append_week(get_date_dow) + '"' + message + '"'
    return prompt

def prepare_get_date_sd(message):
    prompt = get_date_sd + '"' + message + '"'
    return prompt


def prepare_calendar_request_type(message):
    prompt = calendar_request_type + '"' + message + '"'
    return prompt

def prepare_parse_time(message):
    prompt = parse_time + '"' + message + '"'
    return prompt

def prepare_parse_duration(message):
    prompt = parse_duration + '"' + message + '"'
    return prompt


def prepare_parse_subject(message):
    prompt = parse_subject + '"' + message + '"'
    return prompt

def prepare_filter_signature(message):
    prompt = filter_signature + '"' + message + '"'
    return prompt

def prepare_filter_date(message):
    prompt = filter_date + '"' + message + '"'
    return prompt

def prepare_date_is_available(message):
    prompt = date_is_available + '"' + message + '"'
    return prompt

# TODO: wait for the google record to update.
# If these general use cases can not be approved, we can focus on startups. Startup ideas, startup projects, and calednars.
conversation ='''
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and friendly. The assistant excellent at creating project ideas, sharing information technology knowledge, and managing the user's calendars. 

The assistant does not have access to any personal data and protects user privacy.  

>Your assistant says:
Hello, I am your assistant. Let me know how I can help. 
'''

is_calendar_related = '''
The following classifies if a message is related to the calendar or events.  "Yes" if it is related to the calendar or events and "No" if it is not.

"Hi, I actually need to meet with them tomorrow. Can you send me a calendar for that time?"
Calendar related: Yes
###
"The weather is great out there today. Wonder what the temperature is."
Calendar related: No
###
"Where is the event? Please send me the details."
Calendar related: Yes
###
"Let's get started today."
Calendar related: Yes
###
"How about we go tomorrow? Can you send the event details?"
Calendar related: Yes
###
"Can you send Jeff the calendar for tomorrow?"
Calendar related: Yes
###
"What day is it today?"
Calendar related: Yes
###
"Is there an event for this? "
Calendar related: Yes
###
"That sounds cool. What this the total mass of the rocket engine?"
Calendar related: No
###
"Well how about that? Let's schedule a time for it"
Calendar related: Yes
###
"What is the software development life cycle?"
Calendar related: No
###
"The QA testing looks good. How long until we release the product?" 
Calendar related: No
###
"How about we meet sunday at 2 PM?" 
Calendar related: Yes
###
"Do you have any good project ideas? I am trying to get into agile development. " 
Calendar related: No 
###
"What is HTML?" 
Calendar related: No
###
"Let's go to the beach tomorrow. Please send an invite for tomorrow at 1 PM" 
Calendar related: Yes
###
"Hi, can you help me with something?"
Calendar related: No
###
'''

is_calendar_request = '''
The following classifies if a message requests a calendar invite.  "Yes" if it is requests an invite and "No" if it is not.

"Hi, I actually need to meet with them tomorrow. Can you send me a calendar for that time?"
Calendar request: Yes
###
"What day is it today"
Calendar request: No
###
"Let's get started today."
Calendar request: No
###
"How about we go tomorrow? Can you send the event details?"
Calendar request: No
###
"Can you send Jeff the calendar for tomorrow?"
Calendar request: Yes
###
"Is there an event for this? "
Calendar request: No
###
'''

is_it_related = '''
The following classifies if a message is related to information technology (IT). "Yes" if a conversation is related to IT knowledge and "No" if it is not.

"Hi, I actually need to meet with them tomorrow. Can you send me a calendar for that time?"
IT knowledge related: No
###
"What is HTML?"
IT knowledge related: Yes
###
"Is the world round? I'd love to know more about if it is."
IT knowledge related: No
###
"How should I work on connecting my networks? Do you know any good products?"
IT knowledge related: Yes
###
"How many pixels are on my computer screen?"
IT knowledge related: Yes
###
"Can you send me a calendar for 4 PM on Saturday? Call it meeting on Space future"
IT knowledge related: No
###
"Can you send me a calendar for 4 PM on Saturday? Call it meeting on AI future"
IT knowledge related: No
###
"Can you direct me to good cloud hosting websites?"
IT knowledge related: Yes
###
"What is a website?"
IT knowledge related: Yes
###
"How far away is Mars?"
IT knowledge related: No
###
"How do I get a job in software development?"
IT knowledge related: Yes
###
"How do I get a job in accounting?"
IT knowledge related: No
###
"What is a newspaper? Any good examples? "
IT knowledge related: No
###
"Who is Benjamin Franklin? I am curious if he did anything meaningful."
IT knowledge related: No
###
"What is the difference between javascript and java?"
IT knowledge related: Yes
###
"How many computers were existing in 1945?"
IT knowledge related: Yes
###
"Can we go check out the backyard fence? I think it needs some work"
IT knowledge related: No
###
"Can you explain what AWS is?"
IT knowledge related: Yes
###
"What's the difference between an internet browser and a website?"
IT knowledge related: Yes
###
"What are some good food recipes?"
IT knowledge related: No
###
"Do you provide medical advise?"
IT knowledge related: No
###
"What's the weather like in Austin, Texas tomorrow?"
IT knowledge related: No
###
"How is Javascript different than Java/"
IT knowledge related: Yes
###
'''

is_project_related = '''
The following classifies if a message is related to work and business projects. "Yes" if a conversation is related to work and business projects and "No" if it is not.

"Hi, I actually need to meet with them tomorrow. Can you send me a calendar for that time?"
Related to projects: No
###
"What is HTML?"
Related to projects: No
###
"Yea, I like that idea"
Related to projects: Yes
###
"How can I make this project work? Any ideas?"
Related to projects: Yes
###
"How many pixels are on my computer screen?"
Related to projects: no
###
"Hi, can you help with a project idea?"
Related to projects: Yes
###
"What is the the micro processor?"
Related to projects: No
###
"How do I get a software engineering job?"
Related to projects: No
###
"We are going to get a business grant, have any ideas on how to do that?"
Related to projects: Yes
###
"What is a good idea for a startup?"
Related to projects: Yes
###
"Can you teach me a good cooking recipe?"
Related to projects: No
###
"Can you share some medical advise?"
Related to projects: No
###
"I am working on a marketing website. Do you have any ideas on a good feature that uses AI?"
Related to projects: Yes
###
"Do you have any advise on what projects for our restaurant to try?"
Related to projects: Yes
###
'''

calendar_request_type = '''
Please categorize calendar messages into a "day of week" type or "specific date" type based on the context. If the message references a specific date such as April 2 then it is always a specific date type. 

###
"5/28"
Type: specific date
###
"Monday"
Type: day of week
###
"August 27th"
Type: specific date
###
"Sep. 5th"
Type: specific date
###
"August 27th"
Type: specific date
###
"Tomorrow"
Type: day of week
###
"Tuesday"
Type: day of week
###
"July 10th"
Type: specific date
###
"November 13th"
Type: specific date
###
"Tuesday"
Type: day of week
###
"today"
Type: day of week
###
'''

# I am having to use davinci, because even with adding a larger prompt with more examples, curie is not getting it.
get_date_dow = '''
Please choose the calendar date by reading the message. Today's date is the first date in the calendar. 

Calendar: 
Tuesday 02/16 (today)
Wednesday 02/17
Thursday 02/18
Friday 02/19
Saturday 02/20
Sunday 02/21
Monday 02/22

"Saturday"
Event date: 02/20
###
"Monday"
Event date: 02/22
###
"today"
Event date: 02/16
###
"Thursday"
Event date: 02/18
###
"tomorrow"
Event date: 02/17
###
----

Calendar:
Monday 05/17 (today)
Tuesday 05/18
Wednesday 05/19
Thursday 05/20
Friday 05/21
Saturday 05/22
Sunday 05/23

"Sunday"
Event date: 05/23
###
"today"
Event date: 05/17
###
"Wednesday"
Event date: 05/19
###
"Friday"
Event date: 05/21
###
----

Calendar:
Friday 08/28
Saturday 08/29
Sunday 08/30
Monday 08/31
Tuesday 09/01
Wednesday 09/02
Thursday 09/03

"today"
Event date: 08/28
###
"Tuesday"
Event date: 09/01
###
"Wednesday"
Event date: 09/02
###
"tomorrow"
Event date: 08/29
###
----

Calendar:
Friday 01/21 (today)
Saturday 01/22
Sunday 01/23
Monday 01/24
Tuesday 01/25
Wednesday 01/26
Thursday 01/27

"tomorrow"
Event date: 01/22
###
"Today"
Event date: 01/21
###
----

Calendar:
Thursday 04/07 (today)
Friday 04/08
Saturday 04/09
Sunday 04/10
Monday 04/11
Tuesday 04/12
Wednesday 04/13

"Monday"
Event date: 04/11
###
"tomorrow"
Event date: 04/08
###
"sunday"
Event date: 04/10
###
----

Calendar:
Thursday 07/01 (today)
Friday 07/02
Saturday 07/03
Sunday 07/04
Monday 07/05
Tuesday 07/06
Wednesday 07/07

"tomorrow"
Event date: 07/02
###
"today"
Event date: 07/01
###
"monday"
Event date: 07/05
###
----

Calendar:
'''


get_date_sd = '''
Please choose the calendar date by reading the message.

"September 2nd"
Event date: 09/02
###
"nov. 5th"
Event date: 11/05
###
"November 19th"
Event date: 11/19
###
"March 21"
Event date: 03/21
###
"December 23rd"
Event date: 12/23
###
"Feb. 17th"
Event date: 02/17
###
'''

# While dow and sd may require different models I think getting time may only need one.
parse_time = '''
Choose the event time in UTC by reading the message. It is important to choose correctly. It is important to pay attention to "am" and "pm" to select the correct time.

"How about on Friday at 3 PM"
Event time: 03:00 PM
###
"Let's go to the lake at 10:30 AM"
Event time: 10:30 AM
### 
"I am available at 2 pm"
Event time: 02:00 PM
### 
"Friday at 8:25 AM"
Event time: 08:25 AM 
###
"Not until Monday at 9:10 pm"
Event time: 09:10 PM
###
"Please send a calendar for 5 pm on Wednesday to meet with Thomas, Jess, and Mark." 
Event time: 05:00 PM
### 
"Let's plan for that at 2 p and we can go to dinner after. Thanks
Josh" 
Event time: 02:00 PM
### 
"1 pm works, let's plan on that! I can schedule it with the venue"
Event time: 01:00 PM
###
"can you send a calendar for July 7th to meet up with Kyle at Sora Sushi at
12:30 PM?" 
Event time: 12:30 PM
###
"That sounds great. I am not sure why that is.  Let's schedule for Friday March 26th at 6PM" 
Event time: 06:00 PM
###
"Thanks, how about tomorrow for 2 pm? Let's call it Testing"
Event time: 02:00 PM
'''

# returns duration in minutes
parse_duration = '''
Choose the event duration by reading the message.  All event durations should be listed in minutes. When an event duration is not provided default to 30 minute meetings. It is important to choose correctly.

"How about on Friday at 3 PM for 30 minutes? "
Event Duration: 30 minutes
###
"We can meet Monday at 10 am for 10 mins"
Event Duration: 10 minutes
### 
"I was thinking on thursday for an hour"
Event Duration: 60 minutes
### 
"It looks like it will be Monday the 5th for 2 hours"
Event Duration: 120 minutes
###
"how about for an hour?" 
Event Duration: 60 minutes
###
"Monday Sep. 5th at 2 pm works. Let's meet for 15 min"
Event Duration: 15 minutes
###
"Tuesday sounds good"
Event Duration: 30 minutes
###
"It will be at 1 o'clock I think, but may be be at 2 pm"
Event Duration: 30 minutes
###
"Let's go at 5 PM, we may be there an hour. I am not sure how why the weather will be so hot. I guess we will just deal with it."
Event Duration: 60 minutes
###
"Can you send me a calendar for Friday July 2nd? please make it for 5 pm and last for 3 hours. "
Event Duration: 180 minutes
###
"4 hours"
Event Duration: 240 minutes
###
"5 hours"
Event Duration: 300 minutes
###
"This will be a long meeting. Can you schedule it for 3 hours? It will be Friday at 10 am. "
Event Duration: 180 minutes
###
"That works for me. 4 hours will do"
Event Duration: 240 minutes
###
"Yea, it may take up to 5 hours. Let's add it to the calendar for Friday at 10 AM"
Event Duration: 300 minutes
###
"Sometimes yes, Will two hours be ok?"
Event Duration: 120 minutes
###
"Five hours?! Sure. Let's schedule it for 10 am to get an early start. Plus we have to drive. Let's call it Snowboard trip."
Event Duration: 300 minutes
###
"ok, let's schedule a meeting for tomorrow morning at 10 am to talk about it. The meeting can be for 2 hours."
Event Duration: 120 minutes
###
"Can you send me a calendar for July 6th? It should be at be for 4 PM that day. Title it Arrive from Rogue river."
Event Duration: 30 minutes
###
"Let's plan for November 3rd at 9 PM. How does that work for you? We can call it Family gathering. It will last 2 hours"
Event Duration: 120 minutes
###
'''


parse_subject = '''
Please choose the event subject by reading the message. If unsure of the subject, choose "meeting". 

"Let's go to the river to catch some fish tomorrow at 5 PM"
Subject: Go to river
###
"Let's meet with marketing at 7 pm on Friday for the outbound campaign"
Subject: Marketing meeting
### 
"Friday we are going to go to the Zoo with family."
Subject: Go to Zoom
###
"How about Wednesday at 3 pm? "
Subject: Meeting
### 
"Catch the train Friday at 6 pm to go to dinner"
Subject: Catch the train
###
"Let's go a 2 pm"
Subject: Meeting
###
"We can plan to see the game at 1 pm on Saturday and get beers."
Subject: See the game
###
"Let's do that but at 1 pm"
Subject: Meeting
###
"Yea, floating the river sounds good let's go at 1 pm"
Subject: Floating the river
###
"Make appointment for the dentist on Friday"
Subject: Appointment
###
"Let's see, we can try on Monday at 2 PM"
Subject: Meeting
###
"We went to the zoo. Now we would like to go to Portland for the market at 1 pm on Wed."
Subject: Go to Portland
###
"Please send us a calendar to talk on Friday from 2pm to 4 pm. Call the
calendar Marketing Meeting"
Subject: Marketing Meeting
###
"We will stay up for this. I can pick you up from the airport at 1 PM"
Subject: Airport pick up
###
"Assistant, please check their calendars and find mutual availability. Please schedule the meeting and call it QA testing."
Subject: QA testing
###
"can you send a calendar for July 7th to meet up with Kyle at Sora Sushi at 12:30 PM?"
Subject: Meet Kyle at Sora Sushi
###
"How about tuesday at 1 PM? Let's call the calendar, Getting off the river."
Subject: Getting off the river
###
'''

filter_signature = '''
Please filter out the email signature from the following messages.

Original message|
"Hi, I actually need to meet with them tomorrow. Can you send me a calendar for that time?

Tom Cel
Email: tom@gmail.com 
Phone: 301-203-1209"

Filtered message|
Hi, I actually need to meet with them tomorrow. Can you send me a calendar for that time?
###
Original message|
"How are you?

Carle Palin
Founder
E: Carle@timber.com | C: 100-129-1201
Linkedin <https://www.linkedin.com/in/Carle-4219b166/>
https://timber.com/
<https://timber.com/>"

Filtered message|
How are you?
###
Original message|
"Assistant, please check their calendars and find mutual availability. Please schedule the meeting and call it QA testing.
Bijak Plon
Analysis
Email Bijak@oncewasis.com
Cellphone: 800-129-1201
Personal website: https://oncewasis.com/"

Filtered message|
Assistant, please check their calendars and find mutual availability. Please schedule the meeting and call it QA testing.
###
Original message|
"We went to the zoo. Now we would like to go to Portland for the market at 1 pm on Wed. There is a lot to do at the zoo. 

Sometimes I want to go to the zoo more often, but I guess I've got to work. :(

Jimmy Page
714-301-2390"

Filtered message|
We went to the zoo. Now we would like to go to Portland for the market at 1 pm on Wed. There is a lot to do at the zoo. 
Sometimes I want to go to the zoo more often, but I guess I've got to work. :(
###
Original message|
"hi, how are you?"

Filtered message| 
hi, how are you
###
Original message|
"what should we do today?? How about the golf course!

Best, Josh"

Filtered message| 
what should we do today?? How about the golf course!
###
Original message|
'''

filter_date = '''
Please select the date from the messages. If the message includes a day of the week and a calendar date, default to choosing the calendar date with the month and date information. 

###
"Hey, can you send me a calendar for next Tuesday at 3 pm? We need to talk about the business."
Date: Tuesday
###
"How about 5/28 at 2 pm?"
Date: 5/28
###
"Does monday work for you?"
Date: Monday
###
"I can go tomorrow at 5 pm if that works for you."
Date: Tomorrow
###
"Let's go on Friday August 27th"
Date: August 27th
###
"Can you send me a calendar for Monday Sep. 5th?"
Date: Sep. 5th
###
"Please send a calendar for next Tuesday at 2 PM to discuss the acquisition"
Date: Tuesday
###
"Can we meet next Wednesday the Feb. 17th at 1 PM to talk about the weather?"
Date: Feb. 17th
###
"How is about on July 10th?"
Date: July 10th
###
"Let's go with November 13th at 10 pm. Can you schedule that? "
Date: November 13th
###
"July 1"
Date: July 1
###
"Feb. 19th 2021"
Date: Feb. 19th
###
"Tuesday works for me. Please go ahead and schedule it for 1 pm and name it project meeting."
Date: Tuesday
###
"That won't work. How about on Dec. 13th"
Date: Dec. 13th
###
"let's go with Sunday September 3rd at 1PM for 2 hours. You can call the meeting Brain storming."
Date: September 3rd
###
"Please send me a calendar for tomorrow."
Date: tomorrow
###
"Let's plan it for April 1st, that sounds like a good day."
Date: April 1st
###
"Hey, can you send me a calendar for tomorrow?"
Date: tomorrow
###
"Ok, please send me a calendar for 5 PM today to Pick up my truck"
Date: today
###
"How about March 1st at 9 am. We can go to the parkk"
Date: March 1st
###
"tomorrow or today at 1 pm works for me. 42060:)"
Date: tomorrow
###
'''

date_is_available = '''
Please check if date information is available. 

###
"Hey, can you send me a calendar for next Tuesday at 3 pm? We need to talk about the business."
Date available: TRUE
###
"How about 5/28 at 2 pm?"
Date available: TRUE
###
"How about sending a calendar?"
Date available: FALSE
###
"Tuesday works for me. Please go ahead and schedule it for 1 pm and name it project meeting."
Date available: TRUE
###
"Please send me a calendar"
Date available: FALSE
###
"Let's plan it for April 1st, that sounds like a good day."
Date available: TRUE
###
"Hey, can you send me a calendar for tomorrow?"
Date available: TRUE
###
"Ok, please send me a calendar for 5 PM today to Pick up my truck."
Date available: TRUE
###
"What about Tuesday?"
Date available: TRUE
###
"That works, please send me a calendar"
Date available: FALSE
###
"Let's plan it for April 1st, that sounds like a good day."
Date available: TRUE
###
"let's plan for that"
Date available: FALSE
###
"let's plan for that"
Date available: FALSE
###
"how about march 25"
Date available: TRUE
###
"how about march 25"
Date available: TRUE
###
"Let's complete that task"
Date available: FALSE
###
"Let's send the calendar for today over gmail."
Date available: TRUE
###
'''
