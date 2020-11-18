# Python program that simulates a printer in the lab and assumes that students will print twice in an hour

import random
from Print_job import Print_job
from Print_job import Queue


# function that simulates a lab printer with 20 students per second
def printer_sim():
    printer_speed = int(input('Enter printer how many seconds it takes to print a page: '))
    amount_of_students = int(input('Enter the amount of students in lab: '))
    print("Beginning printer simulation....")
    while printer_speed == 0:
        printer_speed =int(input('Please enter a valid seconds/page: '))

    printer_q = Queue()
    # Assigns a random amount of pages in index 0, 1 and a random time that these pages are requested to print in
    # index 2, 3
    students = [[random.randint(1,20), random.randint(1,20),
                 random.randint(1,3600), random.randint(1,3600)] for i in range(amount_of_students)]
    current_print_job = 0
    # Creates an empty list of Print_job objects
    list_of_Print_jobs = [Print_job() for i in range(2 * amount_of_students)]
    jobs_queue = 0 # A variable that keeps track of order in which requested to print
    average_print_time = 0
    for i in range(3601):  # Simulates every second
        for q in range(amount_of_students): # Checks the list of students if they have submitted a print job
            if students[q][2] == i:
                printer_q.enqueue(list_of_Print_jobs[jobs_queue])
                list_of_Print_jobs[jobs_queue].set_start(i) # Adds the time in which request was sent
                list_of_Print_jobs[jobs_queue].pages = students[q][0] # Adds the pages that are to be printed
                jobs_queue += 1

            if students[q][3] == i:
                printer_q.enqueue(list_of_Print_jobs[jobs_queue])
                list_of_Print_jobs[jobs_queue].set_start(i) # Adds the time in which request was sent
                list_of_Print_jobs[jobs_queue].pages = students[q][1] # Adds the pages that are to be printed
                jobs_queue += 1

        if current_print_job == 0 and printer_q.isEmpty() == False:
            popped_job = printer_q.dequeue()
            popped_job.set_end(i) # Adds the time that the job was beginning to print
            current_print_job = popped_job.get_pages()
        elif current_print_job > 0:
            if i % printer_speed == 0: # Logic for how long it takes for a page to print
                current_print_job -= 1  # A page of the current print job has been printed

    # Calculates the average time spent in queue
    total_time = 0
    amount_completed = 0
    for jobs in list_of_Print_jobs:
        time_until_print = jobs.get_time_print()
        if jobs.get_end_time() == None:
            jobs.set_end(3600)
            time_until_print = jobs.get_time_print()
        else:
            print(f'Time taken from entered into queue to start of printing {time_until_print} seconds')
            amount_completed += 1
        total_time += jobs.get_time_print()
    average_queue_time = total_time / len(list_of_Print_jobs)
    print(f'Average queue time is {average_queue_time} seconds')
    print(f'The amount print jobs started = {amount_completed}')



def main():
    printer_sim()

main()

