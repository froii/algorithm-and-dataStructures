
import pulp

model = pulp.LpProblem("Juice_Production", pulp.LpMaximize)

L = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
F = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += L + F, "Total_Products"
model += 2 * L + 1 * F <= 100, "Water"
model += 1 * L <= 50, "Sugar"
model += 1 * L <= 30, "Lemon_Juice"
model += 2 * F <= 40, "Fruit_Puree"

model.solve(pulp.PULP_CBC_CMD(msg=0))

print(f"Lemonade: {L.varValue} units.")
print(f"Fruit Juice: {F.varValue} units.")
print(f"Total Products: {pulp.value(model.objective)} units.")
print(f"Status: {pulp.LpStatus[model.status]}")
