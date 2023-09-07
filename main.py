!alias gem embed
<drac2>
match "&1&".lower():
    case "malahite":
        T = "Malahite"
        D = "You can invoke this to clean yourself and your equipment from all impurities."
    case "hemanite":
        T = "Hemanite"
        target = combat().get_combatant(argparse(&ARGS&).last('t'))
        D = f"You can invoke this as bonus action to stabilize one dying creature 5ft from you.\n{target.name} is stabilized."
    case "ruby":
        T = "Ruby"
        target = combat().get_combatant(argparse(&ARGS&).last('t'))
        D = f"As an action you can invooke it to heal yourself or one creature 5ft from you for 2d4+2 hp. {target.name}"
    case "azurite":
        T = "Azurite"
        D = f"When rolling d20 you can forgo roll and invoke this gem to get 10 on the dice."
    case "lapis" | "lapis lazuli":
        T = "Lapis Lazuli"
        target = combat().get_combatant(argparse(&ARGS&).last('t'))
        D = f"You can invoke this to gain ability to breathe water for 1 minute."
    case _:
        T= "404"
        D = "Gem &1& not found"
</drac2>
-title "{{T}}"
-desc "{{D}}"