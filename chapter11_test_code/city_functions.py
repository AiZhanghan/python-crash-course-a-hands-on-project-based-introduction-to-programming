'''
编写函数，接受两个形参：一个城市名和一个国家名。
返回格式为City, Country的字符串。
'''


def get_formated_city_name(city, country, population=None):
    '''
    返回City, Country的字符串
    '''
    formatted_city_name = city + ', ' + country
    if population:
        res = (formatted_city_name.title() + 
            ' - population '+ str(population))
    else:
        res = formatted_city_name.title()

    return res
