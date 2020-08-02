import zmq
context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")


def add_quantize_task(kmeg_params: dict):
    sender.send_json(kmeg_params)





