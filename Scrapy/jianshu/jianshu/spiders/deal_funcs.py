import re
class DealFunction:
    def format_time(self,time):
        replace_time = re.sub(r'T|\+',' ',time)
        return replace_time
