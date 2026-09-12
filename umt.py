import itertools

def find_optimal_y_combinations(named_x_values, named_y_values):
    # 1. Generate all possible unique pairs of y values (allowing self-pairing)
    y_combinations = []
    
    for (name1, val1), (name2, val2) in itertools.combinations_with_replacement(named_y_values.items(), 2):
        # Apply your combination formula
        combined_y = ((val1 + val2) * 1.15) * 1.4
        
        y_combinations.append({
            'pair_names': f"{name1} & {name2}",
            'combined_y': combined_y
        })
        
    # Sort combinations from lowest to highest combined_y
    y_combinations.sort(key=lambda item: item['combined_y'])
    
    results = []
    for x_name, x in named_x_values.items():
        # Process the original x through the formula
        final_x = ((((x + 20) * 1.2) * 4) * 1.2)
        
        # Calculate the exact y boundary 
        y_threshold = (5 / 22) * final_x - (10495 / 88)
        
        # Find the first y combination that is strictly greater than the threshold
        best_match = None
        for combo in y_combinations:
            if combo['combined_y'] > y_threshold:
                best_match = combo
                break
                
        results.append({
            'x_name': x_name,
            'original_x': x,
            'y_threshold': y_threshold,
            'best_pair': best_match['pair_names'] if best_match else "No match found",
            'best_combined_y': best_match['combined_y'] if best_match else 0
        })
        
    return results

# Your provided x values
predetermined_x_values = {
    "Tin": 10,
    "Iron": 20,
    "Lead": 30,
    "Cobalt": 50,
    "Aluminium": 65,
    "Silver": 150,
    "Uranium": 180,
    "Vanadium": 240,
    "Tungsten": 300,
    "Gold": 350,
    "Titanium": 400,
    "Molybdenum": 600,
    "Plutonium": 1000,
    "Palladium": 1200,
    "Mithril": 2000,
    "Thorium": 3200,
    "Iridium": 3700,
    "Adamantium": 4500,
    "Rhodium": 15000,
    "Unobtanium": 30000
}

# PLACEHOLDER: Replace these with your actual named y values
predetermined_y_values = {
    "Topaz": 75,
    "Emerald": 200,
    "Sapphire": 250,
    "Ruby": 300,
    "Diamond": 1500,
    "Poudretteite": 1700,
    "Zultanite": 2300,
    "Grandidierite": 4500,
    "Musgravite": 5800,
    "Painite": 12000
}

calculated_data = find_optimal_y_combinations(predetermined_x_values, predetermined_y_values)

# Print the results
print(f"{'X Name':<10} | {'Threshold':<12} | {'Optimal Y Pair':<20} | {'Combined Y Value'}")
print("-" * 65)

for data in calculated_data:
    x_name = data['x_name']
    thresh = data['y_threshold']
    pair = data['best_pair']
    c_val = data['best_combined_y']
    
    print(f"{x_name:<10} | > {thresh:<10.2f} | {pair:<20} | {c_val:.2f}")