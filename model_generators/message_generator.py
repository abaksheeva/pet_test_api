class MsgGenerator:
    @staticmethod
    def generate_from(code, msg_type, message):
        msg = dict()

        msg['code'] = code
        msg['type'] = msg_type
        msg['message'] = message

        return msg
