def month(month_number, language):
    if month_number < 1 or month_number > 12:
        return "Некорректный номер месяца"
    months = {
        'ru': [
            "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ],
        'en': [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    }
    return months[language][month_number - 1]

print(month(1, 'ru'))  