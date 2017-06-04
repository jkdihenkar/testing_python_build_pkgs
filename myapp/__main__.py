from myapp.worker_lib import Worker


def main():
    w = Worker('AdditionWorker')
    print("Worker {} :: Result {}".format(w.whoami(), w.do_addition(7, 8)))

if __name__ == '__main__':
    main()