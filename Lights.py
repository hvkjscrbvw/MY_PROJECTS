import time
lights = ['⚫', '⚫', '⚫', '⚫', '⚫']
print(lights)
time.sleep(5)
for i in range(len(lights)):
    lights[i] = '🔴'
    print(lights)
    time.sleep(1)
for i in range(len(lights)):
    lights[i] = '🟢'
print(lights)