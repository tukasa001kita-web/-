import global_value as g
#スタート
import start
#モルロードメニュー
import road_stage
#どこかのまち
import dokokanomachi
#道具屋の中
import douguyanonaka
#------------stage call-------------------
def stage_call():
    if g.stage == "1":
        start.stage_start()
    
    if g.stage == "2":
        road_stage.stage_load()
    
    if g.stage == "3":
        dokokanomachi.stage_dokokanomachi()
    
    if g.stage == "3-1":
        douguyanonaka.douguya()
