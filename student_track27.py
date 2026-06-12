name=input( ).strip()
total_days=int(input())
day=1
while day<=total_days:
    if day ==3 :
        day+=1
        continue
    print(f"Attendance recorded for {name} on Day {day}")
    day+=1