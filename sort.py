
dispatch_stacks = {
    "REJECTED": {
        "bulky": True,
        "heavy": True
    },
    "STANDARD": {
        "bulky": False,
        "heavy": False
    },
}

def isBulky(width: float, height: float, length: float) -> bool:
    volume = width * height * length

    if (
        (volume >= 1000000) or 
        (width >= 150) or 
        (height >= 150) or 
        (length >= 150)
    ):
        return True
    return False

def isHeavy(mass: float) -> bool:
    if (mass >= 20):
        return True
    return False

""" 
Inputs are of type float 

Units for dimensional units are centimeters. Units for mass if in kilograms

"""
def sort(width: float, height: float, length: float, mass: float) -> str:
    bulky = isBulky(width, height, length)
    heavy = isHeavy(mass)

    for stacks in dispatch_stacks:
        if (
            (bulky == dispatch_stacks[stacks]["bulky"]) and
            (heavy == dispatch_stacks[stacks]["heavy"])
        ):
            print(stacks)
            return stacks

    if bulky != heavy:
        return "SPECIAL"
    
if (__name__ == "__main__"):
    user_input_params = {
        "width": 0.0,
        "length": 0.0,
        "height": 0.0,
        "mass": 0.0,
    }
    user_input = ""
    stack = ""
    
    print("Enter 'q' or 'quit' to quit.\n")
    for inputs in user_input_params:
        while (user_input != 'q' or user_input != "quit"):
            user_input = input(f"Please input the {inputs} of the box:\t")
            if user_input == 'q' or user_input == "quit":
                break

            try:
                user_input_params[inputs] = float(user_input)
                break
            except ValueError:
                print("Try again. Please enter a numerical decimal or integer.")
        if user_input == 'q' or user_input == "quit":
                break
    
    stack = sort(
        user_input_params["width"],
        user_input_params["length"],
        user_input_params["height"],
        user_input_params["mass"],
    )

    print(f"Sorted Stack: {stack}")
            
        