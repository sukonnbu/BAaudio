import os
def convert_to_wav(path):
    if os.path.isdir(path):
        src_list = os.listdir(path)

        for audio in src_list:
            try:
                os.system(f"ffmpeg.exe -i ./{path}/{audio} ./{path}/{audio[:-4]}.wav")
                os.remove(f"./{path}/{audio}")
                print(f"./{path}/{audio} 파일 삭제")
            except Exception as e:
                print("파일 변환중 오류 발생... 오류 메시지: ", e)

if __name__ == "__main__":
    character = input("원하는 블루아카 캐릭터를 영문으로 입력하세요(예시: Azusa) : ")
    path = f"./{character.replace(' ', '_')}/"

    convert_to_wav(path)
