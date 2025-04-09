import PySimpleGUI as sg

layout = [
    [sg.Text("Convert KM into Miles", enable_events = True, key = "-TXT-")],
    [sg.Input(key = "-INPUT-")],
    [sg.Button("Submit", key = "-BUTT1-")],
    [sg.Text("", key = "-MESSAGE-")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTT1-":
        input_value = values["-INPUT-"]
        if input_value.isnumeric():
            km_conversion_to_miles = float(input_value) * 0.6214
            window["-TXT-"].update(f"{input_value} kilometres is {km_conversion_to_miles} miles")
            window["-MESSAGE-"].update("")
        else:
            window["-MESSAGE-"].update("You did not enter a valid number")


window.close()
