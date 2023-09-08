!alias dt embed
<drac2>
character().set_cvar_nx("downtimePoints", 0)
points = int(downtimePoints)
if &ARGS&:
    try: 
        int(&ARGS&[0])
    except "ValueError":
        text = "Wymagana liczba całkowita!"
        return
    value = int(&ARGS&[0])
    if value < 0 and -value > points:
        text = "Nie wystarczająco punktów!"
        return
    points += value
    character().set_cvar("downtimePoints", points)
    text = f"{points} ({'+' if value >= 0 else ''}{value})"
else:
    text = points
</drac2>
-title "Downtime Points"
-desc "{{text}}"