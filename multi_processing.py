from multiprocessing import Pool
from multiprocessing import Process
import create_corpus as sc



def multi_make(file_list):

    # process 로 동작
    try:
        pool = Pool(processes=len(file_list))
        var = pool.map(cc.corpus, file_list)
        pool.close()
        pool.join()
        # 한번이라도 실패했는지 체크
        is_fail = False
        for result in var:
            if result == False:
                is_fail = True
        
        if is_fail == True:
         print(u"멀티 생성 실패하였습니다. 하나하나 재 생성하겠습니다.")
         for fa in file_list:
             cc.create_corpus(fa)

    except KeyboardInterrupt:
        print("KeyboardInterrupt sys.exit")
        sys.exit(0)
        print("KeyboardInterrupt os.exit")
        os._exit(os.EX_OK)
        print("KeyboardInterrupt quit")
        quit()
        print("KeyboardInterrupt exit")         
        exit()