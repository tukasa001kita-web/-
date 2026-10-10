import global_value as g
import time
#----------------セーブデータをロードする-----------------
def save_load():
    save_one = open('../save_data/save1.txt','r')
    save_datalist = save_one.read().split("\n")
    print ("savedata",save_datalist)
    #0:stage 1:moruxyz.x 2:moruxyz.y 3:level 4:PRPT
    g.stage = save_datalist[1]
    g.moruxyz.x = int(save_datalist[2])
    g.moruxyz.y = int(save_datalist[3])
    g.level = int(save_datalist[4])
    g.PRPT = int(save_datalist[5])
    
    save_one.close()
    
    savedata_inventory = open('../save_data/save_inventory1.txt','r', encoding='UTF-8')
    save_datalist_inventory = savedata_inventory.read().split("\n")
    print(save_datalist_inventory)
    #reading inbetory 一番初めは日時なので飛ばす。
    inventory_read_Flag = False
    
    for save_inbentory_datalist_x in save_datalist_inventory:
        if inventory_read_Flag == True:
            g.inventory.append(save_inbentory_datalist_x)
        inventory_read_Flag = True
        
    inventory_read_Flag = False
    
    savedata_inventory.close()
        
#-----------------------------セーブする--------------------
def save():
    print("save")
    t = time.localtime()
    d = time.strftime("%Y/%m/%d %H:%M:%S",t)
    new_savedata = open('../save_data/save1.txt',"w")
    new_savedata.write(str(d))
    #この下はセーブしたいものlist
    most_savelist = [g.stage,g.moruxyz.x,g.moruxyz.y,g.level,g.PRPT]
    
    for one_savedata in most_savelist:
        new_savedata.write("\r")
        new_savedata.write(str(one_savedata))
        
    new_savedata.close()
    save_N = 0

    new_savedata_inventory = open('../save_data/save_inventory1.txt',"w",encoding='UTF-8')
    #yer , day and time
    new_savedata_inventory.write(str(d))
    for save_inventory_y in g.inventory:
        new_savedata_inventory.write("\r")
        new_savedata_inventory.write(str(save_inventory_y))
    new_savedata_inventory.close()
