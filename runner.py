from browser import document as doc, window, timer
import sys
import time
import traceback

##
# Redirect output to console textarea 
##
def console_write(data):
    doc['console'].value += str(data)


print ("runner");

##
# Function to extract main program and run it
##
def run_program ():
    #find selected Tab (and get its contents)
    doc['console'].value=''
    src=doc['main'].text;
    print ('src', src);
    t0 = time.perf_counter()
    try:
        exec(src,globals())
        state = 1
    except Exception as exc:
        traceback.print_exc()
        state = 0

    print('<completed in %6.2f ms>' % ((time.perf_counter()-t0)*1000.0))
    return state

sys.stdout.write = sys.stderr.write = console_write
run_program()