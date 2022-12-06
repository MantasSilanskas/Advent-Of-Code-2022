def MarkerDetection():
    with open("input.txt") as file:
        data = file.read().strip()

    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            print("Character processed before first marker: ",i)
            break

def StartOfMessageMarker():
    with open("input.txt") as file:
        data = file.read().strip()

    for i in range(14, len(data)):
        if len(set(data[i-14:i])) == 14:
            print("Character processed before start of message marker: ",i)
            break

MarkerDetection()
StartOfMessageMarker()