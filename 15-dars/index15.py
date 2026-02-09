# *args
# def sum(*nums):
#     '''Kiritilgan sonlar yig'indisini hisoblaydigan funksiya'''
#     yigindi = 0
#     for num in nums:
#         yigindi += num
#     return yigindi

def sums(*nums):
    '''Kiritilgan sonlar yig'indisini hisoblaydigan funksiya'''
    return sum(nums)

print(sums(1.2,10.3))

# **kwargs
def avto_info(comp, model, **infors):
    '''Avtomobil haqidagi funksiya'''
    infors['comp'] = comp
    infors['model'] = model
    return infors

avto = avto_info('GM', 'malibu', color = 'qora', year = 2023, price = 10000)