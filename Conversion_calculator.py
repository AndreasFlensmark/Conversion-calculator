#Conversion calulator


Unit_From    ="Deci"
Unit_To      ="Nano"
Value        =202

Unit_names=["Yokto","Zepto","Atto","Femto","Piko","Nano","Mikro","Milli","Centi","Deci","Deka","Hekto","Kilo","Mega","Giga","Tera","Peta","Exa","Zetta","Yotta"]
Unit_values=[-24,-21,-19,-15,-12,-9,-6,-3,-2,-1,1,2,3,6,9,12,15,18,21,24]

def conv_unit(u_from,u_to):
    return 10**(Unit_values[Unit_names.index(u_to)]-Unit_values[Unit_names.index(u_from)])

x=(conv_unit(Unit_From ,Unit_To))
print(Value*x)
