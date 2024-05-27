from queue import Queue

patient_queue = Queue()

while True:
        print("\nDesk Manager - Patient Registration and Appointment System")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            patient_name = input("enter patient name")
            patient_queue.put(patient_name)
            print(f"patient (patient_name) registered")
        elif choice == '2':
            if not patient_queue.empty():
                 remove_patient = patient_queue.get()
                 print(f"patient (removed_patient) removed after meeting the doctor.")
            else:
                 print("No patient is in the queue")
        elif choice == '3' :
            if not patient_queue.empty():
                print("current patient queue: ")
                for patient in list(patient_queue.queue):
                    print(patient)
                print()
            else: print("patient queue is empty")
        elif choice == "4":
            print("Exiting program..")
            break
        else:
             print("invalid choice! pls enter a valid option")