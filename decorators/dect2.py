def capitalize(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper

@capitalize
def morning_greetings():
    return "good morning"

@capitalize
def afternoon_greetings():
    return "good afternoon"

# print(morning_greetings())
# print(afternoon_greetings())


from datetime import datetime
@capitalize
def greeting_bytime():
    current_time=datetime.now()
    current_hour=current_time.hour
    if (5<=current_hour<12):
        return "good morning"
    elif (12<=current_hour<18):
        return "good afternoon"
    else:
        return "good evening"
print(greeting_bytime())