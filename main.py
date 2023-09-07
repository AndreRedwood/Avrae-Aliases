!alias dt embed
<drac2>
character().set_cvar_nx("downtimePoints", 0)
T=int(downtimePoints)
if &ARGS&:
    T=&ARGS&[0]
else:
    T:"nope"
</drac2>
-title "{{T}}"