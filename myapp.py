from worker_lib import Worker

if __name__ == '__main__':
    w = Worker('AdditionWorker')
    print("Worker {} :: Result {}".format(w.whoami(), w.do_addition(7, 8)))
