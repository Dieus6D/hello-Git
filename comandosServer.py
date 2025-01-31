/itemedit rename &color nombre
/itemtags effects


Server Item guardar item.
/si give nombre_item
/si rename nombre_item

escudo_tanque_lv1:
    /itemedit rename <aqua>Escudo <dark_green>Lvl 1
    /itemedit lore set 3 Efectos:
    /itemedit lore set 4 <red>- <gray>Lentitud lv1
    /itemedit lore set 5 <green>+ <gray>Aumento de salud lv1
    /itemedit lore set 6 <green>+ <gray>Resistencia lv1
    /itemedit lore set 8 <shadow:#55FF55>Al usar <underlined>click derecho <shadow:#55FF55>todos al rededor de 20 bloques 
    /itemedit lore set 9 <shadow:#55FF55>Obtienen el efecto absorsion durante 15 segundos


    efectos:
        - resistencia lv1 
        - heal boosst lv1
        - slow lv1
    Encantamientos:
        - unbreaking lv1
    Acciones:
        - effect give @a[sort=nearest,distance=0..20] minecraft:absorption 15 
        // /it actions add command effect give @a[sort=nearest,distance=0..20] minecraft:absorption 15
