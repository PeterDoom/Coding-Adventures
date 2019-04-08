value = float(input())
enter_metric = str(input())
exit_metric = str(input())

if enter_metric == "m":
    if exit_metric =="m":
        m_m = value
        print(str(value) + "m")
    elif  exit_metric =="cm":
        m_c= value * 100
        print(str(m_c)+ "cm")
    elif exit_metric == "mm":
        m_mm = value * 1000
        print(str(m_mm)+"mm")
    elif exit_metric == "mi":
        m_mi = value * 0.000621371192
        print(str(m_mi)+ "mi")
    elif exit_metric == "in":
        m_in = value* 39.3700787
        print(str(m_in)+ "in")
    elif exit_metric == "km":
        m_km = value * 0.001
        print(str(m_km) + "km")
    elif exit_metric == "ft":
        m_ft = value * 3.2808399
        print(str(m_ft)+ "ft")
    elif exit_metric == "yd":
        m_yd = value * 1.0936133
        print(str(m_yd)+ "yd")

if enter_metric == "mm":
    if exit_metric =="mm":
        mm_mm = value
        print(str(value) + "mm")
    elif  exit_metric =="cm":
        mm_cm= (value * 100) / 1000
        print(str(m_c)+ "cm")
    elif exit_metric == "mm":
        m_mm = value * 1000
        print(str(m_mm)+"mm")
    elif exit_metric == "mi":
        m_mi = value * 0.000621371192
        print(str(m_mi)+ "mi")
    elif exit_metric == "in":
        m_in = value* 39.3700787
        print(str(m_in)+ "in")
    elif exit_metric == "km":
        m_km = value * 0.001
        print(str(m_km) + "km")
    elif exit_metric == "ft":
        m_ft = value * 3.2808399
        print(str(m_ft)+ "ft")
    elif exit_metric == "yd":
        m_yd = value * 1.0936133
        print(str(m_yd)+ "yd")