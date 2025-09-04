Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each, line_total)

# --- Discount helpers ---
def apply_group_discount(qty, price_each):
    """Apply 10% discount if qty >= 4"""
    subtotal = qty * price_each
    if qty >= 4:
        subtotal *= 0.9
    return subtotal

def apply_member_discount(total, is_member):
    """Apply extra 5% discount if member"""
    if is_member:
        total *= 0.95
    return total



# Part A — Simulated Input

sample_orders = [
    ("Dune", 2),
    ("Barbie", 5),       # group discount applies
    ("Oppenheimer", 1),
    ("Spirited Away", 4) # group discount applies
]

for title, qty in sample_orders:
    if title not in movies or qty <= 0:
        continue
    line_total = apply_group_discount(qty, movies[title])
    purchases.append((title, qty, movies[title], line_total))



# Part B — Receipt

print("\n--- Receipt ---")
grand_total = 0
for title, qty, price_each, line_total in purchases:
    print(f"{title:15} x{qty:<3} @ ${price_each:<5.2f} = ${line_total:.2f}")
    grand_total += line_total

# Member discount (simulated as True)
member = True
grand_total = apply_member_discount(grand_total, member)

print(f"Grand Total: ${grand_total:.2f}")


... 
... # Part C — Sales summary
... 
... tickets_by_movie = {}
... revenue_by_movie = {}
... 
... for title, qty, price_each, line_total in purchases:
...     tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
...     revenue_by_movie[title] = revenue_by_movie.get(title, 0) + line_total
... 
... print("\n--- Sales Summary ---")
... for title in movies.keys():
...     tickets = tickets_by_movie.get(title, 0)
...     revenue = revenue_by_movie.get(title, 0.0)
...     print(f"{title:15} Tickets: {tickets:<3}  Revenue: ${revenue:.2f}")
... 
... 
... 
... # Part E — Analytics
... 
... if purchases:
...     # Top seller by tickets
...     top_title, top_qty = None, -1
...     for title, qty in tickets_by_movie.items():
...         if qty > top_qty:
...             top_title, top_qty = title, qty
...     print("\nTop seller:", top_title, "with", top_qty, "tickets")
... 
...     # Sort by revenue
...     sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
...     print("Movies sorted by revenue:", sorted_by_rev)
... 
...     # Average tickets per purchase
...     total_tickets = sum(qty for _, qty, _, _ in purchases)
...     avg_tickets = total_tickets / len(purchases)
...     print(f"Average tickets per purchase: {avg_tickets:.2f}")
... else:
...     print("\nNo purchases made.")
