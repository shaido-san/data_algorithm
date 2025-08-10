import time
import threading

def debounce(wait):
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                debounced._timer = None
                fn(*args, **kwargs)

            if debounced._timer is not None:
                debounced._timer.cancel()
            debounced._timer = threading.Timer(wait, call_it)
            debounced._timer.start()

        debounced._timer = None
        return debounced
    return decorator

# 0.3秒入力が止まったら実行
@debounce(0.3)  
def search(keyword):
    print(f"検索API呼び出し: {keyword}")

search("ca")
time.sleep(0.1)
search("cat")   # 前の呼び出しはキャンセルされ、これだけ実行