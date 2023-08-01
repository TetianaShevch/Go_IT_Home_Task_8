from datetime import datetime, date, timedelta

days_of_week = {
    0:'Monday',
    1:'Tuesday',
    2:'Wednesday',
    3:'Thursday',
    4:'Friday',
    5:'Saturday',
    6:'Sunday'
}

def get_birthdays_per_week(users:list)->None:
    '''
    Функція get_birthdays_per_week друкує список колег, яких треба привітати із днем народження на тиждень вперед 
    від поточного дня.
    
    Функція приймає як параметр список словників (users:list), ключами яких є ім'я колеги (name) і його день народження 
    у вигляді строки "YYYY-mm-dd" (birthday). ВНагадування виводиться у вигляді переліку "День тижня - перелік імен іменинників". 
    Якщо день народження припадає на вихідні, нагадування про це буде в наступний понеділок. 
    Дні тижня, в які немає іменинників, не виводяться.   
    '''
     
    today = date.today()
    year_now = today.year
    
    for i in range(7):
        list_of_birthday = []
        for us in users:
            for name in us:
                birthday = datetime.strptime(us[name], "%Y-%m-%d")
                birthday = birthday.date()
                birthday = birthday.replace(year=year_now)
                birthday = birthday + timedelta(days = 2) if birthday.weekday() == 5 else birthday + timedelta(days = 1) if birthday.weekday() == 6 else birthday
                
                if today == birthday:
                    list_of_birthday.append(name)
                                        
        if list_of_birthday:
            day_of_week = today.weekday()
            
            print(f'{days_of_week[day_of_week]}:',end=' ')
            for j in list_of_birthday:
                print(j,end=' ')
            print()
        today = today + timedelta(days = 1)
        i += 1
    