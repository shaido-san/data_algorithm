import re
import unicodedata

def slugify(value):
    # 1. 全角文字を半角にしたり、特殊文字を分解
    value = unicodedata.normalize('NFKD', value)
    # 2. 記号や不要な文字を削除
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    # 3. 空白やハイフンをまとめて「-」に
    return re.sub(r'[-\s]+', '-', value)

print(slugify("にゃんこ日記 #23!"))