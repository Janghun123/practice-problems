def configure_device(model, capacity, color = 'black', warranty = None):
    
    print(f"Model: {model}")
    print(f"Capacity: {capacity}GB")
    print(f"Color: {color}")
    
    if warranty:
        print(f"Warranty: {warranty} years")
    else:
        print("Warranty: Not specified")
        
configure_device('Model_X', 256)
configure_device('Model_Y', 512, color = 'white', warranty = 2)
