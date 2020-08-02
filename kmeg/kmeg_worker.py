import zmq
from kmeg.tasks import perform_quantization_task
import sys

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")





if __name__=='__main__':
    print(sys.path)
    while True:
        pay_load = receiver.recv_json()
        perform_quantization_task(pay_load)


