import PySimpleGUI as sg

layout = [
    [sg.Input(key = "-INPUT-"), sg.Spin(["km to mile", "kg to pound", "sec to min"], key = "-UNITS-")],
    [sg.Button("Submit", key = "-BUTT1-")],
    [sg.Text("Hello!", key = "-MESSAGE-")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTT1-":
        input_value = values["-INPUT-"]
        if input_value.isnumeric():
            match values["-UNITS-"]:
                case "km to mile":
                    output = round(float(input_value) * 0.6214, 2)
                    window["-MESSAGE-"].update(f"{input_value} kilometres is {output} miles")
                case "kg to pound":
                    output = round(float(input_value) * 2.20462, 2)
                    window["-MESSAGE-"].update(f"{input_value} kg are {output} pounds")
                case "sec to min":
                    output = round(float(input_value) / 60, 2)
                    window["-MESSAGE-"].update(f"{input_value} seconds are {output} minutes")
        else:
            window["-MESSAGE-"].update("You did not enter a valid number")


window.close()
