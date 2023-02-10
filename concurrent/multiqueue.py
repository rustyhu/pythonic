from multiprocessing import Process, Queue
import time


def recorder_process(recorder_queue: Queue, extractor_queue: Queue):
    try:
        while True:
            request = recorder_queue.get(timeout=1)
            res_str = "recorder get " + str(request)
            extractor_queue.put(res_str)
    except BaseException as e:
        # print("Except:", str(e))
        extractor_queue.close()


def extractor_process(extractor_queue: Queue, results_queue: Queue = None):
    try:
        while True:
            transcript = extractor_queue.get(timeout=1)
            if results_queue:
                results_queue.put(transcript)
            else:
                print(transcript)
    except BaseException as e:
        if results_queue:
            results_queue.close()


if __name__ == "__main__":
    # Set up a Queue to pass data to the update process
    recorder_queue = Queue()
    extractor_queue = Queue()
    # results_queue = Queue()

    # Create two child processes, pass a reference to the Queue to each
    recorder = Process(target=recorder_process, args=(
        recorder_queue, extractor_queue))
    extractor = Process(target=extractor_process, args=(extractor_queue,))
    recorder.start()
    extractor.start()

    for index in range(10):
        recorder_queue.put(index)
        time.sleep(0.5)
    recorder_queue.close()

    recorder.join()
    extractor.join()
