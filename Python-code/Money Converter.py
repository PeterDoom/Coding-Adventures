value = float(input())
enter_cur = str.upper((input()))
exit_cur = str.upper((input()))

eur = 1.95583
usd = 1.79549
gbp = 2.53405

usd_lev = "{:.2f}".format(value *  usd)
usd_usd = "{:.2f}".format(value * 1)
usd_eur ="{:.2f}".format((value * usd)/ eur)
usd_gbp = "{:.2f}".format((value * usd) / gbp)

lev_usd = "{:.2f}".format(value / usd)
lev_lev = "{:.2f}".format( value * 1)
lev_eur = "{:.2f}".format(value / eur)
lev_gbp = "{:.2f}".format(value / gbp)

eur_usd = "{:.2f}".format((value * eur) / usd)
eur_lev = "{:.2f}".format(value * eur)
eur_eur = "{:.2f}".format(value * 1)
eur_gbp = "{:.2f}".format((value * eur) / gbp)

gbp_usd = "{:.2f}".format((value * gbp) / usd)
gbp_lev = "{:.2f}".format(value * gbp)
gbp_eur = "{:.2f}".format((value * gbp) / eur)
gbp_gbp = "{:.2f}".format(value * 1)

if enter_cur == "USD":
    if exit_cur == "BGN":
        print(str(usd_lev)+ " BGN")
    elif exit_cur == "USD":
        print (str(usd_usd) + " USD")
    elif exit_cur == "EUR":
        print(str(usd_eur) + " EUR")
    elif exit_cur.lower() == "GBP":
        print(str(usd_gbp) + " GBP")

if enter_cur == "BGN":
    if exit_cur == "USD":
        print(str(lev_usd) + " USD")
    elif exit_cur == "BGN":
        print(str(lev_lev) + " BGN")
    elif exit_cur == "EUR":
        print(str(lev_eur) + " EUR")
    elif exit_cur == "GBP":
        print(str(lev_gbp) + " GBP")

if enter_cur == "EUR":
    if exit_cur == "USD":
        print(str(eur_usd) + " USD")
    elif exit_cur == "BGN":
        print(str(eur_lev) + " BGN")
    elif exit_cur == "EUR":
        print(str(eur_eur) + " EUR")
    elif exit_cur == "GBP":
        print(str(eur_gbp) + " GBP")

if enter_cur == "GBP":
    if exit_cur == "USD":
        print(str(gbp_usd) + " USD")
    elif exit_cur == "BGN":
        print(str(gbp_lev) + " BGN")
    elif exit_cur == "EUR":
        print(str(gbp_eur) + " EUR")
    elif exit_cur == "GBP":
        print(str(gbp_gbp) + " GBP")