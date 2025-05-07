country = input()
tool = input()

ribbon = 0
hoop = 0
rope = 0

if country == 'Bulgaria':
    ribbon = 9.600 + 9.400
    hoop = 9.750 + 9.750
    rope = 9.500 + 9.400

elif country == 'Russia':
    ribbon = 9.100 + 9.400
    hoop = 9.300 + 9.800
    rope = 9.600 + 9.000

elif country == 'Italy':
    ribbon = 9.200 + 9.500
    hoop = 9.450 + 9.350
    rope = 9.700 + 9.150

if tool == 'ribbon':
    tool_playing = ribbon
elif tool == 'hoop':
    tool_playing = hoop
elif tool == 'rope':
    tool_playing = rope

max_grade = (20 - tool_playing) / 20 * 100

print(f'The team of {country} get {tool_playing:.3f} on {tool}.')
print(f'{max_grade:.2f}%')

