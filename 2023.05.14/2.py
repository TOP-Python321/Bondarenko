def taxi_cost(distance: int, waiting_time: int = 0) -> int | None:
    if distance < 0 or waiting_time < 0:
        return None
        
    base_cost = 80
    addictional_distance_cost = (distance // 150) * 6
    distance_remainder = distance % 150 
    if distance_remainder > 0:
        addictional_distance_cost += 6
        
    
    waiting_time_cost = waiting_time * 3
    
    total_cost = base_cost + addictional_distance_cost + waiting_time_cost
    
    if distance == 0:
        total_cost += base_cost + waiting_time_cost
        
    return round(total_cost)
    
    
