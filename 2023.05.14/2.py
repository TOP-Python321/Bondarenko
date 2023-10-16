def taxi_cost(length: int, wait: int = 0) -> int | None:
    if length <= 0 or wait <= 0:
        return None
    
    base_cost = 80
    cost_per_meter = 6

    total_cost = base_cost + (length * cost_per_meter)
    total_cost += wait * 3
    total_cost += round(cost_per_meter) * wait

    if length <= 0:
        total_cost += 80
    if wait <= 0:
        total_cost += 0

    return total_cost

