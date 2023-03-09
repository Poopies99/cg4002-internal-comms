from bluno_beetle import BlunoBeetle

class BlunoBeetleGameState(BlunoBeetle):
    def __init__(self, params):
        super(),__init__(params)

    def wait_for_data(self):
        try:
            self.three_way_handshake()
            start_time = time.perf_counter()
            while not self.shutdown.is_set():
                # check for bluetooth communication
                if self.peripheral.waitForNotifications(0.0005):
                    # reset start time if packet is received
                    start_time = time.perf_counter()

                    # check if a full packet is in buffer
                    if self.delegate.buffer_len < PACKET_SIZE:
                        self.fragmented_packet_count += 1
                        continue
                    
                    # full packet in buffer
                    self.process_data()
                    self.processed_bit_count += PACKET_SIZE * 8
                    continue

                # no packet received, check for timeout
                if time.perf_counter() - start_time >= 2.5:
                    self.reconnect()
                    start_time = time.perf_counter()

            # shutdown connection and terminate thread
            self.disconnect()
            print("Beetle ID {} terminated".format(self.beetle_id))
        except Exception as e:
            #print(e)
            self.reconnect()
            self.wait_for_data()



