!alias dt embed
<drac2>
character().set_cvar_nx("downtimePoints", 0)
points = int(downtimePoints)
if &ARGS&:
    try: 
        int(&ARGS&[0])
    except "ValueError":
        T = "Wymagana liczba całkowita!"
        return
    value = int(&ARGS&[0])
    if value < 0 and -value > points:
        T = "Nie wystarczająco punktów!"
        return
    points += value
    character().set_cvar("downtimePoints", points)
    T=f"{points} ({'+' if value >= 0 else ''}{value})"
else:
    T=points
</drac2>
-title "Downtime Points"
-desc "{{T}}"