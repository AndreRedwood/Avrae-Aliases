!alias dt embed
<drac2>
character().set_cvar_nx("downtimePoints", 0)
points = int(downtimePoints)
if &ARGS&:
    try: 
        value = int(&ARGS&[0])
    except "ValueError":
        text = "Downtime points are an integer number."
        return
    if value < 0 and -value > points:
        text = "Your Downtime Points can't be negative."
        return
    points += value
    character().set_cvar("downtimePoints", points)
    text = f"{points} ({'+' if value >= 0 else ''}{value})"
else:
    text = points
</drac2> 
-title "{{character().name}}'s Downtime Points"
-desc "{{text}}"