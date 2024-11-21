capacity=50
objects=[{'weight':20,'value':60},{'weight':30,'value':120},{'weight':10,'value':50}]
for object in objects:
    weight=object.get('weight')
    value = object.get('value')
    object['value_per_weight']=value/weight

left_capacity=capacity
total_value=0
while left_capacity>0:
    value=[]
    for object in objects:
        value.append(object.get('value_per_weight'))
    index=value.index(max(value))
    if left_capacity>=objects[index]['weight']:
        total_value+=objects[index]['value']
        left_capacity -=objects[index]['weight']
        print(f'put all of object {index+1}')
        del objects[index]
    else:
        total_value += objects[index]['value_per_weight']*left_capacity
        print(f'put {left_capacity} of object {index + 1}')
        left_capacity=0
print(total_value)
