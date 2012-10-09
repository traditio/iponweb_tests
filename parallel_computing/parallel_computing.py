import csv

from collections import defaultdict
import os
from threading import Thread
from Queue import Queue


def thread(data_source, results_queue):
    result = defaultdict(int)
    with open(data_source, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        for k, v in reader:
            result[k] += int(v)
    results_queue.put(result)


def data_sources(dir):
    dir_content = [os.path.join(dir, f) for f in os.listdir(dir)]
    return filter(os.path.isfile, dir_content)


def parallel_computing():
    sources = data_sources('./data_sources')
    processed = Queue(len(sources))
    threads = [Thread(target=thread, args=(source, processed,)) for source in sources]
    for t in threads:
        t.daemon = True
        t.start()
    result = defaultdict(int)
    for _ in xrange(processed.maxsize):
        for k, v in processed.get().iteritems():
            result[k] += v
    return dict(result)

if __name__ == '__main__':
    print parallel_computing()
