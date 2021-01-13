from django import template  
  
register = template.Library()  

@register.simple_tag  
def find_out_free_time(booking_table, workplace):
    default_times = list(range(8, 19))
    for el in booking_table:
        # print(default_times)
        if el.workplace == workplace:
            time_from = default_times.index(int(el.datetime_from))
            time_to = default_times.index(int(el.datetime_to))
            del default_times[time_from : 1 : time_to]
            # time_from = default_times.index(int(el.datetime_from))
            # if time_from == 0:
            #     times_from = default_times[: time_from]  
            # else:
            #     times_from = default_times[: time_from]                       
            # times_to = default_times[default_times.index(int(el.datetime_to)):]
            # default_times = times_from + times_to
    return default_times
  
  
# def find_out_free_time():
#     default_times = list(range(8, 18))
#     print(default_times)
#     if
#     times_from = default_times[:default_times.index(10)]
#     times_to = default_times[default_times.index(12):]
#     default_times = times_from + times_to
#     return default_times

# print(find_out_free_time())

