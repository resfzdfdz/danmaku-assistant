
import re
import math

def GetLineNum (s):
    str_width = 0
    for per in s:
        if re.match ('[\u4e00-\u9fff]', per):
            str_width += 2
        elif per == "：":
            str_width += 2
        else:
            str_width += 1

    return str_width

def LineNum2RowNum(n):
    return math.ceil(n/25)

def DanmakuRoll (new_str):
    max_line = 17
    new_sw = GetLineNum(new_str)
    new_rw = LineNum2RowNum(new_sw)
    
    with open ('danmaku_text.txt', 'r', encoding='utf-8') as fp:
        text = fp.read()
        
    split_by_line = text.split("\n")
    if len(split_by_line[0]) == 0:
        split_by_line = split_by_line[1:]

    ## utf-8 every hanzi is 1 length
    rw_list = []
    for per in split_by_line:
        sw = GetLineNum(per)
        rw = LineNum2RowNum(sw)
        rw_list.append (rw)

    ## Total Row Num
    cur_rw = new_rw + sum(rw_list)
    del_rw = 0
    del_pos = -1

    if cur_rw >= max_line:
        for i, per in enumerate(rw_list):
            del_rw += per
            if cur_rw - del_rw < max_line:
                del_pos = i
                break
        
##    print (f"cur_rw  = {cur_rw}")
##    print (f"del_rw  = {del_rw}")
##    print (f"del_pos = {del_pos}")

    new_list = split_by_line[del_pos+1:] + [new_str]
    new_line = "\n".join(new_list)

##    print (new_line)
    with open ('danmaku_text.txt', 'w', encoding='utf-8') as wp:
        wp.write(new_line)
        wp.flush()
        

if __name__ == "__main__":
    ns = "浮生欸：666老奶奶过马路我都不扶就服你们"
##    ns = "666"
    DanmakuRoll (ns)
