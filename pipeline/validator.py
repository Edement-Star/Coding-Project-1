# Check Data Here
from pipeline import transformer

data_requirements = {'Product': str, 'Provider': str, 'Quantity': int, 'Unit Price': float, 'Date Ordered': tuple, 'Resolved': bool}
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

def correctData(data: list):
    if bool(data):
        for i in range(len(data)):
            #print(i)
            for key, expected_type in data_requirements.items():
                #print(key)
                if key in data[i]:
                    if (
                    #Check for Blanks, Excluding the ones with defaults
                        (key not in data[i] and (key != "Date Ordered" or key != "Resolved"))
                    #Check if not Correct type
                        or (not isinstance(data[i][key], expected_type))
                    ):
                        data = transformer.decide(data, key, i)
                    #Check Date Tuple
                    elif key == "Date Ordered" and len(data[i][key]) != 3:
                        data = transformer.decide(data, key, i)
                    elif key == "Date Ordered" and len(data[i][key]) == 3:
                        for x in range(len(data[i][key])):
                            if x == 0:
                                if data[i][key][x].title() not in months:
                                    data = transformer.decide(data, key, i)
                            elif x == 1:
                                if data[i][key][x] == 0:
                                    data = transformer.decide(data, key, i)
                                elif data[i][key][x] not in range(32):
                                    data = transformer.decide(data, key, i)
                            else:
                                if not isinstance(data[i][key][x], int):
                                    data = transformer.decide(data, key, i)
        return data
    else:
        return False
