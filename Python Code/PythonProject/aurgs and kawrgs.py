def intro(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is {value}")


person = {'Name':'Hasnain','Gender':'Male'}
intro(**person)

intro(Name ='hasnain', Gender='male', Weight = '75')