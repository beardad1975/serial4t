import serial


__all__ = [ 
            '序列連接', '序列連接microbit'
            
            ]


def 序列連接(連接埠, 傳輸率=115200, timeout=None):
    pass


def 序列連接microbit(連接埠='auto', 傳輸率=115200, timeout=None):
    pass


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
    
