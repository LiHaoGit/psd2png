from psd_tools import PSDImage
import queue,threading,os,sys,time




            

def getQueue():
    files = [file for file in os.listdir('.') if file.endswith('.psd')];
    q = queue.Queue();
    for f in files:
        q.put(f);
    print(">> files. ",q.qsize())
    return q;


q = getQueue()
s = q.qsize()

def converPng():    
    while not q.empty():                
        file = q.get();    
        if file.endswith('.psd'):            
            psd = PSDImage.load(file)
            merged_image = psd.as_PIL();
            png = file[:-3]+'png';
            merged_image.save(png)
            print('>> '+png+' done!')

def conver(threadNum):
    threads=[]    
    for i in range(0,threadNum):        
        t = threading.Thread(target=converPng,name=str(i)+'--worker')        
        threads.append(t)
    return threads;
    
    


if __name__ == '__main__':
    print('>> Start Conver !!')

    threadNum = 5
    argv = sys.argv

    if len(argv)>1:
        try:
            threadNum = int(argv[1])    
        except ValueError as e:
            pass
        
    ts = conver(threadNum)

    for t1 in ts:
        t1.start()

    for t2 in ts:
        t2.join()

    print('>> End Conver !!')
