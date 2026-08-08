--TASK 0--
using 
gdb main0
we open the code with gdb and then:
disas main
we disassemble the main code then we find check_flag:
disas check_flag
using this we disasssemble the flag function and from there decoding the hexadecimals we find :
HOLB{Reverse_Engineering_is_Fun}
