import time



def test_open_s6(pages):
    
    pages.home.open()
    pages.home.click_galaxys6()
    pages.product.check_tittle_is("Samsung galaxy s6")

def test_two_monitors(pages):
    pages.home.open()
    pages.home.click_monitors()
    
    time.sleep(2)
    
    pages.monitor.check_monitor_count_is(2)