# Packet size in bytes
PACKET_SIZE = 16

# Number of data fields in packet
PACKET_FIELDS = 8

# Packet format string for use with struct library
PACKET_FORMAT_STRING = "Bx6hH"

# Escape character to return cursor to previous line
LINE_UP = '\033[F'

# Disconnect timeout
TIMEOUT = 1.0

# Poll period
POLL_PERIOD = 0.0005

# Packet header offsets
NODE_ID_POS = 4
PACKET_TYPE_POS = 2

# MAC addresses of Bluno Beetles
# Player 1
P1_IR_TRANSMITTER = "b0:b1:13:2d:cb:8c"
P1_IR_RECEIVER = "c4:be:84:20:1b:09"
P1_IMU_SENSOR = "c4:be:84:20:1a:51"

# Player
P2_IR_TRANSMITTER = "b0:b1:13:2d:d3:79"
P2_IR_RECEIVER = "b0:b1:13:2d:b6:3d"
P2_IMU_SENSOR = "c4:be:84:20:19:4c"

STD_OP_LENGTH = 80
STD_OP_LINES = 20
