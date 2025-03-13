from operator import index
import sys  # 프로그램 종료를 위해 sys 모듈 사용
import Book_Checking_func as bcf

# 사용자에게 보여줄 메뉴 화면
display = '''
-------------------------------------------------------------
1. 도서 추가, 2. 도서 수정, 3. 도서 삭제, 4. 도서 검색, 5. 도서 대여 반납 6. 프로그램종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

# 도서를 저장할 리스트 (초기값: 예제 도서 한 개 포함)
books = [
    {"ISBN": "0000", "제목": "파이썬 프로그래밍", "저자": "홍길동", "대여 여부": False}
]

while True:
    menu = input(display)  # 사용자 입력 받기

    if menu == '1':
        bcf.book_input(books)

    elif menu == '2':  # 도서 수정 기능
        
    elif menu == '3':  # 도서 삭제 기능

    elif menu == '4':  # 도서 목록 보기 (검색 기능 추가)
        
    elif menu == '5' :  # 도서 검색 및 대여/반납 기능
        bcf.book_rent(books)
        
    elif menu == '6':  # 프로그램 종료
        print('\n프로그램 종료')
        sys.exit()

    else:
        print("메뉴 선택을 잘못하셨습니다.")