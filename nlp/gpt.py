import os
import openai
import nlp.prompts as prompts

openai.organization = ""
openai.api_key = ""
completion = openai.Completion()

def get_conversation_response(conversation):
    prompt = prompts.prepare_to_converse(conversation)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_conversation_response ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['>'], temperature=0.7,
        prompt=prompt, engine="curie", stop=['>'], temperature=0.7,
        # Added a slight frequency_penalty because the model sometypes quoted the model prompt
        top_p=1, frequency_penalty=0.2, presence_penalty=0, best_of=1,
        # OpenAI's open-ended generation requirement is less than 40 tokens, but for specific
        # chatbots it looks like you can have up to 50 tokens.
        max_tokens=50)
    reply = response.choices[0].text.strip()
    print("-------------------------- completion -------------------------- ")
    print(reply)
    return reply

def is_calendar_related(message):
    prompt = prompts.prepare_is_calendar_related(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ is_calendar_related ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    response = response_str.split(":")[1].strip()
    print("-------------------------- completion -------------------------- ")
    print(response)
    return response


def is_calendar_request(message):
    prompt = prompts.prepare_is_calendar_request(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ is_calendar_request ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()

    response = response_str.split(":")[1].strip()
    print("-------------------------- completion -------------------------- ")
    print(response)
    return response


def is_it_related(message):
    prompt = prompts.prepare_is_it_related(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ is_it_related ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    print(response_str)
    response = response_str.split(":")[1].strip()
    print("-------------------------- completion -------------------------- ")
    print(response)
    return response

def is_project_related(message):
    prompt = prompts.prepare_is_project_related(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ is_project_related ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    response = response_str.split(":")[1].strip()
    print("-------------------------- completion -------------------------- ")
    print(response)
    return response

def get_calendar_request_type(message):
    prompt = prompts.prepare_calendar_request_type(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_calendar_request_type ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    response_arr = response_str.split(":")
    print("-------------------------- completion -------------------------- ")
    print(response_arr)
    calendar_request_type = Calendar_Request.get_type(response_arr[1].strip())
    return calendar_request_type

def get_event_date_sd(message):
    prompt = prompts.prepare_get_date_sd(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_event_date_sd ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=subprompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    date = response_str.split(":")[1].strip()
    date_arr = date.split("/")
    print("-------------------------- completion -------------------------- ")
    print(date_arr)
    month = int(date_arr[0])
    day = int(date_arr[1])

    year = datetime.date.today().year
    date = datetime.datetime(year, month, day, 0, 0, 0)
    return date

def get_event_date_dow(message):
    prompt = prompts.prepare_get_date_dow(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_event_date_dow ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=subprompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    # TODO: solve this in new script
    # if dow == "null":
    #     print("dow is null")
    #     dow = "today"
    response_str = response.choices[0].text.strip()
    date = response_str.split(":")[1].strip()
    date_arr = date.split("/")
    print("-------------------------- completion -------------------------- ")
    print(date_arr)
    month = int(date_arr[0])
    day = int(date_arr[1])
    year = datetime.date.today().year
    date = datetime.datetime(year,month,day,0,0,0)
    return date

def get_event_time(message):
    prompt = prompts.prepare_parse_time(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_event_time ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    print("test")
    print(response_str)
    if response_str.split(":")[1].strip() == "null":
        print("time is null")
        print("setting meeting for 12:00")
        time = "12:00"
    else:
        time = response_str.split(":")[1].strip() + ":" + response_str.split(":")[2].strip()
        time = datetime.datetime.strptime(time, "%I:%M %p")
        time = datetime.datetime.strftime(time, "%H:%M")
    hours = time.split(":")[0].strip()
    minutes = time.split(":")[1].strip()
    time_arr = [hours, minutes]
    print("-------------------------- completion -------------------------- ")
    print(time_arr)
    return time_arr

def get_event_duration(message):
    prompt = prompts.prepare_parse_duration(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_event_duration ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=10)
    response_str = response.choices[0].text.strip()
    print("-------------------------- completion -------------------------- ")
    print(response_str)
    minutes = response_str.split(":")[1].strip()
    minutes = minutes.split(" ")[0].strip()
    return int(minutes)

def get_subject(message):
    prompt = prompts.prepare_parse_subject(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ get_subject ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
            # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
            prompt=prompt, engine="curie", stop=['##'], temperature=0.1,
            top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
            max_tokens=25)
    response_str = response.choices[0].text.strip()
    print("-------------------------- completion -------------------------- ")
    print(response_str)
    subject = response_str.split(":")[1].strip()
    return subject

def filter_signature(message):
    prompt = prompts.prepare_filter_signature(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ filter_signature ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=60)
    response_str = response.choices[0].text.strip()
    print("-------------------------- completion -------------------------- ")
    print(response_str)
    message = response_str.split("|")[1].strip()
    return message

def filter_date(message):
    prompt = prompts.prepare_filter_date(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ filter_date ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=15)
    response_str = response.choices[0].text.strip()
    print("-------------------------- completion -------------------------- ")
    print(response_str)
    date = response_str.split(":")[1].strip()
    return date

def date_is_available(message):
    prompt = prompts.prepare_date_is_available(message)
    print("~~~~~~~~~~~~~~~~~~~~~~ date_is_available ~~~~~~~~~~~~~~~~~~~~~~")
    print("---------------------------- prompt ---------------------------- ")
    print(prompt)
    response = completion.create(
        # prompt=prompt, engine="davinci", stop=['##'], temperature=0,
        prompt=prompt, engine="curie", stop=['##'], temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0, best_of=1,
        max_tokens=15)
    response_str = response.choices[0].text.strip()
    print("-------------------------- completion -------------------------- ")
    print(response_str)

    response = response_str.split(":")[1].strip()

    return response
