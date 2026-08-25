raw_order = "   oRdEr_ID: #89421-US | CuStOmEr: 'sArAh cOnNoR' | iTeM: \"wireless mechanical keyboard\" pRiCe: $149.9982 | StAtUs: PENDING   "

stripped = raw_order.strip()
quotes = stripped.replace("'","")
double_quotes = quotes.replace('"','')
titled = double_quotes.title()
order_id = stripped[11:16]
order_country = stripped[17:19]
customer = titled[32:44]
item = titled[53:81]
price = titled[90:98]
total = round(float(price), 2)
all_caps = titled.upper()
status = all_caps[109:116]


print("==========Reciept==========\n")
print(f"Order ID: {order_id:>10} (Country:{order_country})")
print(f"Customer: {customer:>17}")
print(f"Item: {item:>37}")
print(f"Total Paid: {total:>8}")
print(f"Status: {status:>14}")
print("="*27)
