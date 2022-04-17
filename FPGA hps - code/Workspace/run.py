import os                                                                       
from multiprocessing import Pool                                                
                                                                          
file1 = "smart_irrigation.py"
file2 = "send_to_cloud.py"
file3 = "rfs_send.py"
processes = (file1, file2, file3)                                    
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
if __name__ == "__main__":
    pool = Pool(processes=3)
    pool.map(run_process, processes)
