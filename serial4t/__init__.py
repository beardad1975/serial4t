import serial
import serial.tools.list_ports
import os.path
import platform

__all__ = [ 
            '序列連接', '序列連接microbit'
            
            ]

def detect_potential_ports():
    # code from list_serial_ports 
    
    try:
        old_islink = os.path.islink
        if platform.system() == "Windows":
            os.path.islink = lambda _: False
        all_ports = list(serial.tools.list_ports.comports())
    finally:
        os.path.islink = old_islink

    return [(p.device, p.description) for p in all_ports 
                    if (p.vid, p.pid) in {(0x0D28, 0x0204)} ]


def 序列連接(連接埠, 傳輸率=115200, timeout=None):
    pass


def 序列連接microbit(連接埠='auto', 傳輸率=115200, timeout=None):
    print('connect microbit')
    if 連接埠 == 'auto':
        potential = detect_potential_ports()
        #print(potential)
        microbit_num = len(potential)
        if  microbit_num == 1:
            port = potential[0][0]
            print('port: ', port)
        elif microbit_num > 1:
            _, descriptions = zip(*potential)

            message = f'偵測到{microbit_num}片microbit(如下)。使用自動連接時，請只使用1片'
            message += "\n * " + "\n * ".join(descriptions)
            print(message)
            return
        else :
            print('偵測不到microbit，請確認是否已接上電腦')
            return

class Connection():
    def __init__(self, ser):
        self.ser = ser

    def 傳送位元組(self, send_bytes):
        pass

    def 傳送文字(self, send_text):
        pass

    def 接送位元組(self, bytes_num=None):
        pass

    def 關閉(self):
        pass



### Custom Exceptions
# class ImageReadError(Exception):
#     def __init__(self, value):
#         message = f"無法讀取圖片檔 (檔名:{value})"
#         super().__init__(message)

### wrapper functions


if __name__ == '__main__' :
    pass
    
