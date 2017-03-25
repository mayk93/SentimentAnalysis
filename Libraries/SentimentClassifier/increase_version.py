with open("current_version", "r") as source:
    content = source.read().strip()
    numbers = [int(i) for i in content.split(".")]
    numbers[2] += 1

with open("current_version", "w") as destination:
    destination.write(".".join([str(i) for i in numbers]))