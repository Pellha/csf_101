from queue import Queue 

def register_patient(queue):
    name = input("Enter patient name: ")
    queue.put(name)
    print("Patient Registered.")

def remove_patient(queue):
    if queue.empty():
        print("No patient in the queue.")
    else:
        removed_patient = queue.get()
        print(f"{removed_patient} has met the docotor and been removed from the queue.")

def display_queue(queue):
    if queue.empty():
        print("No patient in the queue.")
    else:
        print("Current patient queue: ")
        for index, patient in